
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
# entrei no navegador

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)

# entrei no site

# fazer login no site
pyautogui.press("tab")
# para selecionar o campo de escrita ou apenas aperta tab da nada mesma
pyautogui.write("pedro.guilherme.berardo@outlook.com")
pyautogui.press("tab")

pyautogui.write("minha_senha")
pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(3)

# loguei no site
 
import pandas as pd
# pandas ferramenta que deixa trabalhar com base de dados

tabela = pd.read_csv("produtos.csv")

print(tabela)

# agora para cadastrar um produto
# codigo
# str = string

for linha in tabela.index:    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=789, y=241)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    # tipo 
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    # categoria 
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    # aperta o botao
    pyautogui.press("enter")
    pyautogui.scroll(5000)

 