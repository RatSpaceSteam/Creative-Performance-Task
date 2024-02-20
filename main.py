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
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, choice):
        super(Obstacle, self).__init__()
        if choice % 1 == 0:
                self.image = pygame.image.load("obstacles/hedgehog.png")
        if choice % 2 == 0:
                self.image = pygame.image.load("obstacles/boulder.png")
        self.rect = self.image.get_rect(center = (random.randint(100, 900), random.randint(0, 800)))

    def conveyor(self, deltax, deltay):
        if self.rect.top >= 800:
            self.rect = self.image.get_rect(center = (random.randint(100, 900), 25))
            self.rect.centery += deltay
        else:
            self.rect.centery += deltay


pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3 Minutes to Sunrise")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

assignment = 50
choice = 0
you = Player()
line_one = Line(100)
line_two = Line(900)

font1 = pygame.font.Font('freesansbold.ttf', 17)
font2 = pygame.font.Font('freesansbold.ttf', 32)

l0 = font2.render("Three Minutes to Sunrise", True, WHITE, BLACK)
l0Rect = l0.get_rect()
l0Rect.center = (500, 100)

l1 = font1.render("Aliens have invaded Earth.", True, WHITE, BLACK)
l1Rect = l1.get_rect()
l1Rect.center = (500, 200)

l2 = font1.render("All systems of nuclear missile defense have been disabled.", True, WHITE, BLACK)
l2Rect = l2.get_rect()
l2Rect.center = (500, 300)

l3 = font1.render("Only trucks can deliver payloads towards their intended targets now.", True, WHITE, BLACK)
l3Rect = l3.get_rect()
l3Rect.center = (500, 400)

l4 = font1.render("Your mission is to deliver a warhead to the largest ship in the invading fleet, which has recently made landfall.", True, WHITE, BLACK)
l4Rect = l4.get_rect()
l4Rect.center = (500, 500)

l5 = font1.render("Are you brave enough to save humanity?", True, WHITE, BLACK)
l5Rect = l5.get_rect()
l5Rect.center = (500, 600)

font6 = pygame.font.Font('freesansbold.ttf', 17)
certainty = ""
input_active = True

font2 = pygame.font.Font('freesansbold.ttf', 50)
lose = font2.render("GAME OVER", True, WHITE, BLACK)
loseRect = lose.get_rect()
loseRect.center = (500, 400)

font3 = pygame.font.Font('freesansbold.ttf', 17)
win = font3.render("You win!", True, WHITE, BLACK)
winRect = win.get_rect()
winRect.center = (500, 300)

win2 = font3.render("THE ALIENS HAVE BEEN DEFEATED!", True, WHITE, BLACK)
win2Rect = win2.get_rect()
win2Rect.center = (500, 400)

win3 = font3.render("HUMANITY IS SAVED!", True, WHITE, BLACK)
win3Rect = win3.get_rect()
win3Rect.center = (500, 500)
begin = 0
pts = 0

road_obj = pygame.sprite.Group()
road_rage = pygame.sprite.Group()
road_obj.add(line_one)
road_obj.add(line_two)
mid = pygame.sprite.Group()
for num in range(8):
    mid.add(Middle(assignment))
    assignment += 100
for num in range(6):
    road_rage.add(Obstacle(choice))
    choice += 1
road_obj.add(mid)
road_obj.add(you)
alive = True

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
        screen.blit(l0, l0Rect)
        screen.blit(l1, l1Rect)
        screen.blit(l2, l2Rect)
        screen.blit(l3, l3Rect)
        screen.blit(l4, l4Rect)
        screen.blit(l5, l5Rect)
        choice = font6.render(certainty, True, WHITE, BLACK)
        choiceRect = choice.get_rect()
        choiceRect.center = (500, 700)
        screen.blit(choice, choiceRect)
        if (certainty == "Yes" or certainty == "yes") and input_active == False:
            begin += 1
        if (certainty == "No" or certainty == "no") and input_active == False:
            break
        
    if begin == 1 and alive:
        for middle in mid:
            if type(middle) == Middle:
                middle.conveyor(0, 10)
        for bump in road_rage:
            if type(bump) == Obstacle:
                bump.conveyor(0, 10)

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
        road_rage.draw(screen)
        screen.blit(wangmiao, wangmiaoRect)

        current = time.time()
        if (current - start) >= 1:
            timer -= 1
            start = time.time()

    if timer == 0:
        begin += 2

    get_hit = pygame.sprite.spritecollide(you, road_rage, False)
    if get_hit:
        you.kill()

    if you not in road_obj:
        alive = False

    if not alive:
        screen.blit(lose, loseRect)
        timer = 180

    if begin == 3:
        screen.blit(win, winRect)
        screen.blit(win2, win2Rect)
        screen.blit(win3, win3Rect)
        timer = 180


    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()