import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,900))
pygame.display.set_caption('Birb')
sky=pygame.image.load('skybird.png')
ground=pygame.image.load('floor.png')
restartbutton=pygame.image.load('restarrt.png')
scroll=0
pipediff=150
gameover=False
flying=False
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(1,4):
            image=pygame.image.load(f'bird{i}.png')
            self.images.append(image)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.velocity=0
        self.click=False
    def update(self):
        if flying==True:
            #self.velocity+=0.5
            if self.velocity>8:
                self.velocity=8
            #if self.rect.bottom<650:
              # self.rect.y+=self.velocity
        if gameover==False:
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                 self.click=True
                 self.velocity=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.click=False
            self.counter+=1
            if self.counter>5:
                self.counter=0
                self.index+=1
                if self.index>=3:
                    self.index=0
                self.image=self.images[self.index]
bgroup=pygame.sprite.Group()
flappy=bird(30,200)
bgroup.add(flappy)
while True:
    screen.blit(sky,(0,0))
    screen.blit(ground,(scroll,650))
    bgroup.draw(screen)
    bgroup.update()
    if gameover==False:
       scroll-=5
       if scroll<-35:
           scroll=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and gameover==False and flying==False:
            flying=True
    pygame.display.update()
    
