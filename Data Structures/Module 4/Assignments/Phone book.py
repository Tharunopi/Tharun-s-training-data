import time
from turtledemo.penrose import start


class PhoneBook:
    history = []
    def __init__(self, user_name):
        self.username = user_name
        self.data = []

    def add_number_name(self, name, number):
        if self.data:
            for i in self.data:
                if i[1] == number:
                    i[0] = name
                    return print("Done"), self.history.append([f"{self.username} added {name}"])
        return self.data.append([name, number]), self.history.append([f"{self.username} added {name}"])

    def delete_number(self, name):
        if self.data:
            for i in self.data:
                if i[0] == name:
                    i[1] = None
                    return print("Deleted"), self.history.append([f"{self.username} deleted a person"])

    def find(self, number):
        if self.data:
            for i in self.data:
                if i[1] == number:
                    return print(i[0])
        return print("Match not found")

start = time.time()
pb = PhoneBook("Tharun")
pb.add_number_name("police", 911)
pb.add_number_name("mom", 9864)
pb.add_number_name("bob", "6543")
pb.find(76213)
pb.find(910)
pb.find(911)
pb.delete_number("hiuser")
pb.delete_number("police")
pb.find(911)
pb.find(9864)
pb.add_number_name("daddy", 5415)
pb.find(5415)

end = time.time()
print(end - start)
