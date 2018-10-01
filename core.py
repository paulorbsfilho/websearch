from bs4 import BeautifulSoup
import requests, re, time

def main():
    keyword = "Federal"#input("Digite sua busca:\n")
    url = "http://www.globoesporte.com/" #input("Digite a url de inicio:\n")
    depth = 3#input("digite a profundidade\n")
    search(keyword, url, depth)


def search(keyword, url, depth):
    start = time.time()
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html5lib')
    links = html.find_all("a")
    for l in links:
        print(l.get('href'))
    searchInPage(keyword,html)
    end = time.time()
    print(u"Tempo de execução:", end - start)


def searchInPage(keyword,html):
    pass


if __name__ == '__main__':
    main()