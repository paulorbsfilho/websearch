from bs4 import BeautifulSoup
import requests, time, re


def main():
    keyword = u"Federal"  # input("Digite sua busca:\n")
    url = "http://libra.ifpi.edu.br/"  # input("Digite a url de inicio:\n")
    depth = 2  # input("digite a profundidade\n")
    start = time.time()
    search(keyword, url, depth)
    end = time.time()
    print(u"Tempo de execução:", end - start)


def search(keyword, url, depth):

    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html5lib')
    links = html.find_all("a")
    words = html.find_all("p")
    palavras_da_pagina = []
    res = []
    try:
        for w in words:
            palavras_da_pagina += w
        for w2 in palavras_da_pagina:
            if keyword == words.index(w2):
                res = " foi encontrada"
    except:
        res = "nao foi encontrada"
    print(u"\nSua busca retornou: " + keyword + ". " + res + "\nLink: " + url)
    if depth > 0:
        for link in links:
            try:
                if link['href'].startswith('http'):
                    time.sleep(2)
                    search(keyword, link['href'], depth -1)
            except KeyError:
                print(u"Link inválido: " + str(link))



if __name__ == '__main__':
    main()