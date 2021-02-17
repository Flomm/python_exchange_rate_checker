from .rate_finder import Rate_finder
import urllib.request


class Foreign_rate_finder(Rate_finder):

    def __init__(self, eur_rate, chf_rate, eur_url, chf_url):
        self.eur_rate = 0
        self.chf_rate = 0
        self.eur_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=HUF'
        self.chf_url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=CHF&To=HUF'

    def find_eur_rate(self):
        page_content = str(urllib.request.urlopen(self.eur_url).read())
        eur_index = page_content.find('"EUR_HUF"')
        self.eur_rate = page_content[eur_index + 131:eur_index+137]

    def find_chf_rate(self):
        page_content = str(urllib.request.urlopen(self.eur_url).read())
        eur_index = page_content.find('"EUR_HUF"')
        self.eur_rate = page_content[eur_index + 131:eur_index+137]
