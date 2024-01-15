from assets import *
import pygame
import random

WIDTH = 800            # Constant Variables
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()         # Initialize module
pygame.mixer.init()   # Initialize sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create Window
pygame.display.set_caption("Shooter Game")  # Title Window
clock = pygame.time.Clock()   # Velocity Game


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/player.png").convert()  # Load Player Image
        self.image.set_colorkey(BLACK)  # Sets color as transparent in the image
        self.rect = self.image.get_rect()  # Gets rectangle for image
        self.rect.centerx = WIDTH // 2  # Sets initial position on X
        self.rect.bottom = HEIGHT - 10  # Sets initial position down Y
        self.speed_x = 0  # Sets speed for X

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()      # List of keys pressed
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:             # Adjust our ship on the window when we touch our keys
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/meteorGrey_med1.png").convert()   # Load Meteor Medium image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)         # Random position to object
        self.speedy = random.randrange(1, 10)             # Random speed X for object
        self.speedx = random.randrange(-5, 5)


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top > HEIGHT + 5 or self.rect.left < -10 or self.rect.right > WIDTH + 5:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)  # Random position to object
            self.speedy = random.randrange(1, 10)


players_list = pygame.sprite.Group()    # Keep all of players
meteorites_list = pygame.sprite.Group()
background = pygame.image.load("../assets/background_1.png").convert()

for i in range(10):
    meteor = Meteor()
    players_list.add(meteor)
    meteorites_list.add(meteor)

player = Player()
players_list.add(player)     # Keep the player on our list

running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():    # We call our window
        if event.type == pygame.QUIT:
            running = False             # Stop running the game
    players_list.update()                # Update all players when the game ends

    screen.blit(background, [0, 0])                  # Sets all the window with the color

    players_list.draw(screen)            # Show our images on screen

    pygame.display.flip()               # Update our screen after all
pygame.quit()

