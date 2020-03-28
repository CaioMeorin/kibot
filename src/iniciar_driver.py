from colorama import init,Fore,Back,Style

init()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


import time



def iniciar(url):

    #criando objeto option
    options = Options()

    #setando para headless
    options.headless = True

    #criando o driver

    print(Fore.LIGHTYELLOW_EX + 'Iniciando o driver...')
    driver = webdriver.Firefox(options = options) # options=options para realizar as tarefas sem vermos
    driver.maximize_window()
    #executando um get na url

    print(Fore.LIGHTYELLOW_EX + 'Requisitando url...')
    driver.get(url)
    print(Fore.GREEN + 'Pronto para começar\n'+ Fore.LIGHTBLUE_EX)
    #pausando por 5s pra ter certeza que o get() foi concluido
    time.sleep(2)

    return driver