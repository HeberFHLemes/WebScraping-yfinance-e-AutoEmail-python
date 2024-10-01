import yfinance

ticker = input("Digite o código da ação desejada: ")
dt_inicial = input("Digite a data inicial (aaaa-mm-dd): ")
dt_final = input("Digite a data final (aaaa-mm-dd): ")
dados = yfinance.Ticker(ticker)
tabela = dados.history(start=dt_inicial,end=dt_final)
tabela

# Valor de fechamento e gráfico com matplotlib -> .plot()
fechamento=tabela.Close
fechamento

#fechamento.plot()

# Análises da ação
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)

print(maxima)
print(minima)
print(media)

# Envio e customização do e-mail
import pyautogui
import pyperclip
import webbrowser
from time import sleep

# Inserir e-mail do destinatário 
destinatario = "exemplo@gmail.com"

assunto = "Análises Projeto 2024"

mensagem = f"""
Bom dia, 

Segue abaixo as análises da ação {ticker} do período solicitado: {dt_inicial} a {dt_final}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${media}
"""

#configurar pausa entre ações do pyautogui.
pyautogui.PAUSE = 3

# abrir o navegador e ir ao g-mail
webbrowser.open("www.gmail.com")
sleep(3)

# clicar no botão Escrever
pyautogui.click(x=82, y=197)

# Preencher Para 
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# Preencher assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Preencher corpo do e-mail
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

# Clicar no botão enviar
pyautogui.click(x=1324, y=990)

# Fechar a aba
pyautogui.hotkey("alt","f4")

print("E-mail enviado com sucesso!")

# Código usado para conseguir as coordenadas na tela:
# import time
# import pyautogui

# time.sleep(5)
# print(pyautogui.position())
