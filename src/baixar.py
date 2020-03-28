from colorama import init,Fore,Back,Style

init()

import urllib.request
import requests
import subprocess
import time
from os import path
from bs4 import BeautifulSoup

from random import randint

def twitter(driver,n):


    directory = 'imagens\\twitter\\'
    pre = 'Twitter '

    if not path.exists(directory):
        subprocess.run(['mkdir', directory], shell =True)

    for i in range(int(n)):

        #pegando o source da pagina
        page = driver.page_source
        driver.execute_script("window.scrollBy(0,720)")
        #usando lxml de parser, criando a sopa
        soup = BeautifulSoup(page, 'lxml')

        # grab todas as imagens de post
        imgs = soup.find_all("img", attrs={"alt":"Imagem"})

    return (imgs, directory, pre)

def reddit(driver, n):


    directory = 'imagens\\reddit\\'
    pre = 'Reddit '

    if not path.exists(directory):
        subprocess.run(['mkdir', directory], shell =True)

    for i in range(int(n)):

        #pegando o source da pagina
        page = driver.page_source
        driver.execute_script("window.scrollBy(0,720)")
        #usando lxml de parser, criando a sopa
        soup = BeautifulSoup(page, 'lxml')

        # grab todas as imagens de post
        imgs = soup.find_all("img", attrs={"alt":"Post image"})

    return (imgs, directory, pre)

def facebook(driver, n):


    directory = 'imagens\\facebook\\'
    pre = 'facebook '

    if not path.exists(directory):
        subprocess.run(['mkdir', directory], shell =True)
    
    for i in range(int(n)):

        #pegando o source da pagina
        page = driver.page_source
        driver.execute_script("window.scrollBy(0,720)")
        #usando lxml de parser, criando a sopa
        soup = BeautifulSoup(page, 'lxml')

        # grab todas as imagens de post
        imgs = soup.find_all("img", {"class":"img"})

    return (imgs, directory, pre)

def baixar(driver, url):


    if not path.exists("imagens"):
        subprocess.run(['mkdir', 'imagens'], shell =True)

    n = input("Quantos ciclos? (0-10 imagens por ciclo): ")

    print(Fore.CYAN + 'Baixando imagens\n')


    if "reddit" in url:
        imgs, directory, pre = reddit(driver, n)

    elif "facebook" in url:
        pass
        #imgs, directory, pre = facebook(driver, n)

    elif "twitter" in url:
        imgs, directory, pre = twitter(driver , n)

        


    if path.exists('src\\src.txt'):
        

        with open('src\\src.txt', 'r') as r:
            content = r.readlines()

        with open('src\\src.txt', 'a') as f:

            for img in imgs:
                num = randint(100000, 999999)
                
                img = img['src']

                if img+'\n' in content:
                    print(Fore.YELLOW + f"Imagem encontrada já baixada anteriormente, ignorando (link da imagem: "+ Fore.MAGENTA + f"{img}")
                else:
                    
                    urllib.request.urlretrieve(img, directory + pre + "Imagem "+ str(num) + ".png")
                    f.write(f"{img}\n")
    else:

        with open('src\\src.txt', 'w') as f:
            for img in imgs:
                num = randint(100000, 999999)
                img = img['src']
                urllib.request.urlretrieve(img, directory + pre + "Imagem " + str(num)+ ".png")
                f.write(f"{img}\n")

    print()
    print(Fore.RED + 'Finalizado...')
    time.sleep(1)


    #encerrando o script
    driver.quit()