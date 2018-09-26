from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# class Crawler:
#
#     def Search(self,keyword, url, depth):



if __name__ == '__main__':
    html = urlopen("https://www.google.com/")
    res = BeautifulSoup(html.read(), "html5lib");
    print(res.title)

    response = requests.get('http://www.google.com/')
    print(response.status_code)
