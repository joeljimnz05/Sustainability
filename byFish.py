import pygame
import random

class byFish:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('images/byFish.png')
        self.xSpeed = 10
        self.chickenWidth = 50
        self.chickenHeight = 50

        self.x = random.randint(0, self.windowWidth - self.chickenWidth)
        self.y = random.randint(0,  self.windowHeight - self.chickenHeight)
        self.image = pygame.transform.scale(self.image, (self.chickenWidth, self.chickenHeight))

        fishRect = self.image.get_rect()
        self.width = fishRect.width
        self.height = fishRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):
        if (self.x < 0) or (self.x + self.chickenWidth >= self.windowWidth):
            self.xSpeed = -self.xSpeed

        self.x = self.x + self.xSpeed

        self.rect = self.get_rect()






