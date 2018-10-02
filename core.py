from bs4 import BeautifulSoup
import requests, time


def main():
    keyword = u"Inscrição"  # input("Digite sua busca:\n")
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
    text = html.text
    t = text.split()
    s = 0
    try:
        s = t.index(keyword)
        print(s)
    except ValueError:
        print(u"\nPalavra ou expressão nao encontrada dentro da página.\n")
        print(url)
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
    res = " ".join(v)
    if depth > 0:
        for link in links:
            try:
                if link['href'].startswith('http'):
                    search(keyword, link['href'], depth -1)
            except KeyError:
                print(u"Link inválido: " + str(link))

    print(u"\nSua busca retornou: " + keyword + ". " + res + "\nLink: " + url)



if __name__ == '__main__':
    main()