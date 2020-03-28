from colorama import init,Fore,Back,Style

from src.iniciar_driver import *

from src.baixar import baixar

def main():

    while True:
        print(Fore.RESET)
        url = input("Cole o link que deseja procurar por imagens: ")
        if "facebook" in url:
            print("facebook ainda não implementado")
            continue
        elif url == '':
            print('Encerrando tarefa')
            break

        else:
            print()
            driver = iniciar(url)

            baixar(driver, url)


if __name__ == "__main__":
    main()  