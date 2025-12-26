from pygame import *

mixer.init()
font.init()

window = display.set_mode((900, 500))
display.set_caption('Ping pong')
window.fill((145, 222, 227))
FPS = 60
clock = time.Clock()
game = True
finish = False
#Music here

class GameSprite(sprite.Sprite):
    def __init__(self, speed, picture_name, x, y, width, height):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(picture_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_ws(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 480:
           self.rect.y += self.speed

    def update_arrows(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 480:
           self.rect.y += self.speed

player_1 = Player(7, 'koshak 1.png', 5, 250, 80, 80)
while game:
    window.fill((255, 255, 255, 0.92))
    if finish == False:
        player_1.reset()
        player_1.update_ws()




    for e in event.get():
        if e.type == QUIT:
           game = False


    display.update()
    clock.tick(FPS)