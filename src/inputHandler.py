import pygame

class InputHandler():
    """A class for handling all keyboard inputs. Passed as a reference to objects that need input"""
    def __init__(self):
        self.keyArray = []

    def update(self):
        """Update the handler's with information from input device"""
        self.keyArray = pygame.key.get_pressed()

    def getPressed(self):
        """Return the array of keyboard inputs"""
        return self.keyArray
        