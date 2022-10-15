class Creditcard:
    def __init__(self, number, password, name, cash):
        self.__number = number
        self.name = name
        self.__cash = cash
        self.__password = password

    @property
    def info(self):
        if input("input your name: ") == self.name and int(input("input your password: ")) == self.__password:
            print(f"number: {self.__number}, cash: {self.__cash}")
        else:
            print("error password ###########"+self.__number[-4:])
    @property
    def cash(self):
        return self.__cash
    @cash.setter
    def cash(self,target):
        self.__cash = target

    def operation(self, word, mon):
        if str(word) == "Снять":
            self.cash -= mon
        elif str(word) == "Внести":
            self.cash += mon


card = Creditcard("1234567891023569", 7458921, "Gleb", 1000000000)
card.info
card.operation("Снять", 1)
card.info
