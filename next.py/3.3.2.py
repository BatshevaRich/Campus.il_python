class UnderAgeException(Exception):

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Provided age %s is less than 18. In %d years you can join the party!" % (self._arg, 18 - self._arg)

    def get_arg(self):
        return self._arg

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAgeException(age)
    except UnderAgeException as e:
        print(e)
    else:
        print("You should send an invite to " + name)

send_invitation('hello', 20)