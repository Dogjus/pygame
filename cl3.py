class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def hello(self):
        print(f'Hello my name is {self.name}, I am {self.age} years old. Nice to meet you')

    def bye(self):
        print("Goodbye see you next time!")

    def sleep(self):
        print("Good night!")

    def woke_up(self):
        print("Good morning!")

    def walk(self):
        print("I took a step")


hum = Human(10, "Bob")
hum.sleep()
hum.woke_up()
hum.walk()
hum.hello()
hum.bye()

