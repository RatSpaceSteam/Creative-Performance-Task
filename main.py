import pygame, sys, random, math, time
start = time.time()
timer = 180
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("delivery.png")
        self.rect = self.image.get_rect(center = (500, 400))

    def move(self, deltax, deltay):
        if self.rect.top >= 0 and self.rect.bottom <= 800 and self.rect.left >= 100 and self.rect.right <= 900:
            self.rect.centery += deltay
            self.rect.centerx += deltax
        else:
            if deltay <= 0 and self.rect.bottom >= 800:
                self.rect.centery += deltay
                if self.rect.left >= 100 and self.rect.right <= 900:
                    self.rect.centerx += deltax
            if deltay >= 0 and self.rect.top <= 0:
                self.rect.centery += deltay
                if self.rect.left >= 100 and self.rect.right <= 900:
                    self.rect.centerx += deltax
            if deltax <= 0 and self.rect.right >= 900:
                self.rect.centerx += deltax
                if self.rect.top >= 0 and self.rect.bottom <= 800:
                    self.rect.centery += deltay
            if deltax >= 0 and self.rect.left <= 100:
                self.rect.centerx += deltax
                if self.rect.top >= 0 and self.rect.bottom <= 800:
                    self.rect.centery += deltay

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
    
    def conveyor(self, deltax, deltay):
        if self.rect.top >= 800:
            self.rect = self.image.get_rect(center = (500, 25))
            self.rect.centery += deltay
        else:
            self.rect.centery += deltay
        

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3 Minutes to Midnight")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

assignment = 50
you = Player()
line_one = Line(100)
line_two = Line(900)

font1 = pygame.font.Font('freesansbold.ttf', 17)
l1 = font1.render("Aliens have invaded Earth.", True, WHITE, BLACK)
l1Rect = l1.get_rect()
l1Rect.center = (500, 100)

font2 = pygame.font.Font('freesansbold.ttf', 17)
l2 = font2.render("All systems of nuclear missile defense have been disabled.", True, WHITE, BLACK)
l2Rect = l2.get_rect()
l2Rect.center = (500, 200)

font3 = pygame.font.Font('freesansbold.ttf', 17)
l3 = font3.render("Only trucks can deliver payloads towards their intended targets now.", True, WHITE, BLACK)
l3Rect = l3.get_rect()
l3Rect.center = (500, 300)

font4 = pygame.font.Font('freesansbold.ttf', 17)
l4 = font4.render("Your mission is to deliver a warhead to the largest ship in the invading fleet, which has recently made landfall.", True, WHITE, BLACK)
l4Rect = l4.get_rect()
l4Rect.center = (500, 400)

font5 = pygame.font.Font('freesansbold.ttf', 17)
l5 = font5.render("Are you brave enough to save humanity?", True, WHITE, BLACK)
l5Rect = l5.get_rect()
l5Rect.center = (500, 500)

font6 = pygame.font.Font('freesansbold.ttf', 17)
certainty = ""
input_active = True

begin = 0

road_obj = pygame.sprite.Group()
road_obj.add(line_one)
road_obj.add(line_two)
mid = pygame.sprite.Group()
for num in range(8):
    mid.add(Middle(assignment))
    assignment += 100
road_obj.add(mid)
road_obj.add(you)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ##credit to Rabbid76 on stackoverflow for how to make pygame inputs while the code is running##
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            certainty = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                certainty = certainty[:-1]
            else:
                certainty += event.unicode

    screen.fill(BLACK)
    if begin == 0:
        screen.blit(l1, l1Rect)
        screen.blit(l2, l2Rect)
        screen.blit(l3, l3Rect)
        screen.blit(l4, l4Rect)
        screen.blit(l5, l5Rect)
        choice = font6.render(certainty, True, WHITE, BLACK)
        choiceRect = choice.get_rect()
        choiceRect.center = (500, 600)
        screen.blit(choice, choiceRect)
        if (certainty == "Yes" or certainty == "yes") and input_active == False:
            begin += 1
        if (certainty == "No" or certainty == "no") and input_active == False:
            break
        
    if begin == 1:
        for middle in mid:
            if type(middle) == Middle:
                middle.conveyor(0, 10)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            you.move(0,-10)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            you.move(0,10)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            you.move(-10,0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            you.move(10,0)

        font = pygame.font.Font('freesansbold.ttf', 32)
        wangmiao = font.render(str(timer), True, WHITE, BLACK)
        wangmiaoRect = wangmiao.get_rect()
        wangmiaoRect.center = (500, 50)

        road_obj.draw(screen)
        screen.blit(wangmiao, wangmiaoRect)

        current = time.time()
        if (current - start) >= 1:
            timer -= 1
            start = time.time()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()