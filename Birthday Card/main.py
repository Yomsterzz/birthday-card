import pygame
import time
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Birthday Card!")

background_img = pygame.image.load("images/backgroundone.jpg")
img = pygame.transform.scale(background_img, (600,600))

while True:
    font = pygame.font.SysFont("Arial", 60)
    text = font.render("Happy", True, (0,0,0))
    text2 = font.render("Birthday!", True, (0,0,0))
    screen.fill("white")
    screen.blit(background_img, (0,0))
    screen.blit(text, (160,180))
    screen.blit(text2, (270,280))
    pygame.display.update()
    time.sleep(3)

    img2 = pygame.image.load("images/backgroundtwo.jpg")
    font2 = pygame.font.SysFont("Verdana", 30)
    text3 = font2.render("May your dreams come true!", True, (0,0,0))
    screen.fill("white")
    screen.blit(img2, (0,0))
    screen.blit(text3, (140,450))
    pygame.display.update()
    time.sleep(3)

    img3 = pygame.image.load("images/backgroundthree.jpg")
    screen.fill("white")
    screen.blit(img3, (0,0))
    pygame.display.update()
    time.sleep(3)