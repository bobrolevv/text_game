from random import randint

class Tank(object):

    def __init__(self, model: str, armor: int, min_damage: int,
                 max_damage: int, health: int):
        self.model = model                              # модель, строка
        self.armor = armor                              # броня, целое число
        self.damage = randint(min_damage, max_damage)   # урон, целое число случайное
        self.health = health                            # здоровье, целое число

    def print_info(self):
        print(f'{self.model} '
              f'имеет лобовую броню {self.armor} мм. '
              f'при {self.health} ед. здоровья '
              f'и урон в {self.damage} единиц.')

    def shot(self, enemy):

        def health_down():
            demage = self.damage
            enemy.health = enemy.health - (demage / enemy.armor)
            print(f'{enemy.model}: Командир, по экипажу {enemy.model} попали, '
                  f'у нас осталось {enemy.health} очков здоровья')

        health_down()

        if enemy.health <= 0:
            print(f'Экипаж танка {enemy.model} уничтожен')
        else:
            print(f'{self.model} Точно в цель, у противника '
                  f'{enemy.model} осталось {enemy.health} единиц здоровья')


t1 = Tank('ПЕРВЫЙ',10,1,100,50)
t2 = Tank('ВТОРОЙ',10,1,100,50)

print('==начало игры==')
t1.print_info()
t2.print_info()
print()

print(f'==выстрел {t1.model}==')
t1.shot(t2)
print()

print(f'==выстрел {t2.model}==')
t2.shot(t2)
print()