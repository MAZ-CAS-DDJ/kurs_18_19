import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

def kommentarezaehlen(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'xml')
    storybox = soup.find_all('div', {'class':'text'})

    lst = []
    for elem in storybox:
        try:
            t = elem.find('h2').text
        except:
            t = 'Kein Titel'
        try:
            k = elem.find('a', {'class':'standard comments'}).text.replace("\n", "")
        except:
            k = 'Keine Kommentare'
        mini_dict = {'Titel': t,
                 'Kommentar': k}
        lst.append(mini_dict)

    return print(pd.DataFrame(lst))

if __name__== "__main__":
    kommentarezaehlen(sys.argv[1])
