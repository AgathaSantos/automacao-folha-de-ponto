import pandas as pd
import pyautogui
import time
import webbrowser
import urllib.parse
import os


# Ler Excel
tabela = pd.read_excel("funcionarias.xlsx")

total = len(tabela)

print(f"Total de funcionárias: {total}")

webbrowser.open("https://web.whatsapp.com")

time.sleep(15)

for index, linha in tabela.iterrows():

    print(f"\nProcessando {index+1}/{total}")
    funcionaria = (
        str(linha["Funcionária"])
        .strip()
        .upper()
    )

    telefone = str(linha["TELEFONE"])

    telefone = (
        telefone
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    if not telefone.startswith("55"):
        telefone = "55" + telefone


    print("\nEnviando para:", funcionaria)
    print("Telefone:", telefone)

    # procurar PDF pelo nome
    pasta_pdf = "pdfs"

    arquivo_pdf = None

    for arquivo in os.listdir(pasta_pdf):

        if funcionaria.upper() in arquivo.upper():
            arquivo_pdf = os.path.join(pasta_pdf, arquivo)
            break

    print("Nome vindo do Excel:")
    print(funcionaria)


    if arquivo_pdf is None:
        print("PDF não encontrado:", funcionaria)
        continue

    print("Funcionária:", funcionaria)
    print("Telefone:", telefone)
    print("PDF:", arquivo_pdf)


    # mensagem
    mensagem = f"Olá, {funcionaria}. Segue sua folha de ponto."

    mensagem = urllib.parse.quote(mensagem)


    # abrir WhatsApp
   # procurar contato pelo número no WhatsApp

    pyautogui.click(229, 164) # barra de pesquisa do WhatsApp

    time.sleep(1)

    pyautogui.write(telefone, interval=0.05)

    time.sleep(3)

    pyautogui.press("enter")

    time.sleep(5)


    # enviar mensagem
    # escrever mensagem
    mensagem = f"Olá, {funcionaria}. Segue sua folha de ponto. Tire Duas Copias e Assine as duas (MAS DEIXE UMA EM BRANCO COM ASSINATURA). Lembresse, sempre 5 minutos antes da entrada e 5 minutos dps da saida (OSCILA)!"

    pyautogui.write(mensagem, interval=0.03)

    time.sleep(2)

    # enviar mensagem
    pyautogui.press("enter")

    time.sleep(7)

    # clicar no clipe de anexar
    pyautogui.click(665, 988)

    time.sleep(2)

    # clicar em Documento
    # coloque aqui a posição que você descobriu
    pyautogui.click(671, 691)

    time.sleep(3)

    # abrir campo de caminho do arquivo
    pyautogui.click(540, 472)

    time.sleep(1)


    # digitar caminho do PDF
    pyautogui.write(
        os.path.abspath(arquivo_pdf),
        interval=0.02
    )

    time.sleep(2)

    pyautogui.press("enter")

    time.sleep(5)

    # clicar em enviar PDF
    pyautogui.click(1870,989)

    time.sleep(7)

print("\nTodos os envios foram concluídos! ✅")

