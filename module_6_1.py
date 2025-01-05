class Animal:  # класс животное родительский
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):  # индивидуальное название каждого животного.
        self.name = name

    def eat(self, food):
        if food.edible:  # если еда съдобная
            print(f"{self.name} съел {food.name}")  # выводит на экран "<self.name> съел <food.name>
            self.fed = True  # меняется на атрибут fed на True
        else:
            print(f"{self.name} не стал есть {food.name}")  # выводит на экран "<self.name> не стал есть <food.name>"
        self.alive = False  # меняется атрибут alive на False


class Plant:  # класс растения родительский
    edible = False  # съедобность

    def __init__(self, name):
        self.name = name
    # индивидуальное название каждого растения


class Mammal(Animal):  # дочерний класс млекопитающие для Animal
     pass

class Predator(Animal):  # дочерний класс хищник для Animal
     pass

class Flower(Plant):  # дочерний класс цветы для Plant
     pass

class Fruit(Plant):  # дочерний класс фрукты для Plant
        edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
