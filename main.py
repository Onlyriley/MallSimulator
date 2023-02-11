import pygame
import pickle
import os
from random import randint
import threading
from time import sleep
import math
import numpy
WIDTH, HEIGHT = 720, 900
SHOP_WIDTH, SHOP_HEIGHT = 100, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mall Simulator")
pygame.font.init()
GENERAL_FONT = pygame.font.SysFont('comicsans', 30)

BACKGROUND_SPRITE = pygame.image.load(os.path.join('Images', 'background.png')).convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND_SPRITE, (WIDTH, HEIGHT))

START_SPRITE = pygame.image.load(os.path.join('Images', 'start_screen.png')).convert_alpha()
START = pygame.transform.scale(START_SPRITE, (WIDTH, HEIGHT))

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

PANTS_SPRITE = pygame.image.load(os.path.join('Images', 'pants.png')).convert_alpha()
PANTS = pygame.transform.scale(PANTS_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

PANTSSTORE_SPRITE = pygame.image.load(os.path.join('Images', 'pants_store.png')).convert_alpha()
PANTSSTORE = pygame.transform.scale(PANTSSTORE_SPRITE, (250, 250))

HAT_SPRITE = pygame.image.load(os.path.join('Images', 'hat.png')).convert_alpha()
HAT = pygame.transform.scale(HAT_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

HATSTORE_SPRITE = pygame.image.load(os.path.join('Images', 'hat_store.png')).convert_alpha()
HATSTORE = pygame.transform.scale(HATSTORE_SPRITE, (250, 250))

POPCORN_SPRITE = pygame.image.load(os.path.join('Images', 'popcorn.png')).convert_alpha()
POPCORN = pygame.transform.scale(POPCORN_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

POPCORNSTORE_SPRITE = pygame.image.load(os.path.join('Images', 'popcorn_store.png')).convert_alpha()
POPCORNSTORE = pygame.transform.scale(POPCORNSTORE_SPRITE, (250, 250))

GLASSES_SPRITE = pygame.image.load(os.path.join('Images', 'glasses.png')).convert_alpha()
GLASSES = pygame.transform.scale(GLASSES_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

GLASSESSTORE_SPRITE = pygame.image.load(os.path.join('Images', 'glasses_store.png')).convert_alpha()
GLASSESSTORE = pygame.transform.scale(GLASSESSTORE_SPRITE, (250, 250))

GOLD_SPRITE = pygame.image.load(os.path.join('Images', 'gold.png')).convert_alpha()
GOLD = pygame.transform.scale(GOLD_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

GOLDSTORE_SPRITE = pygame.image.load(os.path.join('Images', 'gold_store.png')).convert_alpha()
GOLDSTORE = pygame.transform.scale(GOLDSTORE_SPRITE, (300, 300))

CROSSHAIR_SPRITE = pygame.image.load(os.path.join('Images', 'crosshair.png')).convert_alpha()
CROSSHAIR = pygame.transform.scale(CROSSHAIR_SPRITE, (70, 70))

NEXT_SPRITE = pygame.image.load(os.path.join('Images', 'next.png')).convert_alpha()
NEXT = pygame.transform.scale(NEXT_SPRITE, (100, 100))

BACK_SPRITE = pygame.image.load(os.path.join('Images', 'back.png')).convert_alpha()
BACK = pygame.transform.scale(BACK_SPRITE, (100, 100))

PERSON_SPAWN_X = WIDTH / 2
PERSON_SPAWN_Y = 100

pygame.font.init()
GENERAL_FONT = pygame.font.SysFont('comicsans', 30)
SMALL_FONT = pygame.font.SysFont('comicsans', 25)

COLOR_BLACK = (0, 0, 0)

STARTING_BALANCE = 1000

FPS = 60


def render_font(text, position):
    text_sprite = GENERAL_FONT.render(str(text), 1, COLOR_BLACK)
    WIN.blit(text_sprite, position)

def render_small_font(text, position):
    text_sprite = SMALL_FONT.render(str(text), 1, COLOR_BLACK)
    WIN.blit(text_sprite, position)

def draw_main_window(person_list, game):
    WIN.blit(BACKGROUND, (0, 0))
    for shop in game.shop_list:
        WIN.blit(shop.shop_icon, (shop.icon_x, shop.icon_y))
        if shop.selected:
            WIN.blit(SELECTED, (shop.x, shop.y))
        if shop.level >= 1:
            WIN.blit(shop.shop_store, (shop.shop_x, shop.shop_y))
            render_small_font("x" + str(shop.level), (shop.x + 85, shop.y - 10))
        render_small_font(formatBalance(shop.cost), (shop.text_x, shop.text_y))
    render_font((formatBalance(game.balance)), (51, 55))
    render_font((formatBalance(rate) + "/s"), (424, 52))
    draw_people(person_list)
    for crosshair in click_list:
        crosshair.duration -= 1
        if crosshair.duration == 0:
            click_list.remove(crosshair)
        WIN.blit(CROSSHAIR, (crosshair.x, crosshair.y))
    
    level_total = 0
    for shop in game.shop_list:
        level_total += shop.level
    if len(game.button_list) <= 2:
        if level_total >= game.shop_threashold:
            game.upgradable = True
            game.button_list.append(Button(570, 630, 100, 100, NEXT))
        if game.level > 1:
            game.button_list.append(Button(50, 630, 100, 100, BACK))

    for button in game.button_list:
        WIN.blit(button.icon, (button.x, button.y))

    for shop in game.shop_list:
        if shop.selected == True:
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
            self.selected = False
            self.find_position()
        def find_position(self):
            if self.position == 1:
                self.x = 31
                self.y = 750
                self.icon_x = 40
                self.icon_y = 770
                self.shop_x = 15
                self.shop_y = 125
                self.text_x = 43
                self.text_y = 705
            elif self.position == 2:
                self.x = 185
                self.y = 750
                self.icon_x = 199
                self.icon_y = 760
                self.shop_x = 450
                self.shop_y = 125
                self.text_x = 205
                self.text_y = 705
            elif self.position == 3:
                self.x = 322
                self.y = 750
                self.icon_x = 339
                self.icon_y = 765
                self.shop_x = 15
                self.shop_y = 350
                self.text_x = 345
                self.text_y = 705
            elif self.position == 4:
                self.x = 455
                self.y = 750
                self.icon_x = 471
                self.icon_y = 760
                self.shop_x = 450
                self.shop_y = 350
                self.text_x = 475
                self.text_y = 705
            elif self.position == 5:
                self.x = 580
                self.y = 750
                self.icon_x = 600
                self.icon_y = 760
                self.shop_x = 205
                self.shop_y = 470
                self.text_x = 600
                self.text_y = 705

        def level_up(self):
            self.level += 1
            self.gain += self.gain
            self.cost = round(self.cost ** 1.07)
        def select(self):
            self.selected = True
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
        self.tick = 0
        self.shop = Shop()
        self.shops = []
        self.shop_threashold = 25
        self.init_floor1()
        self.init_floor2()
        self.active_shop(1)
        self.upgradable = False
        self.button_list = []
    def init_floor1(self):
        self.shoe_shop = self.shop.store(10, 200, 0, 3, 1, SHOE, SHOESTORE)
        self.shirt_shop = self.shop.store(25, 500, 0, 5, 2, SHIRT, SHIRTSTORE)
        self.pretzel_shop = self.shop.store(75, 1000, 0, 7, 3, PRETZEL, PRETZELSTORE)
        self.skate_shop = self.shop.store(150, 2000, 0, 12, 4, SKATEBOARD, SKATESTORE)
        self.diamond_shop = self.shop.store(700, 10000, 0, 30, 5, DIAMOND, DIAMONDSTORE)
        self.floor1 = [self.shoe_shop, self.shirt_shop, self.pretzel_shop, self.skate_shop, self.diamond_shop]
        for shop in self.floor1:
            self.shops.append(shop)
    def init_floor2(self):
        self.pants_shop = self.shop.store(1000, 15000, 0, 45, 1, PANTS, PANTSSTORE)
        self.hat_shop = self.shop.store(5000, 250000, 0, 60, 2, HAT, HATSTORE)
        self.popcorn_shop = self.shop.store(12000, 500000, 0, 85, 3, POPCORN, POPCORNSTORE)
        self.glasses_shop = self.shop.store(25000, 850000, 0, 120, 4, GLASSES, GLASSESSTORE)
        self.gold_shop = self.shop.store(1000000, 2000000, 0, 150, 5, GOLD, GOLDSTORE)
        self.floor2 = [self.pants_shop, self.hat_shop, self.popcorn_shop, self.glasses_shop, self.gold_shop]
        for shop in self.floor2:
            self.shops.append(shop)
    def active_shop(self, floor):
        if floor == 1:
            self.shop_list = [self.shoe_shop, self.shirt_shop, self.pretzel_shop, self.skate_shop, self.diamond_shop]
        if floor == 2:
            self.shop_list = [self.pants_shop, self.hat_shop, self.popcorn_shop, self.glasses_shop, self.gold_shop]

class SaveObject():
    def __init__(self, balance, level, store_levels):
        self.balance = balance
        self.level = level
        self.store_levels = store_levels

class Crosshair():
    def __init__(self, x, y):
        self.x = x - 35
        self.y = y - 35
        self.duration = 100

class Button():
    def __init__(self, x, y, width, height, icon):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.icon = icon

def formatBalance(balance):
    if balance >= 1000000:
        return "$" + str(round(balance / 1000000, 2)) + "m"
    if balance >= 1000:
        return "$" + str(round(balance / 1000, 2)) + "k"
    else:
        return "$" + str(round(balance, 2))

def spawn_person():
    person = pygame.Rect(randint(WIDTH/2 - 50, WIDTH/2 + 50), PERSON_SPAWN_Y, 75, 75)
    return person

def draw_people(person_list):
    total_levels = 0
    for shop in game.shop_list:
        total_levels += shop.level
    if randint(0, 200 - int(numpy.cbrt(total_levels * 5000))) == 2:
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
        if game.tick >= 30 and person.person.y >= HEIGHT / 2 - 150:
            person.person.y += 1
        elif person.person.y >= HEIGHT / 2 - 150:
            person.person.y -= 1
        WIN.blit(person.sprite, (person.person.x, person.person.y))

def draw_start_screen():
    pygame.time.Clock().tick(FPS)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if 230 <= mouse[0] <= 470 and 580 <= mouse[1] <= 680:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return False
        if event.type == pygame.QUIT:
            quit()
    WIN.blit(START, (0, 0))
    pygame.display.update()

def main():
    while True:
        if draw_start_screen() == False:
            break

    global game
    game = Gamestate()
    if os.path.exists("Game/data.dictionary"):
        with open("Game/data.dictionary", "rb") as f:
            load = pickle.load(f)
            game.balance = load.balance
            game.level = load.level
            counter = 0
            for store in game.shops:
                for level in range(load.store_levels[counter]):
                    store.level_up()
                counter += 1
    run = True
    global rate
    person_list = []
    global click_list
    click_list = []
    game.active_shop(1)
    while run:
        pygame.time.Clock().tick(FPS)
        game.tick += 2
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                store_levels = []
                for store in game.shops:
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
            for button in game.button_list:
                if button.x <= mouse_x <= (button.x + button.width) and button.y <= mouse_y <= (button.y + button.height) and event.type == pygame.MOUSEBUTTONDOWN:
                    person_list = []
                    if button.icon == NEXT:
                        game.level += 1
                        game.active_shop(game.level)
                        game.button_list = []
                    if button.icon == BACK:
                        game.level -= 1
                        game.button_list = []
                        game.active_shop(game.level)
            
        rate = 0
        for shop in game.shops:
            if shop.level > 0:
                rate += (shop.gain / shop.cooldown)
        game.balance += rate / 60
        if game.tick >= 60:
            game.tick = 0
        draw_main_window(person_list, game)

main()