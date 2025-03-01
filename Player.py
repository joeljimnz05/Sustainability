import pygame
import random

class Player:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('images/turtle.png')
        self.__score = 0
        self.__ghost_score = 0
        self.N_PIXELS_TO_MOVE = 6

        self.playerWidth = 65
        self.playerHeight = 65
        self.x = random.randint(0, self.windowWidth - self.playerWidth)
        self.y = random.randint(0, self.windowHeight - self.playerHeight)
        self.image = pygame.transform.scale(self.image, (self.playerWidth, self.playerHeight))

        playerRect = self.image.get_rect()
        self.width = playerRect.width
        self.height = playerRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

    def update(self):
        keyPressedTuple = pygame.key.get_pressed()

        if keyPressedTuple[pygame.K_LEFT]:
            self.x -= self.N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_RIGHT]:
            self.x += self.N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_UP]:
            self.y -= self.N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_DOWN]:
            self.y += self.N_PIXELS_TO_MOVE

        self.rect = self.get_rect()

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def check_collide(self, other_character):
        if self.rect.colliderect(other_character.rect):
            return True
        else:
            return False







