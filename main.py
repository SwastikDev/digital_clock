import pygame
from sys import exit
import datetime
import pygame.mixer as mx
from time import sleep
pygame.init()
mx.init()
def beep():
    mx.music.load("beep.wav")
    mx.music.play()
    sleep(1)
icon = pygame.image.load("icon.ico")
screen = pygame.display.set_mode((430,300),pygame.FULLSCREEN)
pygame.display.set_caption("Digital Clock")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font_s1 = pygame.font.Font("font.ttf",200)
font_s2 = pygame.font.Font("font.ttf",50)
font_s3 = pygame.font.Font("font.ttf",50)
font_s4 = pygame.font.Font("font.ttf",50)
while True:
    now  = datetime.datetime.now()
    time_now = now.strftime("%I:%m")
    am_pm = now.strftime("%p")
    day = now.strftime("%a %d %B %y")
    sec = now.strftime("%S")
    time = font_s1.render(f"{time_now}",True,(22,198,12))
    am_pm_text = font_s2.render(f"{am_pm}",True,(22,198,12))
    down_text = font_s3.render(f"{day}",True,(22,198,12))
    sec_text = font_s3.render(f"{sec}",True,(22,198,12))
    screen.fill((0,0,0))
    screen.blit(time,(20,30))
    screen.blit(am_pm_text,(370,30))
    screen.blit(down_text,(15,230))
    screen.blit(sec_text,(370,125))
    beep()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(120)
    pygame.display.update()