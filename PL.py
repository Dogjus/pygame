import random


class Player:
    def __init__(self, name, colour=0, roll=0):
        self.__roll = roll
        self.name = name
        self.__colour = colour

    @property
    def color(self):
        if len(lst) != 0:
            print("chose color", lst)

            a = input("выберите цвет: ")
            if a == "red":
                self.__colour = a
                lst.remove("red")
                return self.__colour
            elif a == "blue":
                self.__colour = a
                lst.remove("blue")
                return self.__colour
            elif a == "green":
                self.__colour = a
                lst.remove("green")
                return self.__colour
            else:
                return "error color"
        else:
            return "все места заняты"

    @property
    def roll(self):
        if len(lst2) != 0:
            d = random.choice(lst2)
            self.__roll = d
            lst2.remove(d)
            if self.__roll == "impostor":
                return self.name + " is impostor"
            else:
                return self.name + " is not impostor"
        else:
            return " no mest"



lst = ["red", "blue", "green"]
lst2 = ["impostor", "human", "human"]
a = Player("nineraninne568")
print(a.color)
print(a.roll)

a = Player("nninne568")
print(a.color)
print(a.roll)

a = Player("neranne568")
print(a.color)
print(a.roll)

a = Player("nieanine58")
print(a.color)
print(a.roll)






