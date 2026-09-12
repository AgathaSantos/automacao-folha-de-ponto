import pyautogui
import time
import webbrowser


numero = "5511973837997"

mensagem = "Teste de automação"


link = f"https://wa.me/{numero}?text={mensagem}"

webbrowser.open(link)

time.sleep(8)

pyautogui.press("enter")