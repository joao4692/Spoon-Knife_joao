import fitz  # PyMuPDF
import json

# Nome do arquivo PDF que está na raiz
arquivo_pdf = "ementa_curso_excel_avancado.pdf"

doc = fitz.open(arquivo_pdf)
dados_estruturados = []

print(f"Processando o arquivo: {arquivo_pdf}...")

# Percorre todas as páginas do PDF
for num_pagina, pagina in enumerate(doc):
    texto = pagina.get_text()
    
    # Remove quebras de linha excessivas para o texto ficar limpo
    texto_limpo = " ".join(texto.split())

    if not texto_limpo.strip():
        continue  # Pula páginas em branco

    # Cria um bloco simulando um registro que irá para o banco
    bloco = {
        "id_bloco": num_pagina + 1,
        "curso": "Excel Avançado",
        "pagina": num_pagina + 1,
        "conteudo_texto": texto_limpo
    }
    
    dados_estruturados.append(bloco)

# Salva o resultado em um arquivo JSON
# Salva o resultado em um arquivo JSON formatado e legível
with open("ementa_processada.json", "w", encoding="utf-8") as f:
    json.dump(dados_estruturados, f, ensure_ascii=False, indent=4)

print(f"\n[Sucesso] {len(dados_estruturados)} páginas processadas e salvas em 'ementa_processada.json'!")