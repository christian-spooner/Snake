import pygame
import sys
import random


WIDTH, HEIGHT = 480, 480
GRIDSIZE = 20
GRID_WIDTH, GRID_HEIGHT = HEIGHT / GRIDSIZE, WIDTH / GRIDSIZE


UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        current = self.get_head_position()
        x, y = self.direction
        new = (((current[0] + (x*GRIDSIZE)) % WIDTH), (current[1] + (y*GRIDSIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions(0, new)
            if len(self.positions) > self.length:
                self.postions.pop()

    def reset(self):
        pass

    def draw(self, surface):
        pass

    def handle_keys(self):
        pass


class food(object):
    def __init__(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (84, 194, 205), r)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = snake()
    food = food()

    score = 0
    while(True):
        clock.tick(10)
        screen.blit(surface, (0,0))
        pygame.display.update()

main()