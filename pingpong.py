from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
window = display.set_mode((700, 500))
speed_x = 3
speed_y = 3
balls = sprite.Group()
ball = GameSprite("images.jpg", 225, 325, 3, 60, 60)
balls.add(ball)
clock = time.Clock()
FPS = 60
players = sprite.Group()
p1 = Player1("raketka.png", 600, 155, 10, 30, 150)
p2 = Player2("raketka.png", 100, 155, 10, 30, 150)
players.add(p1)
players.add(p2)
game = True
finish = False
background = transform.scale(image.load("стол.jpeg"), (700, 500))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.groupcollide(balls, players, False, False):
            speed_x *=
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        p1.update()
        p1.reset()
        p2.update()
        p2.reset()
        clock.tick(FPS)
        display.update()
        