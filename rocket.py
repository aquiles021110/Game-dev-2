import pygame.display
import pygame.event
import pygame.sprite
import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Space')
class rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('rocket.png')
        self.rect=self.image.get_rect()
    def update(self,press):
        if press[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if press[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if press[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if press[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>800:
            self.rect.right=800
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>600:
            self.rect.bottom=600
rocketgroup=pygame.sprite.Group()
r1=rocket()
rocketgroup.add(r1)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    press=pygame.key.get_pressed()
    r1.update(press)
    img=pygame.image.load('space.png')
    screen.blit(img,(0,0))
    rocketgroup.draw(screen)
    pygame.display.update()    
