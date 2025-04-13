from pygame import *
from random import randint
font.init()
font2 = font.SysFont('Arial', 36)
font3 = font.SysFont('Arial', 60)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x:
            self.rect.y += self.speed
    
class Ball(GameSprite):
    def update(self):
        if self.rect.x - 50 < 0 or self.rect.x > win_width - 50:
            self.kill()
            ball = Ball('asteroid.png', 200, 200, 4, 50, 50) 

score_l = 0
score_r = 0
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill((200, 255, 255))
display.set_caption('Ping Pong')
background = transform.scale(image.load('749.jpg'), (win_width, win_height))
player_l = Player('ufo.png', 30, 200, 4, 50, 150)
player_r = Player('rocket.png', 520, 200, 4, 50, 150)
ball = Ball('asteroid.png', 200, 200, 4, 50, 50)
# ball = GameSprite('asteroid.png', 200, 200, 4, 50, 50)
win = font3.render('PLAYER1 WIN!', True, (66, 245, 114))
lose = font3.render('PLAYER2 WIN!', True, (66, 245, 114))


speed = 20

run = True
finish = False
clock = time.Clock()
FPS = 60
a = False
b = False
speed_x = 15
speed_y = 15
while run:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            run = False
        
            
    if finish != True:
        window.blit(background, (0, 0))
        window.fill((200, 255, 255))
        text = font2.render('Счёт:' + str(score_l) + str('/') + str(score_r), 1, (245, 66, 99))
        window.blit(text,(250, 50))
        
        player_l.update_l()
        player_l.reset()

        
        ball.update()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        
    if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
        speed_x *= -1
        speed_y *= 1
    if ball.rect.y > win_height - 50 or ball.rect.y + 50 < 0:
        speed_y *= -1
    if ball.rect.x < 0:
        score_r += 1
        ball.kill()
        ball = Ball('asteroid.png', 200, 200, 4, 50, 50)    
    if ball.rect.x > 700:
        score_l += 1
        ball.kill()
        ball = Ball('asteroid.png', 200, 200, 4, 50, 50)    
    if score_l >= 3 :
        finish = True
        a = True
    if score_r >= 3 :
        finish = True
        b = True
    if b == True:
        window.blit(lose, (160, 200))
        player_r.kill()
        player_l.kill()
    if a == True:
        window.blit(win, (160, 200))
        player_r.kill()
        player_l.kill()
    player_r.update_r()
    player_r.reset()
    display.update()
    clock.tick(FPS)  