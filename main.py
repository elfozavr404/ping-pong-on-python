from pygame import *
from time import time as time2

mixer.init()
font.init()

window = display.set_mode((900, 500))
display.set_caption('Ping pong')
window.fill((255, 255, 255))
FPS = 60
clock = time.Clock()
font = font.SysFont('Cooper', 80)
game = True
finish = False
timer_ = True
speed_x = 3
speed_y = 3
sc_1 = 0
sc_2 = 0
#Music here
win_1 = font.render('First Player Win :-D', True, (88, 166, 76))
win_2 = font.render('Second Player Win :-D', True, (88, 166, 76))
fake_loading = font.render('Loading...', True, (127, 46, 46))
first_time = time2()


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
        if keys_pressed[K_s] and self.rect.y < 410:
           self.rect.y += self.speed
        

    def update_arrows(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 410:
           self.rect.y += self.speed

ball = GameSprite(5, 'ed666327dd3ce274d94f2b3547155891.jpg', 405, 180, 100, 100)
player_1 = Player(7, 'ya.jpg', 5, 250, 80, 80)
player_2 = Player(7, 'ychtiel.jpg', 818, 250, 80, 80)
window.blit(fake_loading, (330, 200))

while game:
    if timer_ == True:
        last_time = time2()
        if last_time - first_time > 2:
            timer_ = False
    if finish == False and timer_ == False:
        window.fill((250, 250, 250))
        player_1.reset()
        player_1.update_ws()
        player_2.reset()
        player_2.update_arrows()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        score_1 = font.render(str(sc_1), True, (127, 46, 46))
        score_2 = font.render(str(sc_2), True, (127, 46, 46))
        window.blit(score_2, (495, 50))
        window.blit(score_1, (400, 50))
        if ball.rect.x < 75:
            finish = True
            window.blit(win_2, (160, 250))
        if ball.rect.x > 730:
            finish = True
            window.blit(win_1, (190, 250))
        if ball.rect.y > 400 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_1, ball):
            speed_x *= -1
            sc_1 += 1
        if  sprite.collide_rect(player_2, ball):
            speed_x *= -1
            sc_2 += 1
    for e in event.get():
        if e.type == QUIT:
           game = False


    display.update()
    clock.tick(FPS)
