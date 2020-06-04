class Animal:
    count_animals = 0
    def __init__(self, name = 'Octavio', age = 0):
        self._name = name
        self._age = age 

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age
    
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

def main():
    deer = Animal('deer', 2)
    Animal.count_animals +=1
    octopus = Animal()
    Animal.count_animals += 1
    print(deer.get_name())
    print(octopus.get_name())
    deer.set_name('stag')
    print(Animal.count_animals)
    # print('{}, {}'.format(deer.age, dolphin.age))

main()