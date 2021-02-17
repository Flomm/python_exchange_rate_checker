from .rate_finder import Rate_finder
import urllib.request

class Otp_rate_finder(Rate_finder):

    def __init__(self, eur_rate, chn_rate, otp_url):
        self.eur_rate = 0
        self.chf_rate = 0
        self.otp_url = 'https://www.otpbank.hu/portal/hu/Arfolyamok/OTP'
