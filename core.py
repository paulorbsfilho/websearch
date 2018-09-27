from bs4 import BeautifulSoup
import requests
import re

def main():
    keyword = "google"#input("Digite sua busca:\n")
    url = "https://www.google.com/" #input("Digite a url de inicio:\n")
    depth = "3"#input("digite a profundidade\n")
    search(keyword, url, depth)

def search(keyword, url, depth):
    response = requests.get(url)
    print(response.status_code)
    html = BeautifulSoup(response.text, 'html5lib')
    links = html.find_all("a")
    for link in links:
        print(link['href'])

if __name__ == '__main__':
    main()
