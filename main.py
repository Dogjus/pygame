class Warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina

    def __call__(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('---------------')

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('---------------')

    def __add__(self, target):
        if isinstance(target, int):
            self.health += target
            print(f'Здоровье у {self.__class__.__name__} повышено до {self.health}')
        elif isinstance(target, list):
            target.append(self)
            print(f"{self.__class__.__name__} присоединяется к армии")
        elif isinstance(target, (Warrior, Mage)):
            print('---------------')
            print(f'{self.__class__.__name__} накладывает повязку из',
                  f'целебных трав {target.__class__.__name__}')
            self.stamina -= 20
            target.health += 10
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
                  f'\nУ {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
            print('---------------')

    def __sub__(self, target):
        if isinstance(target, int):
            self.health -= target
            print(f'Здоровье у {self.__class__.__name__} понижено до {self.health}')
        elif isinstance(target, list):
            target.remove(self)
            print(f"{self.__class__.__name__} присоединяется к армии")
        elif isinstance(target, (Warrior, Mage)):
            print('---------------')
            print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
            target.health -= 3
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
            print('---------------')

    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')


class Mage:
    def __init__(self, health=60, mana=120):
        self.health = health
        self.mana = mana

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nMana: {self.mana}')
        print('---------------')

    def __add__(self, target):
        if isinstance(target, int):
            self.health += target
            print(f'Здоровье у {self.__class__.__name__} повышено до {self.health}')
        elif isinstance(target, list):
            target.append(self)
            print(f"{self.__class__.__name__} присоединяется к армии")
        elif isinstance(target, (Warrior, Mage)):
            print('---------------')
            print(f'{self.__class__.__name__} накладывает повязку из',
                  f'целебных трав {target.__class__.__name__}')
            self.stamina -= 20
            target.health += 10
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
                  f'\nУ {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
            print('---------------')

    def __sub__(self, target):
        if isinstance(target, int):
            self.health -= target
            print(f'Здоровье у {self.__class__.__name__} понижено до {self.health}')
        elif isinstance(target, list):
            target.remove(self)
            print(f"{self.__class__.__name__} выбывает из армии")
        elif isinstance(target, (Warrior, Mage)):
            print('---------------')
            print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
            target.health -= 3
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
            print('---------------')

    def attacks(self, target):
        print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')


unit1 = Warrior()
unit2 = Mage()
squad = []
unit1 + unit2
unit2 + squad
unit1 + 5
unit2 + 10
unit1 - unit2
unit2 - squad
unit1 - 5
unit2 - 10
