import pandas as pd
import pdfplumber
import os


# Ler Excel
tabela_excel = pd.read_excel("funcionarias.xlsx")
tabela_excel.columns = tabela_excel.columns.str.strip()


tabela_excel["Funcionária"] = (
    tabela_excel["Funcionária"]
    .astype(str)
    .str.strip()
    .str.upper()
)


PASTA = "pdfs"

funcionarias = []


# Ler PDFs
for arquivo in os.listdir(PASTA):

    if arquivo.endswith(".pdf"):

        caminho = os.path.join(PASTA, arquivo)

        with pdfplumber.open(caminho) as pdf:

            texto = ""

            for pagina in pdf.pages:
                texto += pagina.extract_text() + "\n"


        linhas = texto.split("\n")

        nome = None

        for linha in linhas:

            if "Nome :" in linha:

                nome = linha.split("Nome :")[1]
                nome = nome.split("Crachá")[0]
                nome = nome.strip()

                partes = nome.split(" ", 1)

                if partes[0].isdigit():
                    nome = partes[1]

                break


        if nome:
            funcionarias.append({
                "nome": nome,
                "arquivo": arquivo
            })


# ==========================
# GERAR CONFERÊNCIA
# ==========================

resultado = []


for index, linha in tabela_excel.iterrows():

    nome = linha["Funcionária"]
    escola = linha["Escola"]

    encontrado = None


    for f in funcionarias:

        if f["nome"].strip().upper() == nome:

            encontrado = f["arquivo"]
            break


    if encontrado:
        status = "Recebido ✅"
    else:
        status = "Faltando ❌"


    resultado.append({
        "Escola": escola,
        "Funcionária": nome,
        "Status": status,
        "Arquivo PDF": encontrado if encontrado else ""
    })


# Criar Excel

df_resultado = pd.DataFrame(resultado)

df_resultado.to_excel(
    "resultado_conferencia.xlsx",
    index=False
)


print("Arquivo resultado_conferencia.xlsx criado com sucesso!")