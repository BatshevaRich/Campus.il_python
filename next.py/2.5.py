class Animal:

    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger

    def feed(self):
        self._hunger -= 1

    def talk(self, message):
        print(message)


class Dog(Animal):

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger=hunger)

    def __str__(self):
        return 'Dog {}'.format(
            self._name)

    def talk(self):
        super().talk('woof woof')

    def fetch_stick(self):
        print('There you go, sir!')


class Cat(Animal):

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger=hunger)

    def __str__(self):
        return 'Cat {}'.format(
            self._name)

    def talk(self):
        super().talk('meow')

    def chase_laser(self):
        print('Meeeeow')


class Skunk(Animal):

    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger=hunger)
        self._stink_count = stink_count

    def __str__(self):
        return 'Skunk {}'.format(
            self._name)

    def talk(self):
        super().talk('tsssss')

    def stink(self):
        print('Dear lord!')


class Dragon(Animal):

    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger=hunger)
        self._color = color

    def __str__(self):
        return 'Dragon {}'.format(
            self._name)

    def talk(self):
        super().talk('Raaaawr')

    def breath_fire(self):
        print('$@#$#@$	')


class Unicorn(Animal):

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger=hunger)

    def __str__(self):
        return 'Unicorn {}'.format(
            self._name)

    def talk(self):
        super().talk('Good day, darling')

    def sing(self):
        print('I’m not your toy...')


def main():
    zoo_list = []
    zoo_list.append(Dog('Brownie', 10))
    zoo_list.append(Cat('Zelda', 3))
    zoo_list.append(Skunk('Stinky'))
    zoo_list.append(Unicorn('Keith', 7))
    zoo_list.append(Dragon('Lizzy', 1450))
    zoo_list.append(Dog('Doggo', 80))
    zoo_list.append(Cat('Kitty', 80))
    zoo_list.append(Skunk('Stinky Jr.', 80))
    zoo_list.append(Unicorn('Claire', 80))
    zoo_list.append(Dragon('McFly', 80))

    for animal in zoo_list:
        if animal.is_hungry():
            print(animal)
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    print('Zoo Name: {}'.format(Animal.zoo_name))


if __name__ == "__main__":
    main()
