import bs4, requests

def getAmazonPrice(productUrl):

    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#buyNewSection > div > div > span > span')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.it/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1X7N5O7CF397I&keywords=automating+boring+stuff+with+python&qid=1563438086&s=gateway&sprefix=automating+%2Caps%2C166&sr=8-1')
print('The price is '+ price)
