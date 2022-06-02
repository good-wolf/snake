import pygame
from pygame import Surface

class Square:
    def __init__(self,length):
        self.length = length
        self.surface = Surface((self.length,)*2)
        self.rect = self.surface.get_rect()
        

    def _left(self):
        self.rect.left -= 1

    def _right(self):
        self.rect.left += 1

    def _up(self):
        self.rect.top -= 1

    def _down(self):
        self.rect.top += 1

    def update(self):
        pass

# class body(Square):
#     super.__init__()