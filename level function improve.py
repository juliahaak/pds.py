# most recent improvement of code - significant change was the combining of all the levels into 1 function

# justification for how its a "educational resource" for GCSE students.

# in a level further maths in the decision module we covered graph theory and i remember it feeling very abstract and unapplicable
# to real life. for GCSE students who are going to go on to take a level further maths
# this introduces some concepts early on related to graph theory in a real world practical way

# maths teachers can explain that when students play the game they are essentially working out the shortest path between "nodes"
# of the graph not too differently from the travelling salesman problem which they will cover in more depth at A-level further maths

# after having played the games an exercise they could attempt to draw the different levels in terms of graphs
# eg count the number of blocks between
# the respective nodes to calculate the weight of the edges

import pygame
from pygame.locals import *

class Pet:

    _registry = []
    def __init__(self, parent_screen, animal_type, start_x, start_y, house_start_x, house_start_y):
        self._registry.append(self)
        self.x = 40 * start_x
        self.y = 40 * start_y
        self.house_x = house_start_x
        self.house_y = house_start_y
        self.parent_screen = parent_screen
        self.animal_type = animal_type
        self.pet = pygame.image.load(f'resources/pets/{self.animal_type}.jpg')
        self.parent_screen.blit(self.pet, (self.x, self.y))
        self.pethouse = Pethouse(self.parent_screen, self.animal_type, self.house_x, self.house_y)
        self.show_pet = True
        self.pet_picked_up = False

    def draw_pet(self):
        self.parent_screen.blit(self.pet, (self.x, self.y))

    def pick_up_pet(self, pet_positions):
        self.pet_positions = pet_positions
        if self.pet_positions[0] == False or self.pet_positions[1] == False or self.pet_positions[2] == False or \
                self.pet_positions[3] == False:
            self.pet_picked_up = True
            if self.pet_positions[0] == False:
                self.x = 16 * 40 + 10
                self.y = 40 * 5
                self.pet_bag_position = 1
                self.pet_positions[0] = True
            elif self.pet_positions[1] == False:
                self.x = 18 * 40 - 10
                self.y = 40 * 5
                self.pet_positions[1] = True
                self.pet_bag_position = 2
            elif self.pet_positions[2] == False:
                self.x = 16 * 40 + 10
                self.y = 40 * 5 - 50
                self.pet_positions[2] = True
                self.pet_bag_position = 3
            elif self.pet_positions[3] == False:
                self.x = 18 * 40 - 10
                self.y = 40 * 5 - 50
                self.pet_positions[3] = True
                self.pet_bag_position = 4
    def get_pp(self):
        return self.pet_positions




class Pethouse:
    def __init__(self, parent_screen, animal_type, start_x, start_y):
        self.x = 40 * start_x
        self.y = 40 * start_y
        self.parent_screen = parent_screen
        self.animal_type = animal_type
        self.pethouse = pygame.image.load(f'resources/pethouses/new {self.animal_type} house.jpg')

    def draw_pethouse(self):
        self.parent_screen.blit(self.pethouse, (self.x, self.y))


class Map:
    def __init__(self, map_size, parent_screen, map_list):
        self.map_size = map_size
        self.parent_screen = parent_screen
        self.blue_block = pygame.image.load('resources/blue block.jpg')
        self.yellow_block = pygame.image.load('resources/block.jpg')
        self.bag = pygame.image.load('resources/new bag.jpg')
        self.map_list = map_list

    def draw_map_block(self, x, y):
        self.parent_screen.blit(self.yellow_block, (y, x))

    def draw_map(self):
        self.parent_screen.fill((200, 255, 255))
        for x in range(self.map_size):
            for y in range(self.map_size):
                self.parent_screen.blit(self.blue_block, (40 * x + 80, 40 * y + 80))

        for list in self.map_list:
            self.draw_map_block(40 * list[1], 40 * list[0])

        self.parent_screen.blit(self.bag, (40 * 15, 40 * 1.5))

    def get_list(self):
        return self.map_list


class Player:
    def __init__(self, parent_screen, start_x, start_y, map_list):
        self.x = 40 * start_x
        self.y = 40 * start_y
        self.parent_screen = parent_screen
        self.fuel_count = 0
        self.map_list = map_list
        self.can_move = True
        self.orientation = 'up'

    def draw_player(self):
        self.parent_screen.blit(pygame.image.load(f'resources/cars/{self.orientation} car.jpg'), (self.x, self.y))

    def draw_fuel(self, fill_level_0to5):
        self.fill_level_0to5 = fill_level_0to5
        self.parent_screen.blit(pygame.image.load(f'resources/fuels/fuel {self.fill_level_0to5}.jpg'),
                                (40 * 15, 8 * 40))
        self.parent_screen.blit(pygame.image.load(f'resources/fuel label.jpg'), (40 * 16.8, 10 * 40))

    def move_up(self):

        self.can_move = True
        for list in self.map_list:
            if (40 * list[0]) == (self.x) and (40 * list[1]) == (self.y - 40):
                self.can_move = False
                break
        if self.can_move:
            self.y = self.y - 40
            self.orientation = 'up'
            self.fuel_count += 1

    def move_down(self):

        self.can_move = True
        for list in self.map_list:
            if (40 * list[0]) == (self.x) and (40 * list[1]) == (self.y + 40):
                self.can_move = False
                break
        if self.can_move:
            self.y = self.y + 40
            self.orientation = 'down'
            self.fuel_count += 1

    def move_left(self):

        self.can_move = True
        for list in self.map_list:
            if (40 * list[0]) == (self.x - 40) and (40 * list[1]) == (self.y):
                self.can_move = False
                break
        if self.can_move:
            self.x = self.x - 40
            self.orientation = 'left'
            self.fuel_count += 1

    def move_right(self):

        self.can_move = True
        for list in self.map_list:
            if (40 * list[0]) == (self.x + 40) and (40 * list[1]) == (self.y):
                self.can_move = False
                break
        if self.can_move:
            self.x = self.x + 40
            self.orientation = 'right'
            self.fuel_count += 1


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(size=(880, 560))
        self.surface.fill((200, 255, 255))
        self.map_list = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11],
                         [1, 12],
                         [2, 1], [2, 3], [2, 4], [2, 12],
                         [3, 1], [3, 3], [3, 4], [3, 7], [3, 5], [3, 6], [3, 9], [3, 10], [3, 12],
                         [4, 1], [4, 5], [4, 12],
                         [5, 1], [5, 3], [5, 5], [5, 7], [5, 8], [5, 10], [5, 12],
                         [6, 1], [6, 3], [6, 10], [6, 11], [6, 12],
                         [7, 1], [7, 5], [7, 7], [7, 8], [7, 6], [7, 10], [7, 12],
                         [8, 1], [8, 3], [8, 5], [8, 6], [8, 7], [8, 8], [8, 10], [8, 12],
                         [9, 1], [9, 5], [9, 6], [9, 12],
                         [10, 1], [10, 2], [10, 3], [10, 5], [10, 8], [10, 10], [10, 12],
                         [11, 1], [11, 2], [11, 7], [11, 8], [11, 10], [11, 11], [11, 12],
                         [12, 1], [12, 2], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10],
                         [12, 11], [12, 12]]

        self.bg = Map(10, self.surface, self.map_list)
        self.dog = Pet(self.surface, 'dog', 2, 6, 9, 11)
        self.cat = Pet(self.surface, 'cat', 9, 7, 6, 6)
        self.player = Player(self.surface, 5, 4, self.map_list)
        self.pet_positions = [False, False, False, False]
        self.ding_sound = pygame.mixer.Sound('resources/ding.mp3')
        pygame.mixer.music.load('resources/bg_music.mp3')
        pygame.mixer.music.play(3)
        pygame.display.set_caption('Pet Delivery Service')
        self.fuel_numbers = [[7,14,21,28,34],
                             [6,13,19,25,29],
                             [8,16,25,34,42],
                             [8,17,26,36,45],
                             [6,14,23,33,36],
                             [6,19,35,51,60],
                             [6,14,24,33,42]]

    def configure_fuel(self,fuel_values):
        self.fuel_values_list = fuel_values
        if self.player.fuel_count <= self.fuel_values_list[0]:
            self.player.draw_fuel(str(5))
        if self.player.fuel_count > self.fuel_values_list[0] and self.player.fuel_count <= self.fuel_values_list[1]:
            self.player.draw_fuel(str(4))
        if self.player.fuel_count > self.fuel_values_list[1] and self.player.fuel_count <= self.fuel_values_list[2]:
            self.player.draw_fuel(str(3))
        if self.player.fuel_count > self.fuel_values_list[2] and self.player.fuel_count <= self.fuel_values_list[3]:
            self.player.draw_fuel(str(2))
        if self.player.fuel_count > self.fuel_values_list[3] and self.player.fuel_count <= self.fuel_values_list[4]:
            self.player.draw_fuel(str(1))
        if self.player.fuel_count > self.fuel_values_list[4]:
            self.player.draw_fuel(str(0))


    def draw_during_game_message(self):
        self.during_font = pygame.font.SysFont('ariel', 30)
        self.during_message = self.during_font.render(f'deliver the pets in the shortest route! Press enter to restart',
                                                      True, (0, 0, 0))
        self.surface.blit(self.during_message, (80, 10))

    def draw_level_message(self, level):
        self.level_font = pygame.font.SysFont('ariel', 30)
        self.level_message = self.level_font.render(f'level {level}', True, (0, 0, 0))
        self.surface.blit(self.level_message, (6 * 40, 13.2 * 40))

    def draw_game_end_message(self, outcome):
        self.outcome = outcome
        self.end_font = pygame.font.SysFont('ariel', 30)
        if self.outcome == True:
            self.end_message = self.end_font.render(f'You win! Press enter to advance to the next level', True,
                                                    (0, 0, 0))
        else:
            self.end_message = self.end_font.render(f'You lose! Press enter to replay', True, (0, 0, 0))
        self.surface.blit(self.end_message, (80, 10))

    def pick_up_pet(self):
        for pet in Pet._registry:
            if self.player.x == pet.x and self.player.y == pet.y:
                pet.pick_up_pet(self.pet_positions)
                self.pet_positions = pet.pet_positions

    def drop_off_pet(self):
        for pet in Pet._registry:
            if pet.show_pet == True:
                if pet.pet_picked_up == True and self.player.x == pet.pethouse.x and self.player.y == pet.pethouse.y:
                    pet.show_pet = False
                    pygame.mixer.Sound.play(self.ding_sound)
                    if pet.pet_bag_position == 1:
                        self.pet_positions[0] = False
                    if pet.pet_bag_position == 2:
                        self.pet_positions[1] = False
                    if pet.pet_bag_position == 3:
                        self.pet_positions[2] = False
                    if pet.pet_bag_position == 4:
                        self.pet_positions[3] = False

    def draw_pets_and_houses(self):
        for pet in Pet._registry:
            if pet.show_pet:
                pet.draw_pet()

            pet.pethouse.draw_pethouse()

    def show_full_sign(self):
        if self.pet_positions[0] == True and self.pet_positions[1] == True and self.pet_positions[2] == True and self.pet_positions[3] == True:
            self.surface.blit(pygame.image.load('resources/full.jpg'), (40 * 19.5, 4 * 40))

    def initialize_level1(self):
        # self.surface.fill((200, 255, 255))
        for pet in Pet._registry:
            del pet
        Pet._registry = []
        self.bg.draw_map()
        self.dog = Pet(self.surface, 'dog', 2, 6, 9, 11)
        self.cat = Pet(self.surface, 'cat', 9, 7, 6, 6)
        self.player = Player(self.surface, 5, 4, self.map_list)
        self.pet_positions = [False, False, False, False]

    def initialize_level2(self):
        for pet in Pet._registry:
            del pet
        Pet._registry = []
        self.bg.draw_map()
        self.dog = Pet(self.surface, 'dog', 9, 8, 3, 2)
        self.cat = Pet(self.surface, 'cat', 8, 2, 6, 4)
        self.player = Player(self.surface, 6, 5, self.map_list)
        self.pet_positions = [False, False, False, False]

    def initialize_level3(self):

        # self.surface.fill((200, 255, 255))
        for pet in Pet._registry:
            del pet
        Pet._registry = []
        self.bg.draw_map()
        self.dog = Pet(self.surface, 'dog', 9, 10, 7, 9)
        self.cat = Pet(self.surface, 'cat', 4, 10, 7, 11)
        self.fish = Pet(self.surface, 'fish', 4, 6, 6, 8)
        self.rabbit = Pet(self.surface, 'rabbit', 6, 2, 10, 7)
        self.player = Player(self.surface, 2, 7, self.map_list)
        self.pet_positions = [False, False, False, False]

    def initialize_level4(self):
        for pet in Pet._registry:
            del pet
        Pet._registry = []
        self.bg.draw_map()
        self.dog = Pet(self.surface, 'dog', 6, 6, 10, 4)
        self.cat = Pet(self.surface, 'cat', 4, 7, 7, 9)
        self.fish = Pet(self.surface, 'fish', 3, 2, 3, 11)
        self.rabbit = Pet(self.surface, 'rabbit', 10, 9, 2, 7)
        self.player = Player(self.surface, 7, 2, self.map_list)
        self.pet_positions = [False, False, False, False]

    def initialize_level5(self):
        for pet in Pet._registry:
            del pet
        Pet._registry = []
        self.bg.draw_map()
        self.dog = Pet(self.surface, 'dog', 4, 7, 7, 3)
        self.cat = Pet(self.surface, 'cat', 7, 9, 9, 10)
        self.fish = Pet(self.surface, 'fish', 5, 6, 2, 8)
        self.rabbit = Pet(self.surface, 'rabbit', 9, 8, 11, 3)
        self.player = Player(self.surface, 10, 9, self.map_list)
        self.pet_positions = [False, False, False, False]

    def initialize_level6(self):
        for pet in Pet._registry:
            del pet
        Pet._registry = []
        self.bg.draw_map()
        self.dog = Pet(self.surface, 'dog', 4, 8, 7, 11)
        self.cat = Pet(self.surface, 'cat', 11, 9, 8, 4)
        self.fish = Pet(self.surface, 'fish', 6, 8, 2, 9)
        self.rabbit = Pet(self.surface, 'rabbit', 10, 7, 3, 11)
        self.snake = Pet(self.surface, 'snake', 10, 11, 8, 11)
        self.bird = Pet(self.surface, 'bird', 5, 2, 5, 6)
        self.player = Player(self.surface, 9, 10, self.map_list)
        self.pet_positions = [False, False, False, False]

    def initialize_level7(self):
        for pet in Pet._registry:
            del pet
        Pet._registry = []
        self.bg.draw_map()
        self.dog = Pet(self.surface, 'dog', 7, 4, 9, 4)
        self.cat = Pet(self.surface, 'cat', 5, 4, 4, 8)
        self.fish = Pet(self.surface, 'fish', 5, 9, 7, 11)
        self.rabbit = Pet(self.surface, 'rabbit', 6, 4, 3, 11)
        self.snake = Pet(self.surface, 'snake', 5, 2, 11, 5)
        self.bird = Pet(self.surface, 'bird', 4, 4, 9, 9)
        self.player = Player(self.surface, 3, 2, self.map_list)
        self.pet_positions = [False, False, False, False]

    def level(self,which_level):
        self.current_level = which_level
        self.running = True
        self.game_over = False

        while self.running:
            self.bg.draw_map()
            self.drop_off_pet()
            self.pick_up_pet()
            self.draw_pets_and_houses()
            self.show_full_sign()
            self.player.draw_player()
            if not self.game_over:
                self.draw_during_game_message()
            self.draw_level_message(self.current_level)

            # if self.player.fuel_count <= 35:
            self.configure_fuel(self.fuel_numbers[self.current_level-1])

            self.all_pets_invisible = True
            for pet in Pet._registry:
                if pet.show_pet == True:
                    self.all_pets_invisible = False
            if self.all_pets_invisible:
                self.game_over = True

            if self.player.fuel_count > self.fuel_numbers[self.current_level-1][-1]:
                self.game_over = True

            if self.game_over:
                if self.all_pets_invisible == True:
                    self.draw_game_end_message(True)
                if self.player.fuel_count > self.fuel_numbers[self.current_level-1][-1] and self.all_pets_invisible == False:
                    self.draw_game_end_message(False)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                    if self.player.fuel_count <= self.fuel_numbers[self.current_level-1][-1]:
                        if event.key == K_UP:
                            self.player.move_up()
                        if event.key == K_DOWN:
                            self.player.move_down()
                        if event.key == K_LEFT:
                            self.player.move_left()
                        if event.key == K_RIGHT:
                            self.player.move_right()
                    if event.key == K_RETURN:
                        if self.all_pets_invisible:
                            self.current_level +=1
                        self.game_over = False
                        if self.current_level == 1:
                            self.initialize_level1()
                        elif self.current_level == 2:
                            self.initialize_level2()
                        elif self.current_level == 3:
                            self.initialize_level3()
                        elif self.current_level == 4:
                            self.initialize_level4()
                        elif self.current_level == 5:
                            self.initialize_level5()
                        elif self.current_level == 6:
                            self.initialize_level6()
                        elif self.current_level == 7:
                            self.initialize_level7()
                elif event.type == QUIT:
                    self.running = False


if __name__ == '__main__':
    game = Game()
    game.level(1)
