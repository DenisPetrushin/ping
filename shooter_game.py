from pygame import *
from random import randint
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
img_emeny = "ufo.png"
fire_sound = mixer.Sound('fire.ogg')

font.init()
font2 = font.SysFont('Arial', 36)
font3 = font.SysFont('Arial', 60)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill() 
lost = 0
score = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
win_width = 700
win_height = 500
bullets = sprite.Group()
window = display.set_mode((win_width, win_height))
display.set_caption('Space Doom')
background = transform.scale(image.load('749.jpg'), (win_width, win_height))
player = Player('1234.jpg', 5, win_height - 100, 80, 100, 10)
monsters = sprite.Group()
win = font3.render('YOU WIN!', True, (255, 255, 255))
lose = font3.render('YOU LOSE!', True, (180, 0, 0))
for i in range(1,6):
    monster = Enemy(img_emeny, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)

speed = 10
run = True
finish = False
clock = time.Clock()
FPS = 60
a = False
b = False
while run:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()


            
    if finish != True:
        window.blit(background, (0, 0))
        text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text,(10, 50))
        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 70))
        player.update()
        
        player.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy("ufo.png", randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
        if sprite.spritecollide(player, monsters, False) or lost >= 3:
            finish = True
            b = True
        if score >= 10 :
            finish = True
            a = True
    if b == True:
        window.blit(lose, (250, 200))
    if a == True:
        window.blit(win, (250, 200))
    display.update()
    clock.tick(FPS)  