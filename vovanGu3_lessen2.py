import abc


class Animals(abc.ABC):
    def __init__(self, name, age:int ):
        self._name = name
        self._age = age

    @abc.abstractmethod
    def pick_up(self):
        pass

    @property
    def age(self):
        return self._age


class Beasts(Animals):

    def __init__(self, name , age, colour_coat, presence_toy):
        super().__init__(name, age)
        self.__colour_coat = colour_coat
        self._presence_toy = presence_toy

    __shelter_number: int = 2

    def get_shelter_number(self) -> int:
        return self.__shelter_number

    def pick_up(self):
        if self._age > 2:
            print('Have you sheltered a pet: ' + self._name)
        else:
            print(self._name + 'is too small')

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> str:
        return str(self._age)

    def get_presence_toy(self) -> bool:
        return self._presence_toy


class Dog(Beasts):

    def __init__(self, name: str, age: int, colour_coat: str, presence_toy: bool):
        super().__init__(name, age, colour_coat, presence_toy)

    def pick_up(self):
        if self._age > 3:
            if self.get_presence_toy():
                print('Have you sheltered a dog : ' + self._name)
            else:
                print(self._name + ' without a toy')
        else:
            print(self._name + ' is too small.He is only ' + self.get_age() + ' years old')

    @staticmethod
    def submit_vote():
        print("Woof!")

    def get_name(self):
        return super().get_name()

    def set_name(self, name: str) -> None:
        self._name = name

    def get_age(self):
        return super().get_age()

    def set_age(self, age: int) -> None:
        self._age = age

    def get_presence_toy(self):
        return super().get_presence_toy()

    name = property(get_name,set_name)
    age = property(get_age,set_age)


class Cat(Beasts):

    def __init__(self, name: str, age: int, colour_coat: str, presence_toy: bool):
        super().__init__(name, age, colour_coat, presence_toy)

    def pick_up(self):
        if self._age > 1:
            if self.get_presence_toy():
                print('Have you sheltered a cat : ' + self._name)
            else:
                print(self._name + ' without a toy')
        else:
            print(self._name + ' is too small.He is only ' + self.get_age() + ' years old')

    @staticmethod
    def submit_vote():
        print("Meow!")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @property
    def presence_toy(self) -> bool:
        return self._presence_toy()


dog1 = Dog('Sharik', 5, 'red', False)

dog1.pick_up()
print(dog1.get_age())
dog1.submit_vote()
dog1.age = 6
print(dog1.age)

cat1 = Cat('Boris', 4, 'white', True)

print(cat1.name)
cat1.age = 6
print(cat1.age)

cat1.pick_up()

print(cat1.get_shelter_number())
print(dog1.get_shelter_number())
