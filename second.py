import pygame
import sys
pygame.init()

w, h = 600, 400
screen = pygame.display.set_mode((w, h))


white = (255, 255, 255)
red = (255, 0, 0)

r = 25
x = (w - r * 2) // 2
y = (h - r * 2) // 2

clock = pygame.time.Clock()

moving = True
while moving:
    screen.fill(white)

    pygame.draw.circle(screen, red, (x, y), r)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            moving = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - 20 >= 0:
                    y -= 20
            elif event.key == pygame.K_DOWN:
                if y + r//2 + 20 <= h:
                    y += 20
            elif event.key == pygame.K_LEFT:
                if x - 20 >= 0:
                    x -= 20
            elif event.key == pygame.K_RIGHT:
                if x + r//2 + 20 <= w:
                    x += 20

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()
