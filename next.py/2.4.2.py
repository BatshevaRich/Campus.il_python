class BigThing:

    def __init__(self, param):
        self._param = param

    def size(self):
        if isinstance(self._param, int):
            return self._param

        if isinstance(self._param, str):
            return len(self._param)

class BigCat(BigThing):

    def __init__(self, name, param):
        super().__init__(param)
        self._name = name

    def size(self):
        if super().size() > 20:
            return 'Very Fat'
        if super().size() > 15:
            return 'Fat'
        return 'OK'

my_thing = BigThing("balloon")
print(my_thing.size())

cutie = BigCat("mitzy", 22)
print(cutie.size())