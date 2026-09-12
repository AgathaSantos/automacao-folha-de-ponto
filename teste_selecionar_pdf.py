import pyautogui
import time

arquivo_pdf = r"C:\Users\Agatha\OneDrive\.HTML\Automação_PDFS\pdfs\teste.pdf"

time.sleep(5)

# clicar no campo de nome do arquivo
pyautogui.click(540, 472)

time.sleep(1)

# digitar o caminho do PDF
pyautogui.write(arquivo_pdf, interval=0.02)

time.sleep(2)

# confirmar
pyautogui.press("enter")

print("PDF selecionado!")