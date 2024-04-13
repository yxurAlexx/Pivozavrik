import pygame
import random
import sys
from pygame import mixer
pygame.init()
def finish():
    pygame.quit()
    sys.exit()

class Player:
    Jump_SOUND = pygame.mixer.Sound('piu.wav')
    Jump_SOUND.set_volume(0.2)
    def __init__(self, speed = 1,  controll_type = "p1"):
        self.touch_ground = False
        self.gravity = 0
        # self.sprite = pygame.image.load("kubik.png")
        # self.surf = pygame.transform.scale(self.sprite, (40, 40))
        self.rect = pygame.Rect(40, 500, 20, 20)
        self.score = 0
        self.speed = speed
        self.scoreFont = pygame.font.SysFont("Times New Roman", 30)
        self.controll_type = controll_type
    def draw(self, screen):
        # screen.blit(self.surf, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        text = self.scoreFont.render(str(self.score), True, (0, 0, 0))
        screen.blit(text,(20, 20))
    def move(self, keys):
        if self.controll_type == "p1":
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if keys[pygame.K_UP] and self.touch_ground:
                self.Jump_SOUND.play()
                self.rect.y += 1
                self.gravity = -15
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed

        if self.controll_type == "p2":

            if keys[pygame.K_d]:
                self.rect.x += self.speed
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
        self.rect.y += self.gravity
        if self.rect.colliderect(ground):
            self.touch_ground = True
            self.rect.bottom = ground.top + 1
            self.gravity = 0
        else:
            self.touch_ground = False
        self.gravity += world_gravity
class Parctical:
    def __init__(self):
        self.speed = random.randint(1,3)
        self.rect = pygame.Rect(850, random.randint(500,530), random.randint(10,20), 100)
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

    def move(self):
        self.rect.x -= self.speed


screen = pygame.display.set_mode((800, 600))
fps_controller = pygame.time.Clock()
FPS = 30
world_gravity = 1
ground = pygame.Rect(0, 550, 800, 200)
parcticals = []
lastSpawn = pygame.time.get_ticks()
player1 = Player()
pygame.mixer.music.load('background.mp3')
print("music started playing....")
mixer.music.set_volume(0.1)
pygame.mixer.music.play()
while True:
    events = pygame.event.get()
    now = pygame.time.get_ticks()
    for event in events:
        if event.type == pygame.QUIT:
            finish()
    keys = pygame.key.get_pressed()  # Checking pressed keys
    player1.move(keys)
    if now - lastSpawn >= 5000:
        lastSpawn = now
        parcticals.append(Parctical())
    screen.fill((255, 255, 255))
    for p in parcticals:
        p.move()
        p.draw(screen)
        if p.rect.x <= -100:
            player1.score += 1

    parcticals = [p for p in parcticals if p.rect.x > -100]
    pygame.draw.rect(screen, (0, 0, 0), ground)
    player1.draw(screen)
    if player1.rect.collidelist(parcticals) != -1:
        Die_SOUND = pygame.mixer.Sound('game_over.wav')
        Die_SOUND.set_volume(0.2)
        Die_SOUND.play()
        player1.score = 0
        player1.rect.x = 40
        player1.rect.y = 500
        player1.gravity = 0
        lastSpawn = now
        parcticals.clear()
    pygame.display.update()
    fps_controller.tick(FPS)

