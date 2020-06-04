class Animal():
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

def main():
    deer = Animal('deer', 2)
    dolphin = Animal('dolphine', 3)
    deer.birthday()
    print('{}, {}'.format(deer.age, dolphin.age))

main()