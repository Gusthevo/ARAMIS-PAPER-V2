#!/usr/bin/env python3
# tcc_single_to_md_marker_newapi.py
"""
Processa um único PDF -> Markdown + JSON + imagens usando a API atualizada do Marker:
PdfConverter, create_model_dict, text_from_rendered.
"""

import sys
import os
import json
import re
import logging
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
from time import perf_counter
from token_counter_gpt import count_gpt_tokens

# ---------- Tentativa de importar a API nova do marker ----------
try:
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered
    MARKER_API = "new"
except Exception as e:
    # fallback para APIs antigas (se por acaso estiver instalada)
    try:
        from marker.convert import convert_single_pdf  # type: ignore
        from marker.models import load_all_models  # type: ignore
        MARKER_API = "legacy"
    except Exception:
        raise ImportError(
            "Não foi possível importar a API do Marker (nem a nova nem a legacy).\n"
            f"Erro: {e}\n\n"
            "Instale marker-pdf ou o repositório oficial:\n"
            "  python -m pip install marker-pdf\n"
            "ou\n"
            "  python -m pip install git+https://github.com/datalab-to/marker.git\n"
        )

# ---------- Logger ----------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("tcc_single_to_md_marker_newapi")

# ---------- Helpers (mesmos do script anterior, adaptados) ----------
def normalize_text_from_rendered(rendered):
    """
    Normaliza a saída de text_from_rendered(rendered) para dict com full_text, images, metadata.
    text_from_rendered geralmente retorna (text, meta, images) ou similar.
    """
    try:
        # text_from_rendered pode retornar (text, out_meta, images)
        if isinstance(rendered, tuple) or isinstance(rendered, list):
            if len(rendered) == 3:
                text, meta, images = rendered
            elif len(rendered) == 2:
                text, second = rendered
                # tentar distinguir dict/meta ou lista/images
                if isinstance(second, dict):
                    meta = second
                    images = []
                else:
                    images = second
                    meta = {}
            else:
                text = rendered[0] if rendered else ""
                meta = {}
                images = []
        else:
            # se receberam apenas texto
            text = str(rendered)
            meta = {}
            images = []
    except Exception:
        text = ""
        meta = {}
        images = []
    return {"full_text": text or "", "metadata": meta or {}, "images": images or []}

def save_images(images, out_dir: Path):
    saved = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, img in enumerate(images):
        # pode ser caminho, dict com bytes, PIL image ou bytes
        if isinstance(img, str) and Path(img).exists():
            dest = out_dir / Path(img).name
            try:
                Path(img).replace(dest)
                saved.append(str(dest))
                continue
            except Exception:
                pass
        if isinstance(img, dict):
            name = img.get("name") or f"image_{i}.png"
            data = img.get("bytes") or img.get("image") or img.get("raw")
            if isinstance(data, (bytes, bytearray)):
                dest = out_dir / name
                with open(dest, "wb") as f:
                    f.write(data)
                saved.append(str(dest))
                continue
        try:
            if hasattr(img, "save"):
                name = f"image_{i}.png"
                dest = out_dir / name
                img.save(dest)
                saved.append(str(dest))
                continue
        except Exception:
            pass
        if isinstance(img, (bytes, bytearray)):
            dest = out_dir / f"image_{i}.bin"
            with open(dest, "wb") as f:
                f.write(img)
            saved.append(str(dest))
            continue
        # fallback
        dest = out_dir / f"image_{i}.txt"
        with open(dest, "w", encoding="utf-8") as f:
            f.write(repr(img))
        saved.append(str(dest))
    return saved

# Padrões de seção (português) - mesmos do pipeline anterior
SECTION_PATTERNS = {
    "capa": r"(?i)(UNIVERSIDADE|FACULDADE|INSTITUTO|CENTRO UNIVERSITÁRIO)[\s\S]{1,400}?(?=\n\n|\n[A-Z]|RESUMO|ABSTRACT)",
    "resumo": r"(?i)(^|\n)(RESUMO)\b[\s\S]{0,400}?(\n\n)([\s\S]*?)(?=\n\n(ABSTRACT|INTRODUÇÃO|1\.|\n[A-Z]{3,}))",
    "abstract": r"(?i)(^|\n)(ABSTRACT)\b[\s\S]{0,400}?(\n\n)([\s\S]*?)(?=\n\n(INTRODUÇÃO|1\.|\n[A-Z]{3,}))",
    "introducao": r"(?i)(INTRODUÇÃO|1\s*\.?\s*INTRODUÇÃO)[\s\S]*?(?=\n(2\.|3\.|REVISÃO|METODOLOGIA|MATERIAL|MÉTODOS)|$)",
    "revisao_literatura": r"(?i)(REVISÃO\s+(DA\s+)?LITERATURA|REVISÃO\s+BIBLIOGRÁFICA|2\s*\.?\s*[A-Z])[\s\S]*?(?=\n(3\.|METODOLOGIA|MATERIAL|MÉTODOS)|$)",
    "metodologia": r"(?i)(METODOLOGIA|MATERIAL\s+E\s+MÉTODOS|PROCEDIMENTOS|3\s*\.?\s*[A-Z])[\s\S]*?(?=\n(4\.|RESULTADOS|RESULTADOS\s+E\s+DISCUSSÃO)|$)",
    "resultados": r"(?i)(RESULTADOS|4\s*\.?\s*[A-Z])[\s\S]*?(?=\n(5\.|DISCUSSÃO|CONCLUSÃO)|$)",
    "discussao": r"(?i)(DISCUSSÃO|5\s*\.?\s*[A-Z])[\s\S]*?(?=\n(6\.|CONCLUSÃO|CONSIDERAÇÕES)|$)",
    "conclusao": r"(?i)(CONCLUSÃO|CONSIDERAÇÕES\s+FINAIS|6\s*\.?\s*[A-Z])[\s\S]*?(?=\n(REFERÊNCIAS|BIBLIOGRAFIA|ANEXOS|$))",
    "referencias": r"(?i)(REFERÊNCIAS|BIBLIOGRAFIA|REFERÊNCIAS\s+BIBLIOGRÁFICAS)[\s\S]*"
}

def extract_sections(full_text: str):
    sections = []
    for section_type, pattern in SECTION_PATTERNS.items():
        try:
            m = re.search(pattern, full_text, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
            if m:
                content = m.group().strip()
                page_start = max(1, m.start() // 2000 + 1)
                page_end = max(1, m.end() // 2000 + 1)
                sections.append({
                    "section_type": section_type,
                    "content": content,
                    "page_start": page_start,
                    "page_end": page_end,
                    "chars": len(content)
                })
        except Exception as e:
            logger.warning(f"Erro pattern {section_type}: {e}")
    return sections

def analyze_text_quality(text: str):
    if not text or not text.strip():
        return {"total_words": 0, "total_sentences": 0, "avg_sentence_length": 0, "avg_word_length": 0, "academic_word_ratio": 0.0, "readability": "desconhecido"}
    words = re.findall(r"\w+['-]?\w*|\w+", text)
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    avg_sentence_len = len(words) / max(1, len(sentences))
    avg_word_len = sum(len(w) for w in words) / max(1, len(words))
    academic = _calculate_academic_word_ratio(text)
    readability = "complexo" if avg_sentence_len > 25 else ("moderado" if avg_sentence_len > 15 else "simples")
    return {"total_words": len(words), "total_sentences": len(sentences), "avg_sentence_length": avg_sentence_len, "avg_word_length": avg_word_len, "academic_word_ratio": academic, "readability": readability}

def _calculate_academic_word_ratio(text: str) -> float:
    academic_words = {'portanto','contudo','entretanto','todavia','ademais','metodologia','resultados','discussão','conclusão','análise','objetivo','amostra','variável','dados'}
    words = re.findall(r"\w+['-]?\w*|\w+", text.lower())
    if not words:
        return 0.0
    return sum(1 for w in words if w in academic_words) / len(words)

def convert_to_markdown(filename: str, sections: List[Dict], full_text: str, metadata: Dict):
    md_lines = []
    md_lines.append(f"# {filename}\n")
    md_lines.append(f"_Processado em: {datetime.now().isoformat()}_\n")
    md_lines.append("## Metadados\n")
    md_lines.append("```json")
    md_lines.append(json.dumps(metadata, ensure_ascii=False, indent=2))
    md_lines.append("```\n")
    if sections:
        md_lines.append("## Seções extraídas\n")
        for s in sections:
            title = s["section_type"].replace("_", " ").title()
            md_lines.append(f"### {title} (pág. {s['page_start']}-{s['page_end']})\n")
            md_lines.append(s["content"].strip() + "\n")
    else:
        md_lines.append("**Nenhuma seção estruturada detectada.**\n")
    md_lines.append("\n---\n")
    md_lines.append("## Texto completo extraído\n")
    md_lines.append(full_text.strip())
    return "\n".join(md_lines)

# ---------- Função principal para processar um PDF usando a API nova ----------
def process_single_pdf_newapi(pdf_path: Path, out_dir: Path, use_models: bool = True, langs: Optional[List[str]] = None, max_pages: Optional[int]=None, start_page: Optional[int]=None):
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = pdf_path.stem
    json_out = out_dir / f"{stem}_extraction.json"
    md_out = out_dir / f"{stem}.md"
    images_dir = out_dir / f"{stem}_images"

    # preparar o "artifact / model dict"
    model_dict = None
    if use_models:
        try:
            # create_model_dict aceita parâmetros dependendo da versão; aqui usamos default/cache
            model_dict = create_model_dict()
            logger.info("create_model_dict() executado com sucesso.")
        except TypeError:
            # fallback: sem args
            model_dict = create_model_dict
        except Exception as e:
            logger.warning(f"create_model_dict falhou: {e}. Prosseguindo sem models.")
            model_dict = None

    try:
        # instanciar PdfConverter com o model/artifact dict quando disponível
        if model_dict:
            try:
                converter = PdfConverter(artifact_dict=model_dict)
            except TypeError:
                # fallback, tentar sem named arg
                converter = PdfConverter(model_dict)
        else:
            converter = PdfConverter()

        # opções (muitas versões aceitam kwargs ao chamar)
        call_kwargs = {}
        if max_pages is not None:
            call_kwargs["max_pages"] = max_pages
        if start_page is not None:
            call_kwargs["start_page"] = start_page
        if langs:
            call_kwargs["langs"] = langs

        # rodar converter
        rendered = converter(str(pdf_path), **call_kwargs)
        # extrair texto/metadados/imagens
        text_res = text_from_rendered(rendered)
        # text_from_rendered pode retornar (text, meta, images) ou (text, _, images)
        if isinstance(text_res, tuple) and len(text_res) >= 1:
            # normalizar
            norm = normalize_text_from_rendered(text_res)
        else:
            # também pode aceitar a própria 'rendered' como argumento
            norm = normalize_text_from_rendered(text_res)

        full_text = norm["full_text"]
        metadata = norm["metadata"]
        images = norm["images"]

    except Exception as e:
        logger.exception(f"Erro ao converter com PdfConverter/text_from_rendered: {e}")
        return {"success": False, "error": str(e)}

    # extrair seções e métricas
    sections = extract_sections(full_text)
    quality = analyze_text_quality(full_text)

    # salvar json e md
    result_data = {
        "filename": pdf_path.name,
        "processed_at": datetime.now().isoformat(),
        "metadata": metadata,
        "sections": sections,
        "quality": quality,
        "text_length": len(full_text)
    }
    with open(json_out, "w", encoding="utf-8") as jf:
        json.dump(result_data, jf, ensure_ascii=False, indent=2)

    saved_images = []
    if images:
        saved_images = save_images(images, images_dir)

    md_text = convert_to_markdown(pdf_path.name, sections, full_text, metadata)
    if saved_images:
        md_text += "\n\n## Imagens extraídas\n"
        for s in saved_images:
            rel = os.path.relpath(s, out_dir)
            md_text += f"![{Path(s).name}]({rel})\n"
    with open(md_out, "w", encoding="utf-8") as mf:
        mf.write(md_text)

    logger.info(f"Salvo: {md_out}  (images: {len(saved_images)})")
    return {"success": True, "md": str(md_out), "json": str(json_out), "images": saved_images}

PDF_PATH = "../data/raw_tccs/2025_tcc_ltpereira.pdf"        # <-- coloque o PDF aqui
OUT_MD = "../data/processed_tccs/2025_tcc_ltpereira2.md"             # <-- markdown sai aqui

def main():
    start_total = perf_counter()
    print("🔄 Carregando modelos...")

    start_models = perf_counter()
    converter = PdfConverter(
        artifact_dict=create_model_dict()
    )
    end_models = perf_counter()

    print("📄 Processando PDF...")
    start_convert = perf_counter()
    rendered = converter(PDF_PATH)
    end_convert = perf_counter()

    print("✏️ Convertendo para markdown...")
    start_md = perf_counter()
    text, _, images = text_from_rendered(rendered)
    end_md = perf_counter()

    print("💾 Salvando arquivo...")
    start_save = perf_counter()
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(text)
    end_save = perf_counter()

    end_total = perf_counter()

    print("======================================")
    print("⏱️   RELATÓRIO DE TEMPO")
    print("======================================")
    print(f"🧠 Carregar modelos:      {end_models - start_models:.2f} s")
    print(f"📄 Converter PDF:         {end_convert - start_convert:.2f} s")
    print(f"✏️ Extrair markdown:      {end_md - start_md:.2f} s")
    print(f"💾 Salvar arquivo:        {end_save - start_save:.2f} s")
    print("--------------------------------------")
    print(f"⏳ Tempo total:           {end_total - start_total:.2f} s")
    print("======================================")

    print("✅ Finalizado — markdown salvo em:", OUT_MD)
    tokens = count_gpt_tokens(OUT_MD)
    print(f"🔢 Quantidade de tokens do GPT-4 no markdown: {tokens:,}")

if __name__ == "__main__":
    main()