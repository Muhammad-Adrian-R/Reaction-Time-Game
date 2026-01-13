# import pygame
# import random
# import time
# import sys

# pygame.init()
# screen = pygame.display.set_mode((1920, 1080))
# pygame.display.set_caption("Reaction Time Test")

# jump_start = pygame.image.load("Asset/JumpStart.png")
# Press2Start = pygame.image.load("Asset/Press2Start.png")
# PressQuickly = pygame.image.load("Asset/PressQuickly.png")
# Results = pygame.image.load("Asset/Results.png")
# Wait4Green = pygame.image.load("Asset/Wait4Green.png")

# state = "start"
# start_time = 0
# reaction_time = 0

# font = pygame.font.Font("Asset/Anton-Regular.ttf", 120)
# white = (255, 255, 255)


# def draw_text(text, y):
#     img = font.render(text, True, white)
#     rect = img.get_rect(center=(640, y))
#     screen.blit(img, rect)


# running = True
# delay_time = 0

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         # Klik mouse
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if state == "start":
#                 # Player mulai → masuk mode tunggu
#                 state = "waiting"
#                 delay_time = time.time() + random.uniform(2, 5)

#             elif state == "waiting":
#                 # Klik terlalu cepat → Jump Start
#                 state = "jump"
#                 reaction_time = 0

#             elif state == "go":
#                 # Hitung reaksi
#                 reaction_time = (time.time() - start_time) * 1000
#                 state = "result"

#             elif state in ("result", "jump"):
#                 # Klik untuk restart game
#                 state = "start"

#     # Ubah status otomatis
#     if state == "waiting":
#         if time.time() >= delay_time:
#             state = "go"
#             start_time = time.time()

#     # Tampilkan gambar sesuai state
#     if state == "start":
#         screen.blit(Press2Start, (0, 0))

#     elif state == "waiting":
#         screen.blit(Results, (0, 0))

#     elif state == "go":
#         screen.blit(PressQuickly, (0, 0))

#     elif state == "result":
#         screen.blit(Results, (0, 0))
#         draw_text(f"{reaction_time:.0f} ms", 450)

#     elif state == "jump":
#         screen.blit(PressQuickly, (0, 0))
#         draw_text("Jump Start!", 450)

#     pygame.display.update()

import pygame
import random
import time
import sys

# ---------------- SETUP ----------------
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Reaction Time Test")

# Load images
Press2Start = pygame.image.load("Asset/Press2Start.png")
Wait4Green = pygame.image.load("Asset/Wait4Green.png")
PressQuickly = pygame.image.load("Asset/PressQuickly.png")
Results = pygame.image.load("Asset/Results.png")
JumpStart = pygame.image.load("Asset/JumpStart.png")

# Font
font = pygame.font.Font("Asset/Anton-Regular.ttf", 120)
white = (255, 255, 255)

# Game variables
state = "start"
start_time = 0
reaction_time = 0
delay_time = 0

clock = pygame.time.Clock()


def draw_text(text, y):
    img = font.render(text, True, white)
    rect = img.get_rect(center=(960, y))
    screen.blit(img, rect)


# ---------------- GAME LOOP ----------------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if state == "start":
                state = "waiting"
                delay_time = time.time() + random.uniform(2, 5)

            elif state == "waiting":
                # Clicked too early
                state = "jump"

            elif state == "go":
                reaction_time = (time.time() - start_time) * 1000
                state = "result"

            elif state in ["result", "jump"]:
                state = "start"

    # --------- STATE LOGIC ---------
    if state == "waiting":
        if time.time() >= delay_time:
            state = "go"
            start_time = time.time()

    # --------- DRAWING ---------
    if state == "start":
        screen.blit(Press2Start, (0, 0))

    elif state == "waiting":
        screen.blit(Wait4Green, (0, 0))

    elif state == "go":
        screen.blit(PressQuickly, (0, 0))

    elif state == "result":
        screen.blit(Results, (0, 0))
        draw_text(f"{reaction_time:.0f} ms", 450)

    elif state == "jump":
        screen.blit(JumpStart, (0, 0))

    pygame.display.update()
