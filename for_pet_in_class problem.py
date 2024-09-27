class Pet:
    _registry = []
    def __init__(self, animal_type, sound):
        self.animal_type = animal_type
        self._registry.append(self)
        self.sound = sound
    def make_noise(self):
        print(self.sound)


class Game:
    def __init__(self):
        animal1 = Pet('dog','woof')
        animal2 = Pet('cat','meow')

    def chorus(self):
        for animal in Pet._registry:
            print(animal.animal_type)
            animal.make_noise()

if __name__ == '__main__':
    game = Game()
    game.chorus()