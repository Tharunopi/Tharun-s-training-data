from Item import item 
from Phone import phone

item1 = item("mi", 20000, 4)

item1.apply_increment(0.2)

print(item1.price)