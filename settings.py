import pygame
import os
import random
import time
from difficult import diff

#const

fps = 60
screen_width = 600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
white = (255, 255, 255)
scroll_speed = 3
pipe_gap = 200
pipe_frequency = 1500
score = 0
ground_x1 = 0
bg_x1 = 0
bg_x2 = 0
bg_x3 = 0
fog_x1 = 5000
difficulty = 1

#img

bg1 = pygame.image.load('img/bg1.png').convert_alpha()
bg2 = pygame.image.load('img/bg2.png').convert_alpha()
bg3 = pygame.image.load('img/bg3.png').convert_alpha()
fog = pygame.image.load('img/fog.png').convert_alpha()
ground1_img = pygame.image.load('img/ground1.png').convert_alpha()
restart_img = pygame.image.load('img/restart.png').convert_alpha()
play_img = pygame.image.load('img/start.png').convert_alpha()
reset_img = pygame.image.load('img/reset.png').convert_alpha()
icon = pygame.image.load('img/bird1.png')
pygame.display.set_caption('Flappy Woodland')
pygame.display.set_icon(icon)