import requests
from bs4 import BeautifulSoup


url = "http://csgolounge.com/"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text)

names = soup.find_all("div", {"class": "teamtext"})

for name in names:
    b = name.findNext("b")
    i = name.findNext("i")
    bTitle = b.string
    iTitle = i.string
    print(bTitle)
    print(iTitle)