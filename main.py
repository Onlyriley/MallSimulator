import pygame
import pickle
import os
from random import randint
import threading
from time import sleep
WIDTH, HEIGHT = 720, 900
SHOP_WIDTH, SHOP_HEIGHT = 100, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mall Simulator")
pygame.font.init()
GENERAL_FONT = pygame.font.SysFont('comicsans', 30)

BACKGROUND_SPRITE = pygame.image.load(os.path.join('Images', 'background.png')).convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND_SPRITE, (WIDTH, HEIGHT))

SHOE_SPRITE = pygame.image.load(os.path.join('Images', 'shoe.png')).convert_alpha()
SHOE = pygame.transform.scale(SHOE_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

SHIRT_SPRITE = pygame.image.load(os.path.join('Images', 'shirt.png')).convert_alpha()
SHIRT = pygame.transform.scale(SHIRT_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

PRETZEL_SPRITE = pygame.image.load(os.path.join('Images', 'pretzel.png')).convert_alpha()
PRETZEL = pygame.transform.scale(PRETZEL_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

SKATEBOARD_SPRITE = pygame.image.load(os.path.join('Images', 'skateboard.png')).convert_alpha()
SKATEBOARD = pygame.transform.scale(SKATEBOARD_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

DIAMOND_SPRITE = pygame.image.load(os.path.join('Images', 'diamond.png')).convert_alpha()
DIAMOND = pygame.transform.scale(DIAMOND_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

STORE_SPRITE = pygame.image.load(os.path.join('Images', 'store_template.png')).convert_alpha()
STORE = pygame.transform.scale(STORE_SPRITE, (250, 250))

SHOESTORE_SPRITE = pygame.image.load(os.path.join('Images', 'shoe_store.png')).convert_alpha()
SHOESTORE = pygame.transform.scale(SHOESTORE_SPRITE, (250, 250))

SHIRTSTORE_SPRITE = pygame.image.load(os.path.join('Images', 'shirt_store.png')).convert_alpha()
SHIRTSTORE = pygame.transform.scale(SHIRTSTORE_SPRITE, (250, 250))

PRETZELSTORE_SPRITE = pygame.image.load(os.path.join('Images', 'pretzel_store.png')).convert_alpha()
PRETZELSTORE = pygame.transform.scale(PRETZELSTORE_SPRITE, (250, 250))

SKATESTORE_SPRITE = pygame.image.load(os.path.join('Images', 'skate_store.png')).convert_alpha()
SKATESTORE = pygame.transform.scale(SKATESTORE_SPRITE, (250, 250))

DIAMONDSTORE_SPRITE = pygame.image.load(os.path.join('Images', 'diamond_store.png')).convert_alpha()
DIAMONDSTORE = pygame.transform.scale(DIAMONDSTORE_SPRITE, (300, 300))

SELECTED_SPRITE = pygame.image.load(os.path.join('Images', 'selected.png')).convert_alpha()
SELECTED = pygame.transform.scale(SELECTED_SPRITE, (124, 124))

PERSON1_SPRITE = pygame.image.load(os.path.join('Images', 'person1.png')).convert_alpha()
PERSON1 = pygame.transform.scale(PERSON1_SPRITE, (75, 75))

PERSON2_SPRITE = pygame.image.load(os.path.join('Images', 'person2.png')).convert_alpha()
PERSON2 = pygame.transform.scale(PERSON2_SPRITE, (75, 75))

PERSON3_SPRITE = pygame.image.load(os.path.join('Images', 'person3.png')).convert_alpha()
PERSON3 = pygame.transform.scale(PERSON3_SPRITE, (75, 75))

PERSON4_SPRITE = pygame.image.load(os.path.join('Images', 'person4.png')).convert_alpha()
PERSON4 = pygame.transform.scale(PERSON4_SPRITE, (75, 75))

PERSON5_SPRITE = pygame.image.load(os.path.join('Images', 'person5.png')).convert_alpha()
PERSON5 = pygame.transform.scale(PERSON5_SPRITE, (75, 75))

PERSON6_SPRITE = pygame.image.load(os.path.join('Images', 'person6.png')).convert_alpha()
PERSON6 = pygame.transform.scale(PERSON6_SPRITE, (75, 75))

PERSON_SPAWN_X = WIDTH / 2
PERSON_SPAWN_Y = 100

pygame.font.init()
GENERAL_FONT = pygame.font.SysFont('comicsans', 30)

COLOR_BLACK = (0, 0, 0)

STARTING_BALANCE = 1000

FPS = 60


def render_font(text, position):
    text_sprite = GENERAL_FONT.render(str(text), 1, COLOR_BLACK)
    WIN.blit(text_sprite, position)

def draw_main_window():
    for shop in game.shop_list:
        if shop.selected:
            WIN.blit(SELECTED, (shop.x, shop.y))
    pygame.display.update()

class Shop():
    def __init__(self):
        pass
    class store():
        def __init__(self, gain, cost, level, cooldown, position, shop_icon, shop_store):
            self.gain = gain
            self.cost = cost
            self.level = level
            self.cooldown = cooldown
            self.shop_icon = shop_icon
            self.shop_store = shop_store
            self.position = position
            self.find_position()
        def find_position(self):
            if self.position == 1:
                self.x = 31
                self.y = 750
                self.icon_x = 40
                self.icon_y = 770
                self.shop_x = 15
                self.shop_y = 125
                self.text_x = 55
                self.text_y = 705
            elif self.position == 2:
                self.x = 185
                self.y = 750
                self.icon_x = 199
                self.icon_y = 760
                self.shop_x = 450
                self.shop_y = 125
                self.text_x = 215
                self.text_y = 705
            elif self.position == 3:
                self.x = 322
                self.y = 750
                self.icon_x = 339
                self.icon_y = 765
                self.shop_x = 15
                self.shop_y = 350
                self.text_x = 355
                self.text_y = 705
            elif self.position == 4:
                self.x = 455
                self.y = 750
                self.icon_x = 471
                self.icon_y = 760
                self.shop_x = 450
                self.shop_y = 350
                self.text_x = 485
                self.text_y = 705
            elif self.position == 5:
                self.x = 580
                self.y = 750
                self.icon_x = 600
                self.icon_y = 760
                self.shop_x = 205
                self.shop_y = 470
                self.text_x = 610
                self.text_y = 705

        def level_up(self):
            self.level += 1
            self.gain += self.gain
            self.cost = round(self.cost ** 1.07)
            #self.cooldown = self.cooldown ** .99
        def select(self):
            self.selected = True
            #WIN.blit(SELECTED, (self.x, self.y))
        def get_rate(self):
            if self.level >= 1:
                return round(self.gain / self.cooldown, 0)
            else:
                return 0

class Person():
    def __init__(self, person):
        self.person = person
        model = randint(1, 6)
        if model == 1:
            self.sprite = PERSON1
        elif model == 2:
            self.sprite = PERSON2
        elif model == 3:
            self.sprite = PERSON3
        elif model == 4:
            self.sprite = PERSON4
        elif model == 5:
            self.sprite = PERSON5
        elif model == 6:
            self.sprite = PERSON6
        direction = randint(1, 2)
        if direction == 1:
            self.right = True
        else:
            self.right = False

class Gamestate():
    def __init__(self):
        self.balance = STARTING_BALANCE
        self.level = 1
        self.shop = Shop()
        self.init_floor1()
    def init_floor1(self):
        self.shoe_shop = self.shop.store(10, 200, 0, 3, 1, SHOE, SHOESTORE)
        self.shirt_shop = self.shop.store(25, 500, 0, 5, 2, SHIRT, SHIRTSTORE)
        self.pretzel_shop = self.shop.store(75, 1000, 0, 7, 3, PRETZEL, PRETZELSTORE)
        self.skate_shop = self.shop.store(150, 2000, 0, 12, 4, SKATEBOARD, SKATESTORE)
        self.diamond_shop = self.shop.store(700, 10000, 0, 30, 5, DIAMOND, DIAMONDSTORE)
        self.shop_list = [self.shoe_shop, self.shirt_shop, self.pretzel_shop, self.skate_shop, self.diamond_shop]
    
class SaveObject():
    def __init__(self, balance, level, store_levels):
        self.balance = balance
        self.level = level
        self.store_levels = store_levels

def formatBalance(balance):
    if balance >= 1000:
        return "$" + str(round(balance / 1000, 2)) + "k"
    else:
        return "$" + str(round(balance, 2))

def spawn_person():
    person = pygame.Rect(randint(WIDTH/2 - 50, WIDTH/2 + 50), PERSON_SPAWN_Y, 75, 75)
    return person

def draw_people(tick):
    if randint(0, 300) == 2:
        person_list.append(Person(spawn_person()))

    for person in person_list:

        if person.person.x <= -50 or person.person.x >= WIDTH:
            person_list.remove(person)
            continue
        if person.person.y >= HEIGHT / 2 - 150:
            if person.right == True:
                person.person.x += 2
            else:
                person.person.x -= 2
        else:
            person.person.y += 2


        if tick >= 30 and person.person.y >= HEIGHT / 2 - 150:
            person.person.y += 1
        elif person.person.y >= HEIGHT / 2 - 150:
            person.person.y -= 1
        WIN.blit(person.sprite, (person.person.x, person.person.y))

def main():
    global game
    game = Gamestate()

    if os.path.exists("Game/data.dictionary"):
        with open("Game/data.dictionary", "rb") as f:
            load = pickle.load(f)
            game.balance = load.balance
            game.level = load.level
            counter = 0
            for store in game.shop_list:
                for level in range(load.store_levels[counter]):
                    store.level_up()
                counter += 1


    tick = 0
    run = True
    global rate
    rate = 0
    global person_list
    person_list = []



    while run:
        WIN.blit(BACKGROUND, (0, 0))

        for shop in game.shop_list:
            WIN.blit(shop.shop_icon, (shop.icon_x, shop.icon_y))

        pygame.time.Clock().tick(FPS)
        tick += 2


        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                store_levels = []
                for store in game.shop_list:
                    store_levels.append(store.level)
                save = SaveObject(game.balance, game.level, store_levels)
                with open("Game/data.dictionary", "wb") as f:
                    pickle.dump(save, f)
                run = False
            for shop in game.shop_list:
                if shop.x <= mouse_x <= (shop.x + 124) and shop.y <= mouse_y <= (shop.y + 124) and game.balance >= shop.cost:
                    shop.selected = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game.balance -= shop.cost
                        shop.level_up()
                else:
                    shop.selected = False

        for shop in game.shop_list:
            if shop.level >= 1:
                WIN.blit(shop.shop_store, (shop.shop_x, shop.shop_y))
                render_font("x" + str(shop.level), (shop.x + 85, shop.y - 10))


        render_font((formatBalance(game.balance)), (51, 55))
        render_font((formatBalance(rate) + "/s"), (424, 52))

        for shop in game.shop_list:
            render_font(formatBalance(shop.cost), (shop.text_x, shop.text_y))
        
            
        rate = 0
        for shop in game.shop_list:
            if shop.level > 0:
                rate += (shop.gain / shop.cooldown)

        game.balance += rate / 60
        if tick >= 60:
            tick = 0
        draw_people(tick)

        draw_main_window()

main()