from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
 
 
font2 = font.Font(None, 36)
 
 

 
 

img_back = "road.webp"
img_car = "car.png"
img_obstacle = "rustycar.png"
score = 0
lost = 0 

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
 
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
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed


 
  
class Obstacle(GameSprite):
   def update(self):
       self.rect.y += self.speed
       global lost
       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y = 0
           lost = lost + 1  


win_width = 1000
win_height = 900
display.set_caption("Final Race!")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

car = Player(img_car, 5, win_height - 200, 80, 150, 15)

obstacles = sprite.Group()
for i in range(1, 9):
   obstacle = Obstacle(img_obstacle, randint(1, win_width - 80), -40, 80, 80, randint(7, 20))
   obstacles.add(obstacle)

finish = False

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
           run = False

    if not finish:
        window.blit(background,(0,0))
    
    
        car.update()
        obstacles.update()
    
    
        car.reset()
        obstacles.draw(window)


        # collides = sprite.spritecollide(car, obstacles, True, True)
        # for c in collides:
        #     score = score + 1
        #     obstacle = obstacle(img_obstacle, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
        #     obstacles.add(obstacle)
    

        if sprite.spritecollide(car, obstacles, True):
            finish = True
            window.blit(lose, (200, 200))
    
    
        text_lose = font2.render("Проехал препятствий: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
    
    
        display.update()
    
    
    
        # time.delay(3000)
        # for i in range(1, 6):
        #     obstacle = Obstacle(img_obstacle, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
        #     obstacles.add(obstacle)
        
    
    
    time.delay(50)

