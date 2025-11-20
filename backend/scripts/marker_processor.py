import os
import json
import pandas as pd
from pathlib import Path
from typing import List, Dict, Optional
from marker import convert_single_pdf
from marker.models import load_all_models
from marker.schema import Page, Block, Line, Span
import logging
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TCCSegment:
    section_type: str
    content: str
    page_start: int
    page_end: int
    confidence: float
    metadata: Dict

class MarkerTCCProcessor:
    def __init__(self, model_cache_dir: str = "./model_cache"):
        self.model_cache_dir = Path(model_cache_dir)
        self.model_cache_dir.mkdir(exist_ok=True)
        
        # Carrega modelos do Marker
        self.model = load_all_models(cache_dir=self.model_cache_dir)
        self.logger = self._setup_logging()
    
    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(__name__)
    
    def process_pdf(self, pdf_path: Path, **kwargs) -> Dict:
        """
        Processa um único PDF usando Marker
        """
        try:
            self.logger.info(f"Processando: {pdf_path.name}")
            
            # Configurações do Marker
            marker_config = {
                "model": self.model,
                "max_pages": kwargs.get('max_pages', None),
                "start_page": kwargs.get('start_page', 1),
                "langs": ['pt']  # Português como idioma principal
            }
            
            # Converte o PDF
            full_text, images, out_meta = convert_single_pdf(str(pdf_path), **marker_config)
            
            return {
                "success": True,
                "filename": pdf_path.name,
                "full_text": full_text,
                "images": len(images),
                "metadata": out_meta,
                "pages_processed": len(out_meta.get("pages", [])),
                "processing_time": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Erro ao processar {pdf_path}: {str(e)}")
            return {
                "success": False,
                "filename": pdf_path.name,
                "error": str(e)
            }
    
    def extract_sections(self, full_text: str, metadata: Dict) -> List[TCCSegment]:
        """
        Extrai seções acadêmicas do texto usando heurísticas e regex
        """
        sections = []
        
        # Padrões para identificar seções (em português)
        section_patterns = {
            "capa": r"(?:UNIVERSIDADE|FACULDADE|INSTITUTO)[\s\S]{1,200}?(?=\n\n|\n[A-Z])",
            "resumo": r"RESUMO[\s\S]*?(?=ABSTRACT|INTRODUÇÃO|\n\n[A-Z]{3,})",
            "abstract": r"ABSTRACT[\s\S]*?(?=INTRODUÇÃO|\n\n[A-Z]{3,})",
            "introducao":r"INTRODUÇÃO[\s\S]*?(?=\d\s|REVISÃO|METODOLOGIA|OBJETIVO GERAL|OBJETIVOS ESPECÍFICOS|JUSTIFICATIVA|DECLARAÇÃO DO PROBLEMA|PROBLEMA DE PESQUISA|QUESTÃO DE PESQUISA|\n\n\d)",
            "revisao_literatura": r"(?:REVISÃO DA LITERATURA|REVISÃO BIBLIOGRÁFICA|REVISÃO)[\s\S]*?(?=2\s|3\s|METODOLOGIA)",
            "metodologia": r"(?:METODOLOGIA|PROCEDIMENTO METODOLÓGICO|PROPOSTA)[\s\S]*?(?=3\s|4\s|RESULTADOS|ANÁLISE|DISCUSSÃO|CONCLUSÃO)",
            "resultados": r"RESULTADOS[\s\S]*?(?=4\s|5\s|DISCUSSÃO|CONCLUSÃO)",
            "discussao": r"DISCUSSÃO[\s\S]*?(?=5\s|CONCLUSÃO|CONSIDERAÇÕES)",
            "conclusao": r"CONCLUSÃO[\s\S]*?(?=REFERÊNCIAS|BIBLIOGRAFIA|ANEXOS)",
            "referencias": r"(?:REFERÊNCIAS|BIBLIOGRAFIA)[\s\S]*?(?=ANEXOS|APÊNDICES|$)"
        }
        
        for section_type, pattern in section_patterns.items():
            import re
            match = re.search(pattern, full_text, re.IGNORECASE | re.MULTILINE)
            if match:
                content = match.group().strip()
                # Estima páginas baseado na posição no texto
                page_start = self._estimate_page(full_text, match.start())
                page_end = self._estimate_page(full_text, match.end())
                
                sections.append(TCCSegment(
                    section_type=section_type,
                    content=content,
                    page_start=page_start,
                    page_end=page_end,
                    confidence=0.9,  # Marker fornece confiança por bloco
                    metadata={
                        "char_range": (match.start(), match.end()),
                        "word_count": len(content.split()),
                        "pattern_used": pattern
                    }
                ))
        
        return sections
    
    def analyze_text_quality(self, text: str) -> Dict:
        """
        Analisa a qualidade do texto extraído
        """
        words = text.split()
        sentences = text.split('.')
        
        metrics = {
            "total_words": len(words),
            "total_sentences": len(sentences),
            "avg_sentence_length": len(words) / max(1, len(sentences)),
            "avg_word_length": sum(len(word) for word in words) / max(1, len(words)),
            "academic_word_ratio": self._calculate_academic_word_ratio(text),
            "readability_score": self._estimate_readability(text)
        }
        
        return metrics
    
    def _estimate_page(self, text: str, char_position: int, chars_per_page: int = 2500) -> int:
        """Estima o número da página baseado na posição do caractere"""
        return max(1, char_position // chars_per_page + 1)
    
    def _calculate_academic_word_ratio(self, text: str) -> float:
        """Calcula a proporção de palavras acadêmicas"""
        academic_words = {
            'portanto', 'contudo', 'entretanto', 'todavia', 'ademais',
            'consequentemente', 'posteriormente', 'anteriormente',
            'metodologia', 'resultados', 'discussão', 'conclusão',
            'hipótese', 'premissa', 'pressuposto', 'paradigma',
            'análise', 'síntese', 'fundamentação', 'embasamento'
        }
        words = text.lower().split()
        if not words:
            return 0
        
        academic_count = sum(1 for word in words if word in academic_words)
        return academic_count / len(words)
    
    def _estimate_readability(self, text: str) -> str:
        """Estima a legibilidade do texto"""
        words = text.split()
        avg_sentence_len = len(words) / max(1, text.count('.') + text.count('!') + text.count('?'))
        
        if avg_sentence_len > 25:
            return "complexo"
        elif avg_sentence_len > 15:
            return "moderado"
        else:
            return "simples"

class BatchTCCProcessor:
    """
    Processador em lote para múltiplos TCCs
    """
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.processor = MarkerTCCProcessor()
        
        # Diretórios de saída organizados
        (self.output_dir / "raw_extractions").mkdir(exist_ok=True)
        (self.output_dir / "segmented").mkdir(exist_ok=True)
        (self.output_dir / "analysis").mkdir(exist_ok=True)
    
    def process_batch(self, max_files: int = None) -> pd.DataFrame:
        """
        Processa todos os PDFs no diretório de entrada
        """
        pdf_files = list(self.input_dir.glob("*.pdf"))
        if max_files:
            pdf_files = pdf_files[:max_files]
        
        self.processor.logger.info(f"Encontrados {len(pdf_files)} arquivos PDF")
        
        results = []
        
        for pdf_file in pdf_files:
            try:
                # Processa o PDF
                extraction_result = self.processor.process_pdf(pdf_file)
                
                if not extraction_result["success"]:
                    self.processor.logger.warning(f"Falha no processamento: {pdf_file.name}")
                    continue
                
                # Extrai seções
                sections = self.processor.extract_sections(
                    extraction_result["full_text"],
                    extraction_result["metadata"]
                )
                
                # Analisa qualidade
                quality_metrics = self.processor.analyze_text_quality(
                    extraction_result["full_text"]
                )
                
                # Compila resultados
                tcc_result = {
                    "filename": pdf_file.name,
                    "processing_success": True,
                    "total_pages": extraction_result["pages_processed"],
                    "total_words": quality_metrics["total_words"],
                    "sections_found": len(sections),
                    "section_types": [s.section_type for s in sections],
                    "academic_word_ratio": quality_metrics["academic_word_ratio"],
                    "readability_level": quality_metrics["readability_score"],
                    "processing_time": extraction_result["processing_time"],
                    "sections": [
                        {
                            "type": s.section_type,
                            "word_count": s.metadata["word_count"],
                            "page_range": f"{s.page_start}-{s.page_end}",
                            "content_preview": s.content[:200] + "..." if len(s.content) > 200 else s.content
                        }
                        for s in sections
                    ]
                }
                
                results.append(tcc_result)
                
                # Salva extração completa
                self._save_individual_result(pdf_file, extraction_result, sections, quality_metrics)
                
                self.processor.logger.info(f"✅ Processado: {pdf_file.name}")
                
            except Exception as e:
                self.processor.logger.error(f"Erro no processamento em lote para {pdf_file.name}: {str(e)}")
                results.append({
                    "filename": pdf_file.name,
                    "processing_success": False,
                    "error": str(e)
                })
        
        # Salva resumo em CSV
        self._save_summary_csv(results)
        
        return pd.DataFrame(results)
    
    def _save_individual_result(self, pdf_file: Path, extraction: Dict, sections: List[TCCSegment], quality: Dict):
        """Salva resultado individual em JSON"""
        result_data = {
            "metadata": {
                "filename": pdf_file.name,
                "processed_at": datetime.now().isoformat(),
                "marker_metadata": extraction.get("metadata", {})
            },
            "extraction_quality": quality,
            "sections": [
                {
                    "section_type": s.section_type,
                    "content": s.content,
                    "page_range": [s.page_start, s.page_end],
                    "confidence": s.confidence,
                    "metadata": s.metadata
                }
                for s in sections
            ],
            "full_text": extraction["full_text"]
        }
        
        output_file = self.output_dir / "raw_extractions" / f"{pdf_file.stem}_extraction.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result_data, f, ensure_ascii=False, indent=2)
    
    def _save_summary_csv(self, results: List[Dict]):
        """Salva resumo em CSV para análise"""
        df = pd.DataFrame([
            {
                "filename": r["filename"],
                "success": r["processing_success"],
                "pages": r.get("total_pages", 0),
                "words": r.get("total_words", 0),
                "sections": r.get("sections_found", 0),
                "academic_ratio": r.get("academic_word_ratio", 0),
                "readability": r.get("readability_level", "unknown"),
                "section_types": ", ".join(r.get("section_types", []))
            }
            for r in results
        ])
        
        csv_path = self.output_dir / "analysis" / "tcc_processing_summary.csv"
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        self.processor.logger.info(f"Resumo salvo em: {csv_path}")

# Exemplo de uso
if __name__ == "__main__":
    # Configurações
    INPUT_DIR = "data/raw_tccs"
    OUTPUT_DIR = "data/processed"
    MAX_FILES = 10  # None para processar todos
    
    # Processa em lote
    batch_processor = BatchTCCProcessor(INPUT_DIR, OUTPUT_DIR)
    results_df = batch_processor.process_batch(max_files=MAX_FILES)
    
    print(f"\n📊 Processamento concluído!")
    print(f"✅ Sucessos: {len(results_df[results_df['processing_success'] == True])}")
    print(f"❌ Falhas: {len(results_df[results_df['processing_success'] == False])}")
    print(f"📁 Resultados salvos em: {OUTPUT_DIR}")