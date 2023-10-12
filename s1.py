from pygame import *

class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

#Игровая сцена:
back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-Понг")
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

#Создание мяча:
ball = Player('png-clipart-football-football.png', 200, 200, 65, 40, 40)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            window.fill(back)
    if finish != True:
        window.fill(back)
        ball.update() 
        ball.reset()

    display.update()
    clock.tick(FPS)
