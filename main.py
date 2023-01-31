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
DIAMOND = pygame.transform.scale(SKATEBOARD_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

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

SHOESTORE_BASE_INCOME = 10
SHIRTSTORE_BASE_INCOME = 25
PRETZELSTORE_BASE_INCOME = 75
SKATEBOARDSTORE_BASE_INCOME = 150
DIAMONDSTORE_BASE_INCOME = 700

pygame.font.init()
GENERAL_FONT = pygame.font.SysFont('comicsans', 30)

COLOR_BLACK = (0, 0, 0)

STARTING_BALANCE = 1000

FPS = 60


def render_font(text, position):
    text_sprite = GENERAL_FONT.render(str(text), 1, COLOR_BLACK)
    WIN.blit(text_sprite, position)

def draw_main_window(balance, selected_store, shop):

    if selected_store == "shoe":
        SHOE_SPRITE = pygame.image.load(os.path.join('Images', 'shoe_selected.png')).convert_alpha()
        SHOE = pygame.transform.scale(SHOE_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))
    else:
        SHOE_SPRITE = pygame.image.load(os.path.join('Images', 'shoe.png')).convert_alpha()
        SHOE = pygame.transform.scale(SHOE_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

    if selected_store == "shirt":
        SHIRT_SPRITE = pygame.image.load(os.path.join('Images', 'shirt_selected.png')).convert_alpha()
        SHIRT = pygame.transform.scale(SHIRT_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))
    else:
        SHIRT_SPRITE = pygame.image.load(os.path.join('Images', 'shirt.png')).convert_alpha()
        SHIRT = pygame.transform.scale(SHIRT_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

    if selected_store == "pretzel":
        PRETZEL_SPRITE = pygame.image.load(os.path.join('Images', 'pretzel_selected.png')).convert_alpha()
        PRETZEL = pygame.transform.scale(PRETZEL_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))
    else:
        PRETZEL_SPRITE = pygame.image.load(os.path.join('Images', 'pretzel.png')).convert_alpha()
        PRETZEL = pygame.transform.scale(PRETZEL_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

    if selected_store == "skateboard":
        SKATEBOARD_SPRITE = pygame.image.load(os.path.join('Images', 'skateboard_selected.png')).convert_alpha()
        SKATEBOARD = pygame.transform.scale(SKATEBOARD_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))
    else:
        SKATEBOARD_SPRITE = pygame.image.load(os.path.join('Images', 'skateboard.png')).convert_alpha()
        SKATEBOARD = pygame.transform.scale(SKATEBOARD_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

    if selected_store == "diamond":
        DIAMOND_SPRITE = pygame.image.load(os.path.join('Images', 'diamond_selected.png')).convert_alpha()
        DIAMOND = pygame.transform.scale(DIAMOND_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))
    else:
        DIAMOND_SPRITE = pygame.image.load(os.path.join('Images', 'diamond.png')).convert_alpha()
        DIAMOND = pygame.transform.scale(DIAMOND_SPRITE, (SHOP_WIDTH, SHOP_HEIGHT))

    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(SHOE, (40, 770))
    WIN.blit(SHIRT, (199, 760))
    WIN.blit(PRETZEL, (339, 765))
    WIN.blit(SKATEBOARD, (471, 760))
    WIN.blit(DIAMOND, (600, 765))

    if shop.shoe_store_level >= 1:
        WIN.blit(SHOESTORE, (15, 125))
    if shop.shirt_store_level >= 1:
        WIN.blit(SHIRTSTORE, (450, 125))
    if shop.pretzel_store_level >= 1:
        WIN.blit(PRETZELSTORE, (15, 350))
    if shop.skate_store_level >= 1:
        WIN.blit(SKATESTORE, (450, 350))
    if shop.diamond_store_level >= 1:
        WIN.blit(DIAMONDSTORE, (205, 470))


    render_font(str('{:,}'.format(round(balance, 2))), (51, 55))
    render_font(shop.shoe_store_cost, (55, 705))
    render_font(shop.shirt_store_cost, (215, 705))
    render_font(shop.pretzel_store_cost, (355, 705))
    render_font(shop.skate_store_cost, (485, 705))
    render_font(shop.diamond_store_cost, (610, 705))
    render_font(str("$" + str('{:,}'.format(round(rate, 2))) + "/s"), (424, 52))

    pygame.display.update()

class Shop():
    def __init__(self):
        self.shoe_store_cost = 200
        self.shoe_store_level = 0
        self.shoe_store_cooldown = 3

        self.shirt_store_cost = 500
        self.shirt_store_level = 0
        self.shirt_store_cooldown = 5

        self.pretzel_store_cost = 1000
        self.pretzel_store_level = 0
        self.pretzel_store_cooldown = 7

        self.skate_store_cost = 2000
        self.skate_store_level = 0
        self.skate_store_cooldown = 12

        self.diamond_store_cost = 10000
        self.diamond_store_level = 0
        self.diamond_store_cooldown = 30


def main():
    global level
    level = 0

    shop = Shop()

    selected_store = ""

    tick = 0
    run = True
    global balance
    balance = STARTING_BALANCE
    global rate
    rate = 0

    while run:
        tick += 1
        pygame.time.Clock().tick(FPS)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if 33 <= mouse[0] <= 156 and 753 <= mouse[1] <= 867 and balance >= shop.shoe_store_cost:
                selected_store = "shoe"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shop.shoe_store_level += 1
                    balance -= shop.shoe_store_cost
                    shop.shoe_store_cost += (shop.shoe_store_level * 100)
                    if shop.shoe_store_level > 1:
                        shop.shoe_store_cooldown - .6
            elif 186 <= mouse[0] <= 304 and 753 <= mouse[1] <= 867 and balance >= shop.shirt_store_cost:
                selected_store = "shirt"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shop.shirt_store_level += 1
                    balance -= shop.shirt_store_cost
                    shop.shirt_store_cost += (shop.shirt_store_level * 200)
                    if shop.shirt_store_level > 1:
                        shop.shirt_store_cooldown - .6
            elif 333 <= mouse[0] <= 433 and 753 <= mouse[1] <= 867 and balance >= shop.pretzel_store_cost:
                selected_store = "pretzel"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shop.pretzel_store_level += 1
                    balance -= shop.pretzel_store_cost
                    shop.pretzel_store_cost += (shop.pretzel_store_level * 300)
                    if shop.pretzel_store_level > 1:
                        shop.pretzel_store_cooldown - .6
            elif 469 <= mouse[0] <= 570 and 753 <= mouse[1] <= 867 and balance >= shop.skate_store_cost:
                selected_store = "skateboard"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shop.skate_store_level += 1
                    balance -= shop.skate_store_cost
                    shop.skate_store_cost += (shop.skate_store_level * 500)
                    if shop.skate_store_level > 1:
                        shop.skate_store_cooldown - .6
            elif 569 <= mouse[0] <= 690 and 753 <= mouse[1] <= 867 and balance >= shop.diamond_store_cost:
                selected_store = "diamond"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shop.diamond_store_level += 1
                    balance -= shop.diamond_store_cost
                    shop.diamond_store_cost += (shop.diamond_store_level * 900)
                    if shop.diamond_store_level > 1:
                        shop.diamond_store_cooldown - .6
            else:
                selected_store = ""
            
        rate = (SHOESTORE_BASE_INCOME * (shop.shoe_store_level ** 1.8) / shop.shoe_store_cooldown) + (
            SHIRTSTORE_BASE_INCOME * (shop.shirt_store_level ** 1.8) / shop.shirt_store_cooldown) + (
            PRETZELSTORE_BASE_INCOME * (shop.pretzel_store_level ** 1.8) / shop.pretzel_store_cooldown) + (
            SKATEBOARDSTORE_BASE_INCOME * (shop.skate_store_level ** 1.8) / shop.skate_store_cooldown) + (
            DIAMONDSTORE_BASE_INCOME * (shop.diamond_store_level ** 1.8) / shop.diamond_store_cooldown)

        balance += rate / 60
        draw_main_window(balance, selected_store, shop)

main()
        

