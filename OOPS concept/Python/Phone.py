from Item import item

class phone(item):

    def __init__(self, phone: str, price: int, quant: int, broken:int=0):

        super.__init__(
            phone, price, quant    
        )
        
        assert broken >= 0, "price should be greater than 0"
        
        self.broken = broken