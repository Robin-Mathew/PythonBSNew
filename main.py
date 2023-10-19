from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    cards = soup.find_all('div',class_ = 'card')
    for card in cards:
        cardname = card.h5.text
        cardprice = card.a.text.split()[-1]

        print(f'{cardname} costs {cardprice}')