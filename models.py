import pygame
from pygame import Surface

class Square:
    def __init__(self,length):
        self.length = length
        self.surface = Surface((self.length,)*2)
        self.rect = self.surface.get_rect()
        self.direction = 'right'

    def _left(self):
        self.rect.left -= 1

    def _right(self):
        self.rect.left += 1

    def _up(self):
        self.rect.top -= 1

    def _down(self):
        self.rect.top += 1

    def direction(self,direction):
        self.direction = direction

    def update(self):
        if self.direction == 'left':
            self._left()     
        if self.direction == 'right':
            self._right()
        if self.direction == 'up':
            self._up()
        if self.direction == 'down':
            self._down()

# class body(Square):
#     super.__init__()