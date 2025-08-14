import pygame
import sys
import os
import time

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("sily stuff question")
font = pygame.font.Font(None, 36)

def display_text(text):
    screen.fill((0, 0, 0))
    text_surf = font.render(text, True, (255, 255, 255))
    screen.blit(text_surf, (50, 150))
    pygame.display.flip()

running = True
ask = True
last_no_time = 0

while running:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y and ask:
                os.system("shutdown /s /t 1")

                running = False
            elif event.key == pygame.K_n and ask:
                last_no_time = current_time
                ask = False
            elif event.key == pygame.K_RETURN and (pygame.key.get_mods() & pygame.KMOD_CTRL) and (pygame.key.get_mods() & pygame.KMOD_ALT) and (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                running = False

    if ask:
        display_text("Do you give permission to do sily stuf? Press Y or N")
    else:
        display_text("No? I'll come back soon then...")
        if current_time - last_no_time >= 1:
            ask = True

pygame.quit()
sys.exit()
