from abc import ABC, abstractmethod


class Rate_finder(ABC):

    def get_foreign_rate(self):
        pass

    def get_otp_rate(self):
        pass
