import pandas as pd
import webbrowser
import time
import urllib.parse


# Ler Excel
tabela = pd.read_excel("funcionarias.xlsx")


# pegar primeiro telefone
telefone = str(tabela.iloc[0]["TELEFONE"])


# limpar telefone
telefone = (
    telefone
    .replace("(", "")
    .replace(")", "")
    .replace("-", "")
    .replace(" ", "")
)


if not telefone.startswith("55"):
    telefone = "55" + telefone


mensagem = "Olá! Este é um teste de envio automático da folha de ponto."


# transformar mensagem para URL
mensagem = urllib.parse.quote(mensagem)


link = f"https://wa.me/{telefone}?text={mensagem}"


webbrowser.open(link)


time.sleep(8)

# apertar Enter para enviar
import pyautogui
pyautogui.press("enter")


print("Mensagem enviada!")