import pygame
from pygame import Vector2

class Text():
    """
    A class for text objects that need to be drawn on screen
    Takes in a label, draw(value) writes "[label] [value]" to screen
    """
    
    def __init__(self, label, screen, font, color, position=Vector2(0,0)):
        self.label = label
        self.screen = screen
        self.font = font
        self.position = position
        self.color = color
        self.text = self.font.render(label + "  ", True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.centerx = position.x
        self.textRect.centery = position.y
    
    def draw(self, value=""):
        if type(value) == float:
            value = int(value)
        self.text = self.font.render(f"{self.label} {value}", True, self.color)
        self.screen.blit(self.text, self.textRect)

    def setPosition(self, pos):
        assert type(pos) == Vector2, "Position must be of type Vector2"
        self.position = pos
        self.textRect.centerx = pos.x
        self.textRect.centery = pos.y

    def setLabel(self, label):
        assert type(label) == str, "label must be a string"
        self.label = label
        self.text = self.font.render(label + "  ", True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.centerx = self.position.x
        self.textRect.centery = self.position.y