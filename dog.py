from animal import Animal


class Dog(Animal):
    def __init__(self, name, age, weight, bread):
        super().__init__(name, age, weight)
        self.breed = breed

    def is_barking(self):
        print(f'{self.name} id barking')