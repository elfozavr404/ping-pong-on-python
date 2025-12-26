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
speed_x = 3
speed_y = 3
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

ball = GameSprite(5, 'gde kirpich.png', 405, 180, 100, 100)
player_1 = Player(7, 'koshak 1.png', 5, 250, 80, 80)
player_2 = Player(7, 'koshak 2.png', 818, 250, 80, 80)

while game:
    window.fill((250, 250, 250))
    if finish == False:
        player_1.reset()
        player_1.update_ws()
        player_2.reset()
        player_2.update_arrows()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 400 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1
    for e in event.get():
        if e.type == QUIT:
           game = False


    display.update()
    clock.tick(FPS)
