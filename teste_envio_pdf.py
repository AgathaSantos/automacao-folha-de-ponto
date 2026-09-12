import pyautogui
import time
import webbrowser


numero = "5511973837997"  # coloque seu número de teste
arquivo_pdf = r"C:\Users\Agatha\OneDrive\.HTML\Automação_PDFS\pdfs\teste.pdf"


mensagem = "Olá, este é um teste de envio automático da folha de ponto."


# Abre conversa no WhatsApp
link = f"https://wa.me/{numero}?text={mensagem}"

webbrowser.open(link)

time.sleep(8)


# Envia a mensagem
pyautogui.press("enter")

time.sleep(3)


# Abre o botão de anexar
pyautogui.hotkey("ctrl", "alt", "u")