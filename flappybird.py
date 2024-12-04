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
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(1,4):
            image=pygame.image.load(f'bird{i}.png')
            self.images.append(image)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def update(self):
        if gameover==False:
            self.counter+=1
            if self.counter>5:
                self.counter=0
                self.index+=1
                if self.index>=3:
                    self.index=0
                self.image=self.images[self.index]
while True:
    screen.blit(sky,(0,0))
    screen.blit(ground,(scroll,650))
    if gameover==False:
       scroll-=5
       if scroll<-35:
           scroll=0
    pygame.display.update()
    
