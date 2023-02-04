import pygame
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

pygame.font.init()
GENERAL_FONT = pygame.font.SysFont('comicsans', 30)

COLOR_BLACK = (0, 0, 0)

STARTING_BALANCE = 1000

FPS = 60


def render_font(text, position):
    text_sprite = GENERAL_FONT.render(str(text), 1, COLOR_BLACK)
    WIN.blit(text_sprite, position)

def draw_main_window():
    for shop in shop_list:
        if shop.selected:
            WIN.blit(SELECTED, (shop.x, shop.y))
    pygame.display.update()

class Shop():
    def __init__(self):
        pass
    class store():
        def __init__(self, gain, cost, level, cooldown, x, y, icon_x, icon_y, shop_x, shop_y, text_x, text_y, shop_icon, shop_store):
            self.gain = gain
            self.cost = cost
            self.level = level
            self.cooldown = cooldown
            self.x = x
            self.y = y
            self.icon_x = icon_x
            self.icon_y = icon_y
            self.shop_x = shop_x
            self.shop_y = shop_y
            self.text_x = text_x
            self.text_y = text_y
            self.shop_icon = shop_icon
            self.shop_store = shop_store
        def level_up(self):
            self.level += 1
            self.gain += self.gain + (self.level ** 1.2)
            self.cost = round(self.cost ** 1.07)
            self.cooldown = self.cooldown ** .99
            print(self.gain)
        def select(self):
            self.selected = True
            #WIN.blit(SELECTED, (self.x, self.y))
        def get_rate(self):
            if self.level >= 1:
                return round(self.gain / self.cooldown, 0)
            else:
                return 0

def formatBalance(balance):
    if balance >= 1000:
        return "$" + str(round(balance / 1000, 2)) + "k"
    else:
        return "$" + str(round(balance, 2))

def init_floor1(Shop):
    shoe_shop = Shop.store(10, 200, 0, 3, 31, 750, 40, 770, 15, 125, 55, 705, SHOE, SHOESTORE)
    shirt_shop = Shop.store(25, 500, 0, 5, 185, 750, 199, 760, 450, 125, 215, 705, SHIRT, SHIRTSTORE)
    pretzel_shop = Shop.store(75, 1000, 0, 7, 322, 750, 339, 765, 15, 350, 355, 705, PRETZEL, PRETZELSTORE)
    skate_shop = Shop.store(150, 2000, 0, 12, 455, 750, 471, 760, 450, 350, 485, 705, SKATEBOARD, SKATESTORE)
    diamond_shop = Shop.store(700, 10000, 0, 30, 580, 750, 600, 760, 205, 470, 610, 705, DIAMOND, DIAMONDSTORE)
    return [shoe_shop, shirt_shop, pretzel_shop, skate_shop, diamond_shop]

def main():
    global level
    level = 0
    shop = Shop()

    tick = 0
    run = True
    global balance
    balance = STARTING_BALANCE
    global rate
    rate = 0
    floor = 1


    global shop_list
    shop_list = init_floor1(shop)

    while run:
        WIN.blit(BACKGROUND, (0, 0))

        for shop in shop_list:
            WIN.blit(shop.shop_icon, (shop.icon_x, shop.icon_y))

        pygame.time.Clock().tick(FPS)
        tick += 1
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            for shop in shop_list:
                if shop.x <= mouse_x <= (shop.x + 124) and shop.y <= mouse_y <= (shop.y + 124) and balance >= shop.cost:
                    shop.selected = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        balance -= shop.cost
                        shop.level_up()
                else:
                    shop.selected = False

        for shop in shop_list:
            if shop.level >= 1:
                WIN.blit(shop.shop_store, (shop.shop_x, shop.shop_y))


        render_font((formatBalance(balance)), (51, 55))
        render_font(str("$" + str('{:,}'.format(round(rate, 2))) + "/s"), (424, 52))

        for shop in shop_list:
            render_font(shop.cost, (shop.text_x, shop.text_y))
        
            
        rate = 0
        for shop in shop_list:
            if shop.level > 0:
                rate += (shop.gain / shop.cooldown)

        balance += rate / 60
        draw_main_window()

main()