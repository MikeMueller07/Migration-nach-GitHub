import os

import pygame

import random

class Settings:
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 400
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")

class Banane():
    def __init__(self):
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "banane.jpeg")).convert()
        self.image.set_colorkey("white")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)
        self.speedx = random.randint(-10, 10)
        self.speedy = random.randint(-10, 10)

    def update(self):
        self.rect = self.rect.move(self.speedx, self.speedy)
        if self.rect.left < 0 or self.rect.right > Settings.WINDOW_WIDTH:
            self.speedx *= -1
        if self.rect.top < 0 or self.rect.bottom > Settings.WINDOW_HEIGHT:
            self.speedy *= -1

class Affe():
    def __init__(self):
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "affe.jpeg")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, Settings.WINDOW_WIDTH - 50), random.randint(50, Settings.WINDOW_HEIGHT - 50))

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()

    screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    pygame.display.set_caption("leck eier")
    clock = pygame.time.Clock()

    counter = 0
    banane_list = []
    affe_list = []
    for _ in range(0,5):
        affe_list.append(Affe())

    background_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "dschungel.jpeg")).convert()
    background_image = pygame.transform.scale(background_image, (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        counter += 1

        if counter == 90:
            counter = 0
            banane_list.append(Banane()) 

        screen.blit(background_image, (0, 0))

        for affe in affe_list:
            screen.blit(affe.image, affe.rect)

        for banane in banane_list:
            banane.update()
            screen.blit(banane.image, banane.rect)
            for affe in affe_list:
                if banane.rect.colliderect(affe.rect):
                    banane_list.remove(banane)

        pygame.display.flip()
        clock.tick(Settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
