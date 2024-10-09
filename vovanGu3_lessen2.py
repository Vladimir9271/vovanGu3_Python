import abc

class Animals(abc.ABC):
    def __init__(self, name, age ):
        self._name = name
        self._age = age

    @abc.abstractmethod
    def pick_up(self):pass

    @property
    def age(self):
        return self._age


class Beasts(Animals):
    def __init__(self, name , age, colour_coat, presence_toy):
        super().__init__(name, age)
        self.__colour_coat = colour_coat
        self._presence_toy = presence_toy

    def pick_up(self):
        if self._age > 2:
            print('Have you sheltered a pet: ' + self._name)
        else:
            print(self._name + ' is too small')

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def get_presence_toy(self) -> bool:
        return self._presence_toy

class Dog(Beasts):
    def __init__(self, name: str, age: int, colour_coat: str, presence_toy: bool):
        super().__init__(name, age, colour_coat, presence_toy)

    @staticmethod
    def submit_vote():
        print("Woof!")

    def get_name(self):
        return super().get_name()

    def get_age(self):
        return super().get_age()

    def get_presence_toy(self):
        return super().get_presence_toy()

dog1 = Dog('Sharik',6, 'red' , True)
dog1.pick_up()

print(dog1.get_age())
dog1.submit_vote()
