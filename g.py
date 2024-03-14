import pygame
import sys
import math
from time import localtime

pygame.init()

width, height = 300, 300
screen = pygame.display.set_mode((width, height))

mickey_img = pygame.image.load("background.png")
mickey_img = pygame.transform.scale(mickey_img, (300, 300))

minute_hand_img = pygame.image.load("minute.png")
minute_hand_img = pygame.transform.scale(minute_hand_img, (160, 65))
second_hand_img = pygame.image.load("second.png")
second_hand_img = pygame.transform.scale(second_hand_img, (220, 65))

def draw_clock(m, s):
    screen.fill((255, 255, 255))

    screen.blit(mickey_img, (width//2 - mickey_img.get_width()//2, height//2 - mickey_img.get_height()//2))

    rotated_minute_hand = pygame.transform.rotate(minute_hand_img, -(m * 6))
    screen.blit(rotated_minute_hand, (width//2 - rotated_minute_hand.get_width()//2, height//2 - rotated_minute_hand.get_height()//2))

    rotated_second_hand = pygame.transform.rotate(second_hand_img, -(s * 6))
    screen.blit(rotated_second_hand, (width//2 - rotated_second_hand.get_width()//2, height//2 - rotated_second_hand.get_height()//2))

    pygame.display.flip()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = localtime()
    minute, second = current_time.tm_min, current_time.tm_sec


    draw_clock(minute, second)


    clock.tick(60)
