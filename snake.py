import sys, pygame
pygame.init()

size = width, height = 400, 400
x = 0
y = 0
speed = 20
black = 0, 0, 0

#direction
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
direction = RIGHT

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

done = False
clock = pygame.time.Clock()

# Snake class #
class Snake:
    x = []
    y = []
    snakeWidth = 20
    direction = RIGHT
    length = 3

    def __init__(self, length):
        self.length = length
        for i in range(0, length):
            self.x.append(0)
            self.y.append(0)

    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == LEFT and self.x[0] >= speed:
            self.x[0] -= speed
        if self.direction == RIGHT and self.x[0] < width - self.snakeWidth:
            self.x[0] += speed
        if self.direction == UP and self.y[0] >= speed:
            self.y[0] -= speed
        if self.direction == DOWN and self.y[0] < height - self.snakeWidth:
            self.y[0] += speed

    def moveLeft(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def moveRight(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def moveUp(self):
        if self.direction != DOWN:
            self.direction = UP

    def moveDown(self):
        if self.direction != UP:
            self.direction = DOWN

    def draw(self, surface):
        for i in range(0, self.length):
            pygame.draw.rect(surface, (0,255,0), (self.x[i],self.y[i],self.snakeWidth,self.snakeWidth),0)

class Apple:
    x = 0
    y = 0
    appleWidth = 20

    def __init__(self):
        self.x = 60
        self.y = 60
        


snake = Snake(3)

while not done:
    clock.tick(15)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake.moveLeft()
    if keys[pygame.K_RIGHT]:
        snake.moveRight()
    if keys[pygame.K_UP]:
        snake.moveUp()
    if keys[pygame.K_DOWN]:
        snake.moveDown()

    screen.fill(black)

    #pygame.draw.rect(screen, (255,0,0), (x,y,snakeWidth,snakeWidth),0)
    snake.update()
    snake.draw(screen)

    pygame.display.flip()

pygame.quit()