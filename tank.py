from random import randint

class Tank(object):

    def __init__(self, model:str, armor:int, min_damage:int,
                 max_damage:int, health:int):
        self.model = model                              # модель, строка
        self.armor = armor                              # броня, целое число
        self.damage = randint(min_damage, max_damage)   # урон, целое число случайное
        self.health = health                            # здоровье, целое число

    def print_info(self):
        print(f'{self.model} '
              f'имеет лобовую броню {self.armor} мм. '
              f'при {self.health} ед. здоровья '
              f'и урон в {self.damage} единиц.')

    def show(self):
        pass

    def health_down(self):
        pass

t = Tank('ПЕРВЫЙ',10,1,100,50)
t.print_info()