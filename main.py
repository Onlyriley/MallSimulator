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

def draw_main_window(balance, selected_store):

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

    if shoe_store_level >= 1:
        WIN.blit(SHOESTORE, (15, 125))
    if shirt_store_level >= 1:
        WIN.blit(SHIRTSTORE, (450, 125))
    if pretzel_store_level >= 1:
        WIN.blit(PRETZELSTORE, (15, 350))
    if skate_store_level >= 1:
        WIN.blit(SKATESTORE, (450, 350))
    if diamond_store_level >= 1:
        WIN.blit(DIAMONDSTORE, (205, 470))


    render_font(str('{:,}'.format(round(balance, 2))), (51, 55))
    render_font(shoe_store_cost, (55, 705))
    render_font(shirt_store_cost, (215, 705))
    render_font(pretzel_store_cost, (355, 705))
    render_font(skate_store_cost, (485, 705))
    render_font(diamond_store_cost, (610, 705))
    render_font(str("$" + str('{:,}'.format(round(rate, 2))) + "/s"), (424, 52))

    pygame.display.update()

def main():
    global shoe_store_cost
    shoe_store_cost = 200
    global shoe_store_level
    shoe_store_level = 0
    global shoe_store_cooldown
    shoe_store_cooldown = 3

    global shirt_store_cost
    shirt_store_cost = 500
    global shirt_store_level
    shirt_store_level = 0
    global shirt_store_cooldown
    shirt_store_cooldown = 5

    global pretzel_store_cost
    pretzel_store_cost = 1000
    global pretzel_store_level
    pretzel_store_level = 0
    global pretzel_store_cooldown
    pretzel_store_cooldown = 7

    global skate_store_cost
    skate_store_cost = 2000
    global skate_store_level
    skate_store_level = 0
    global skate_store_cooldown
    skate_store_cooldown = 12

    global diamond_store_cost
    diamond_store_cost = 10000
    global diamond_store_level
    diamond_store_level = 0
    global diamond_store_cooldown
    diamond_store_cooldown = 30

    global level
    level = 0

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
            if 33 <= mouse[0] <= 156 and 753 <= mouse[1] <= 867 and balance >= shoe_store_cost:
                selected_store = "shoe"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shoe_store_level += 1
                    balance -= shoe_store_cost
                    shoe_store_cost += (shoe_store_level * 100)
                    if shoe_store_level > 1:
                        shoe_store_cooldown - .6
            elif 186 <= mouse[0] <= 304 and 753 <= mouse[1] <= 867 and balance >= shirt_store_cost:
                selected_store = "shirt"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shirt_store_level += 1
                    balance -= shirt_store_cost
                    shirt_store_cost += (shirt_store_level * 200)
                    if shirt_store_level > 1:
                        shirt_store_cooldown - .6
            elif 333 <= mouse[0] <= 433 and 753 <= mouse[1] <= 867 and balance >= pretzel_store_cost:
                selected_store = "pretzel"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pretzel_store_level += 1
                    balance -= pretzel_store_cost
                    pretzel_store_cost += (pretzel_store_level * 300)
                    if pretzel_store_level > 1:
                        pretzel_store_cooldown - .6
            elif 469 <= mouse[0] <= 570 and 753 <= mouse[1] <= 867 and balance >= skate_store_cost:
                selected_store = "skateboard"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    skate_store_level += 1
                    balance -= skate_store_cost
                    skate_store_cost += (skate_store_level * 500)
                    if skate_store_level > 1:
                        skate_store_cooldown - .6
            elif 569 <= mouse[0] <= 690 and 753 <= mouse[1] <= 867 and balance >= diamond_store_cost:
                selected_store = "diamond"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    diamond_store_level += 1
                    balance -= diamond_store_cost
                    diamond_store_cost += (diamond_store_level * 900)
                    if diamond_store_level > 1:
                        diamond_store_cooldown - .6
            else:
                selected_store = ""
            
        rate = (SHOESTORE_BASE_INCOME * (shoe_store_level ** 1.8) / shoe_store_cooldown) + (
            SHIRTSTORE_BASE_INCOME * (shirt_store_level ** 1.8) / shirt_store_cooldown) + (
            PRETZELSTORE_BASE_INCOME * (pretzel_store_level ** 1.8) / pretzel_store_cooldown) + (
            SKATEBOARDSTORE_BASE_INCOME * (skate_store_level ** 1.8) / skate_store_cooldown) + (
            DIAMONDSTORE_BASE_INCOME * (diamond_store_level ** 1.8) / diamond_store_cooldown)

        balance += rate / 60
        draw_main_window(balance, selected_store)

main()
        

