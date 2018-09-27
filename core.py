from bs4 import BeautifulSoup
import requests, re, time


def main():
    keyword = "Federal"  # input("Digite sua busca:\n")
    url = "http://libra.ifpi.edu.br/"  # input("Digite a url de inicio:\n")
    depth = 3  # input("digite a profundidade\n")
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
    tam = len(t)
    v = []
    cp = 2

    while cp != 0:
        v.append(t[s - cp])
        cp -= 1

    c = 0
    while c < 3:
        if s + c < tam:
            v.append(t[s + c])
            c += 1
        else:
            break
    end = time.time()

    res = " ".join(v)
    print(u"\nSua busca retornou: " + keyword + ". "+ res + "\nLink: " + url)
    print(u"Tempo de execução:", end - start)


if __name__ == '__main__':
    main()
