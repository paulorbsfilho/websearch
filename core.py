from bs4 import BeautifulSoup
import requests, re, time

def main():
    keyword = "alunos"#input("Digite sua busca:\n")
    url = "http://libra.ifpi.edu.br/" #input("Digite a url de inicio:\n")
    depth = "3"#input("digite a profundidade\n")
    search(keyword, url, depth)

def search(keyword, url, depth):
    start = time.time()
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html5lib')
    links = html.find_all("a")
    for link in links:
        try:
            print(link['href'])
        except KeyError:
            print(link)
    text = html.text
    t = text.split()
    try:
        s = t.index(keyword)
        print(s)
    except ValueError:
        print(u"\nPalavra ou expressão nao encontrada dentro da página.")
    end = time.time()
    print(u"Tempo de execução:", end - start)

if __name__ == '__main__':
    main()
