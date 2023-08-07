import pygame
import neat
import time 
import os
import random 

WIN_WIDTH = 600
WIN_HEIGHT =800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("./imgs","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("./imgs","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("./imgs","bird3.png")))]
PIPE_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("./imgs","pipe.png")))]
BASE_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("./imgs","base.png")))]
BD_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("./imgs","bg.png")))]


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT = 20
    ANIMATION_TIME = 5

    def _init(self,x,y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height =self.y
        self.image_count = self.IMGS[0]


    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):