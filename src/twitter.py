from os import path
from bs4 import BeautifulSoup
import subprocess

def twitter(driver,n):


    _path = 'imagens\\twitter'

    if not path.exists(_path):
        subprocess.run(['mkdir', _path], shell =True)

    for i in range(int(n)):

        #pegando o source da pagina
        page = driver.page_source
        driver.execute_script("window.scrollBy(0,720)")
        #usando lxml de parser, criando a sopa
        soup = BeautifulSoup(page, 'lxml')

        # grab todas as imagens de post
        imgs = soup.find_all("img", attrs={"alt":"Imagem"})

    return (imgs, path)