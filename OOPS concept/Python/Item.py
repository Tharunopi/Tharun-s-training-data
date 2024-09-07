import pandas as pd
from typing import List

class item:
    pay_rate = 0.8
    history = []
    
    def __init__(self, phone: str, price: int, quant: int):
     
        assert price >= 1, "price should be greater than 0"
        assert quant >= 1, "price should be greater than 0"
        
        self.__phone = phone
        self.__price = price
        self.__quant = quant

        item.history.append(self)

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def reset_phone(self, x):
        assert len(x) < 10, "value is too large"
        self.__phone = x

    @property
    def price(self):
        return self.__price

    @price.setter
    def reset_price(self, x):
        assert x >= 1, "value is too small"
        self.__price = x
    
    @property
    def quantity(self):
        return self.__quant

    @quantity.setter 
    def reset_quantity(self, x):
        assert x >= 1, "value is too small"
        self.__quant = x
        
    def total_price(self):
        return self.__price * self.__quant

    def apply_discount(self):
        self.__price = self.__price * self.__pay_rate

    def apply_increment(self, x):
        self.__price += self.__price * x

    @classmethod
    def csv_reader(cls):
        df = pd.read_csv("items.csv").values
        for i in df:
            item(
                phone=i[0],
                price=i[1],
                quant=i[2]
            )

    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return False
        else:
            return True

    def __repr__(self):
        # return "item"
        return f"{self.__class__.__name__}('{self.__phone}', {self.__price}, {self.__quant})"

    
