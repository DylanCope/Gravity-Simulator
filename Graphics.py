import pygame
from pygame import *
import sys

pygame.init()

BLACK    = (  0,   0,   0)
WHITE    = (255, 255, 255)
DARKGREY = ( 80,  80,  80)
GREY     = (210, 210, 210)
BLUE     = (  0,   0, 255)
GREEN    = (  0, 255,   0)
RED      = (255,   0,   0)
CYAN     = (0  , 255, 255)
ORANGE   = (255, 141,   0)

class Display:

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.screen = pygame.display.set_mode(
            self.dimensions
            # pygame.FULLSCREEN,
            # 32
        )
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.events = pygame.event.get()
        self.elapsedTime = 0
        self.running = True
        self.timeDistortionFactor = 1

    def setTimeDistortionFactor(self, t):
        self.timeDistortionFactor = t

    def isRunning(self):
        return self.running

    def refresh(self):
        self.screen.fill(BLACK)
        self.clock.tick(self.fps)

    def isEvent(self, type):
        for event in self.events:
            if event.type == type:
                return True

        return False

    def setDimensions(self, width, height):
        self.dimensions = (width, height)
        self.screen = pygame.display.set_mode(self.dimensions)

    def show(self):
        pygame.display.flip()
        self.elapsedTime += self.getDelta()

        self.events = pygame.event.get()

        #Event handling:
        # for event in self.events:
        #     if event.type == KEYDOWN or event.type == QUIT:
        #         if event.type == QUIT or event.type == K_ESCAPE:
        #             pygame.quit()
        #             sys.exit()
        #             break

    def stop(self):
        self.running = False

    def getDelta(self):
        return self.timeDistortionFactor * self.clock.get_time() / 1000.0

    def fill(self, colour):
        self.screen.fill(colour)

    def drawRect(self, x, y, width, height, colour, fill = 0):
        # print(x, y, x + width, y + height)
        pygame.draw.rect(self.screen, colour, [x, y, width, height], fill)

    def drawPixel(self, x, y, colour):
        pygame.draw.rect(self.screen, colour, [x, y, 2, 2], 0)
