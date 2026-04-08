import openreview
import pandas as pd
import os
import re  
from dotenv import load_dotenv
from tqdm import tqdm
import fitz

load_dotenv()

client = openreview.api.OpenReviewClient(
    baseurl='https://api2.openreview.net',
    username=os.getenv('OPENREVIEW_USERNAME'),
    password=os.getenv('OPENREVIEW_PASSWORD')
)

print("Buscando submissões do ICLR 2025...")
submissions = client.get_all_notes(
    invitation="ICLR.cc/2025/Conference/-/Submission",
    details='directReplies'
)

dataset = []

def limpar_e_achatar_texto(texto):
    if not texto: return ''
    texto = str(texto)
    
    # Remove cabeçalho/rodapé da conferência
    texto = re.sub(r'Under review as a conference paper at ICLR \d{4}', '', texto, flags=re.IGNORECASE)
    # Remove colunas de numeração de linhas (5 ou mais números isolados)
    texto = re.sub(r'(?:\b\d+\b\s*){5,}', ' ', texto)
    
    # Achata o texto e transforma múltiplos espaços perdidos em um só
    texto = texto.replace('\n', ' ').replace('\r', '')
    texto = re.sub(r'\s{2,}', ' ', texto)
    
    return texto.strip()

print("Processando revisões, baixando PDFs e calculando médias...")
for sub in tqdm(submissions):
    title = limpar_e_achatar_texto(sub.content.get('title', {}).get('value', ''))
    authors = sub.content.get('authors', {}).get('value', ['Anonymous'])
    
    # Estrutura base com a coluna paper_text e avg_confidence
    row = {
        'paper_id': sub.id,
        'title': title,
        'authors': ", ".join(authors),
        'decision': 'Unknown',
        'paper_text': '',  
        'avg_rating': None,
        'avg_confidence': None,  # <--- NOVA COLUNA
        'avg_soundness': None,
        'avg_presentation': None,
        'avg_contribution': None
    }
    
    # ==========================================
    # EXTRAÇÃO DO PDF DO ARTIGO
    # ==========================================
    try:
        pdf_bytes = client.get_pdf(id=sub.id)
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text_chunks = [page.get_text() for page in doc]
        # Aplica a limpeza no texto extraído
        row['paper_text'] = limpar_e_achatar_texto(" ".join(text_chunks))
        doc.close()
    except Exception as e:
        row['paper_text'] = f"[ERRO AO EXTRAIR PDF: {e}]"
    # ==========================================

    # Prepara as colunas dos revisores incluindo confidence e summary
    for i in range(1, 5):
        row[f'review_{i}_rating'] = ''
        row[f'review_{i}_confidence'] = '' # <--- NOVA COLUNA
        row[f'review_{i}_summary'] = ''    # <--- NOVA COLUNA
        row[f'review_{i}_soundness'] = ''
        row[f'review_{i}_presentation'] = ''
        row[f'review_{i}_contribution'] = ''
        row[f'review_{i}_strengths'] = ''
        row[f'review_{i}_weaknesses'] = ''
        
    reviews = []
    
    if 'directReplies' in sub.details:
        for reply in sub.details['directReplies']:
            invitations = reply.get('invitations', [])
            
            if any('Decision' in inv for inv in invitations):
                row['decision'] = limpar_e_achatar_texto(reply['content'].get('decision', {}).get('value', 'Unknown'))
                
            if any('Official_Review' in inv for inv in invitations):
                reviews.append(reply['content'])
    
    # Dicionário de notas atualizado com confidence
    temp_scores = {'rating': [], 'confidence': [], 'soundness': [], 'presentation': [], 'contribution': []}
    
    for idx, content in enumerate(reviews):
        if idx >= 4: 
            break
            
        def get_val(key):
            return content.get(key, {}).get('value', '')
        
        def get_score(key):
            val = get_val(key)
            if val == '': return ''
            return str(val).split(':')[0].strip()
        
        prefix = f'review_{idx+1}_'
        
        r_rating = get_score('rating')
        r_conf = get_score('confidence')   # <--- NOVA COLUNA
        r_sound = get_score('soundness')
        r_pres = get_score('presentation')
        r_contrib = get_score('contribution')
        
        row[prefix + 'rating'] = r_rating
        row[prefix + 'confidence'] = r_conf # <--- NOVA COLUNA
        row[prefix + 'soundness'] = r_sound
        row[prefix + 'presentation'] = r_pres
        row[prefix + 'contribution'] = r_contrib
        
        # Captura os textos incluindo o summary
        row[prefix + 'summary'] = limpar_e_achatar_texto(get_val('summary')) # <--- NOVA COLUNA
        row[prefix + 'strengths'] = limpar_e_achatar_texto(get_val('strengths'))
        row[prefix + 'weaknesses'] = limpar_e_achatar_texto(get_val('weaknesses'))

        if r_rating.isdigit(): temp_scores['rating'].append(int(r_rating))
        if r_conf.isdigit(): temp_scores['confidence'].append(int(r_conf)) # <--- NOVA COLUNA
        if r_sound.isdigit(): temp_scores['soundness'].append(int(r_sound))
        if r_pres.isdigit(): temp_scores['presentation'].append(int(r_pres))
        if r_contrib.isdigit(): temp_scores['contribution'].append(int(r_contrib))

    if temp_scores['rating']: row['avg_rating'] = round(sum(temp_scores['rating']) / len(temp_scores['rating']), 2)
    if temp_scores['confidence']: row['avg_confidence'] = round(sum(temp_scores['confidence']) / len(temp_scores['confidence']), 2) # <--- NOVA COLUNA
    if temp_scores['soundness']: row['avg_soundness'] = round(sum(temp_scores['soundness']) / len(temp_scores['soundness']), 2)
    if temp_scores['presentation']: row['avg_presentation'] = round(sum(temp_scores['presentation']) / len(temp_scores['presentation']), 2)
    if temp_scores['contribution']: row['avg_contribution'] = round(sum(temp_scores['contribution']) / len(temp_scores['contribution']), 2)

    dataset.append(row)

# Converte para DataFrame
df = pd.DataFrame(dataset)

print("\nSeparando e salvando os arquivos CSV (Oral, Spotlight, Poster, Rejected)...")

# Garante que as pastas de destino existam para não dar erro na hora de salvar
os.makedirs('../data/open_review_datasets_improved', exist_ok=True)

# Categoriza
def categorizar_decisao(decisao):
    dec_lower = str(decisao).lower()
    if 'oral' in dec_lower: return 'oral'
    elif 'spotlight' in dec_lower: return 'spotlight'
    elif 'poster' in dec_lower: return 'poster'
    elif 'reject' in dec_lower: return 'rejected'
    else: return 'other'

df['categoria_temp'] = df['decision'].apply(categorizar_decisao)

categorias_principais = ['oral', 'spotlight', 'poster', 'rejected']

for cat in categorias_principais:
    df_filtrado = df[df['categoria_temp'] == cat].copy()
    if not df_filtrado.empty:
        df_filtrado = df_filtrado.drop(columns=['categoria_temp'])
        # Ajustei o caminho aqui também para manter o padrão que você usou no 'other'
        nome_arquivo = f'../data/open_review_datasets_improved/iclr_2025_{cat}.csv'
        # quoting=1 garante que vírgulas no meio do texto do PDF não quebrem o CSV
        df_filtrado.to_csv(nome_arquivo, index=False, quoting=1) 
        print(f"- {nome_arquivo} salvo com sucesso.")

df_outros = df[df['categoria_temp'] == 'other'].copy()
if not df_outros.empty:
    df_outros = df_outros.drop(columns=['categoria_temp'])
    df_outros.to_csv('../data/open_review_datasets_improved/iclr_2025_other.csv', index=False, quoting=1)
    print("- iclr_2025_other.csv salvo com sucesso.")

print("\nExtração completa! Textos e revisões alinhados e limpos em linha única.")