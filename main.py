import pygame
import sys
import random
import snake


WIDTH, HEIGHT = 480, 480
GRIDSIZE = 20
GRID_WIDTH, GRID_HEIGHT = HEIGHT / GRIDSIZE, WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIMEGREEN = (50, 205, 50)
CRIMSON = (220, 20, 92)
BLUE = (0, 0, 255)


class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = LIMEGREEN

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
        new = (((current[0] + (x*GRIDSIZE)) % WIDTH),
               (current[1] + (y*GRIDSIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        move = snake.movement()
        if move == "UP":
            self.turn(UP)
        elif move == "DOWN":
            self.turn(DOWN)
        elif move == "LEFT":
            self.turn(LEFT)
        elif move == "RIGHT":
            self.turn(RIGHT)


class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = CRIMSON
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) *
                         GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

    def draw(self, surface):
        r = pygame.Rect(
            (self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)


def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, BLACK, r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, BLACK, rr)


def main():
    pygame.init()
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 30)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()
    score = 0
    running = True

    while(running):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
