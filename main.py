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
        def __init__(self, gain, cost, level, cooldown, x, y):
            self.gain = gain
            self.cost = cost
            self.level = level
            self.cooldown = cooldown
            self.x = x
            self.y = y
        def level_up(self):
            self.level += 1
            self.gain += self.gain + (self.level ** 1.2)
            self.cost += round((self.level ** 1.8) * 100, 0)
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

    shoe_shop = Shop.store(10, 200, 0, 3, 31, 750)
    shirt_shop = Shop.store(25, 500, 0, 5, 185, 750)
    pretzel_shop = Shop.store(75, 1000, 0, 7, 322, 750)
    skate_shop = Shop.store(150, 2000, 0, 12, 455, 750)
    diamond_shop = Shop.store(700, 10000, 0, 30, 580, 750)
    global shop_list
    shop_list = [shoe_shop, shirt_shop, pretzel_shop, skate_shop, diamond_shop]

    while run:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(SHOE, (40, 770))
        WIN.blit(SHIRT, (199, 760))
        WIN.blit(PRETZEL, (339, 765))
        WIN.blit(SKATEBOARD, (471, 760))
        WIN.blit(DIAMOND, (600, 765))
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


        if shoe_shop.level >= 1:
            WIN.blit(SHOESTORE, (15, 125))
        if shirt_shop.level >= 1:
            WIN.blit(SHIRTSTORE, (450, 125))
        if pretzel_shop.level >= 1:
            WIN.blit(PRETZELSTORE, (15, 350))
        if skate_shop.level >= 1:
            WIN.blit(SKATESTORE, (450, 350))
        if diamond_shop.level >= 1:
            WIN.blit(DIAMONDSTORE, (205, 470))

        render_font(str('{:,}'.format(round(balance, 2))), (51, 55))
        render_font(str("$" + str('{:,}'.format(round(rate, 2))) + "/s"), (424, 52))
        render_font(shoe_shop.cost, (55, 705))
        render_font(shirt_shop.cost, (215, 705))
        render_font(pretzel_shop.cost, (355, 705))
        render_font(skate_shop.cost, (485, 705))
        render_font(diamond_shop.cost, (610, 705))
        
            
        rate = 0
        for shop in shop_list:
            if shop.level > 0:
                rate += (shop.gain / shop.cooldown)

        balance += rate / 60
        draw_main_window()

main()