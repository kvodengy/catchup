import pygame

FPS = pygame.time.Clock()
win_width = 700
win_height = 500
p_width = 100
p_height = 100

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Догонялки")

class Settings():
    def __init__(self, image, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Settings):
    def __init__(self, image, x, y, w, h, s):
        super().__init__(image, x, y, w, h)
        self.speed = s

    def move1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y<win_height-self.rect.height:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.x>0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x<win_width-self.rect.width:
            self.rect.x += self.speed

    def move2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y<win_height-self.rect.height:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.x>0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x<win_width-self.rect.width:
            self.rect.x += self.speed
        
    
bg = Settings("background.png", 0, 0, win_width, win_height)
p1 = Player("sprite1.png", 0, win_height//2, p_width, p_height, 5)
p2 = Player("sprite2.png", win_width-p_width, win_height//2, p_width, p_height, 5)
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    bg.draw()
    p1.move1()
    p1.draw()
    p2.move2()
    p2.draw()
    pygame.display.flip()
    FPS.tick(40)


#створи 2 спрайти та розмісти їх на сцені

#оброби подію «клік за кнопкою "Закрити вікно"»