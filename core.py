from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

def main():
    keyword = "google"#input("Digite sua busca:\n")
    url = "https://www.google.com/" #input("Digite a url de inicio:\n")
    depth = "1"#input("digite a profundidade\n")
    search(keyword, url, depth)

def search(keyword, url, depth):
    print()
    a = url[-6]
    response = requests.get(url)
    reg = re.compile(r'href="(.*?)"')
    links = []
    for l in response.text.split():
        links += reg.findall(l)
    print(links)
# html = urlopen("https://www.google.com/")
# res = BeautifulSoup(html.read(), "html5lib");
# print(res.title)
#
# response = requests.get('http://www.google.com/')
# print(response.status_code)

if __name__ == '__main__':
    main()
