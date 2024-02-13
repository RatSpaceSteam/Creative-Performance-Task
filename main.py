import pygame, sys, random, math, time
#start = time.time()
#print("Start time", start)
#while True:
    #current = time.time()
    #if (current - start) == 1:
        #print("1 seconds")
        #start = time.time()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("delivery.png")
        self.rect = self.image.get_rect(center = (500, 400))

    def move(self, deltax, deltay):
        if self.rect.top > 0 and self.rect.bottom < 800 and self.rect.left > 100 and self.rect.right < 1000:
            self.rect.centery += deltay
            self.rect.centerx += deltax
        else:
            if deltay <= 0 and self.rect.bottom >= 800:
                self.rect.centery += deltay
            if deltay >= 0 and self.rect.top <= 100:
                self.rect.centery += deltay
            if deltax <= 0 and self.rect.right >= 900:
                self.rect.centerx += deltax
            if deltax >= 0 and self.rect.left <= 100:
                self.rect.centerx += deltax

class Line(pygame.sprite.Sprite):
    def __init__(self, x):
        super(Line, self).__init__()
        self.image = pygame.Surface((15,800), pygame.SRCALPHA, 32)
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (x, 400))

class Middle(pygame.sprite.Sprite):
    def __init__(self, y):
        super(Middle, self).__init__()
        self.image = pygame.Surface((15,50), pygame.SRCALPHA, 32)
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (500, y))

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nuclear Hero")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

assignment = 50
you = Player()
line_one = Line(100)
line_two = Line(900)

road_obj = pygame.sprite.Group()
road_obj.add(line_one)
road_obj.add(line_two)
for num in range(8):
    road_obj.add(Middle(assignment))
    assignment += 100
road_obj.add(you)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        you.move(0,-5)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        you.move(0,5)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        you.move(-5,0)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        you.move(5,0)

    road_obj.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()