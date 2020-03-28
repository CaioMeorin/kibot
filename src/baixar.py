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
    content = ''

    if path.exists('src\\src.txt'):
        with open('src\\src.txt', 'r') as f:
            content = f.readlines()
    
    
    if not path.exists(directory):
        subprocess.run(['mkdir', directory], shell =True)

    while True:
        #pegando o source da pagina
        page = driver.page_source

        soup = BeautifulSoup(page, 'lxml')
        imgs = soup.find_all("img", attrs={"alt":"Imagem"})
        # grab todas as imagens de post

        if len(imgs) < n:
            
            driver.execute_script("window.scrollBy(0,1080)")
            continue

        else:
            if content:
                for img in imgs:
                    if img['src']+'\n' in content:
                        print(Fore.RED+"Imagem ja baixada detectada, tentando evita-la")
                        imgs.remove(img)
                
                    if "small" in img['src']:
                        imgs.remove(img)
            
            imgs = imgs[0:n]
            
        if len(imgs) == n:
            break


    return (imgs, directory, pre)

def reddit(driver, n):


    directory = 'imagens\\reddit\\'
    pre = 'Reddit '
    content = ''

    if path.exists('src\\src.txt'):
        with open('src\\src.txt', 'r') as f:
            content = f.readlines()
    
  
    if not path.exists(directory):
        subprocess.run(['mkdir', directory], shell =True)

    while True:
        #pegando o source da pagina
        page = driver.page_source
        #usando lxml de parser, criando a sopa
        soup = BeautifulSoup(page, 'lxml')

        # grab todas as imagens de post
        imgs = soup.find_all("img", attrs={"alt":"Post image"})

        if len(imgs) < n:
            
            driver.execute_script("window.scrollBy(0,1080")
            continue

        else:
            if content:
                for img in imgs:
                    if img['src']+'\n' in content:
                        print(Fore.RED+"Imagem ja baixada detectada, tentando evita-la")
                        imgs.remove(img)
                
                    if "small" in img['src']:
                        imgs.remove(img)
            
            imgs = imgs[0:n]
            
        if len(imgs) == n:
            break


    return (imgs, directory, pre)

def facebook(driver, n):


    directory = 'imagens\\facebook\\'
    pre = 'facebook '
    content = ''

    if path.exists('src\\src.txt'):
        with open('src\\src.txt', 'r') as f:
            content = f.readlines()

    if not path.exists(directory):
        subprocess.run(['mkdir', directory], shell =True)
    
    while True:
        #pegando o source da pagina
        page = driver.page_source
        driver.execute_script("window.scrollBy(0,720)")
        #usando lxml de parser, criando a sopa
        soup = BeautifulSoup(page, 'lxml')

        # grab todas as imagens de post
        imgs = soup.find_all("img", {"class":"img"})

        if len(imgs) >= n:
            if content:
                for img in imgs:
                    if img['src']+'\n' in content:
                        print(Fore.RED+"Imagem ja baixada detectada, tentando evita-la")
                        imgs.remove(img)
                
            imgs = imgs[0:n]
            
            if len(imgs) == n:
                break
            else:
                continue

    return (imgs, directory, pre)

def baixar(driver, url):


    if not path.exists("imagens"):
        subprocess.run(['mkdir', 'imagens'], shell =True)

    n = int(input("Quantas imagens deseja baixar? "))
    if n in range(1,11):
        print(Fore.CYAN + 'Baixando imagens\n')


        if "reddit" in url:
            imgs, directory, pre = reddit(driver, n)

        elif "facebook" in url:
            pass
            #imgs, directory, pre = facebook(driver, n)

        elif "twitter" in url:
            imgs, directory, pre = twitter(driver , n)

            


        if path.exists('src\\src.txt'):
            

            with open('src\\src.txt', 'a') as f:

                for img in imgs:
                    num = randint(100000, 999999)
                    
                    img = img['src']
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
        time.sleep(3)


        #encerrando o script

        driver.quit()
    else:
        print('Número invalido, escolha entre 1-10')
        driver.quit()