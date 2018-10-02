from bs4 import BeautifulSoup
import requests, time


def main():
    keyword = u"O Sol"  # input("Digite sua busca:\n")
    url = "http://cifraclub.com.br/"  # input("Digite a url de inicio:\n")
    depth = 3  # input("digite a profundidade\n")
    search(keyword, url, depth)


def search(keyword, url, depth):
    start = time.time()
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html5lib')
    nomes = html.find_all("strong", class_="top-txt_primary")
    lista_mais_acessadas = []
    casos = 0
    res = ""
    for n in nomes:
        lista_mais_acessadas += n
    for i in lista_mais_acessadas:
        if keyword in lista_mais_acessadas:
            casos = casos + 1
    end = time.time()
    if casos < 1:
        res = u"não está entre as mais acessadas em:"
    else:
        res = u"está entre as mais acessadas em:"
    print(u"\nSua busca retornou: " + "\"" + keyword + "\" " + res + "\n" + url)
    print(u"Tempo de execução:", end - start)


if __name__ == '__main__':
    main()
