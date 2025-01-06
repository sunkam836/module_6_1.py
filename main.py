class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f'{self.name}, съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False

class Mammal(Animal):
    pass
class Predator(Animal):
    pass


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.dible = True

a1 = Predator('Wolf')
a2 = Mammal('Dog')
p1 = Flower('Flower')
p2 = Fruit('Orange')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
#
#

#class Animal():
#    alive = True
#    fed = False

#    def __init__(self, name):
#        self.name = name

#    def eat(self, food):
#        if food.edible:
#            print(f'{self.name}, съел {food.name}')
#            self.fed = True
#        else:
#            print(f'{self.name}, не стал есть {food.name}')
#            self.alive = False


#class Plant():
#    edible = False

#    def __init__(self, name):
#        self.name = name


#class Mammal(Animal):
#    pass


#class Predator(Animal):
#    pass


#class Flower(Plant):
#    pass


#class Fruit(Plant):
#    edible = True

#    def __init__(self, name):
#        super().__init__(name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

