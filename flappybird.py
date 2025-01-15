import pygame
import random
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('Birb')
sky=pygame.image.load('skybird.png')
ground=pygame.image.load('floor.png')
restartbutton=pygame.image.load('restarrt.png')
scroll=0
pipediff=150
gameover=False
flying=False
pipefreq=2500
lastpipe=pygame.time.get_ticks()-pipefreq
passing=False
score=0
font=pygame.font.SysFont('Arial',30)
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
            self.velocity+=0.5
            if self.velocity>8:
                self.velocity=8
            if self.rect.bottom<650:
               self.rect.y+=self.velocity
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
class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('pipe.png')
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-pipediff/2]
        elif pos==-1:
            self.rect.topleft=[x,y+pipediff/2]
    def update(self):
        self.rect.x-=3
        if self.rect.right<0:
            self.kill()
bgroup=pygame.sprite.Group()
pipeg=pygame.sprite.Group()
flappy=bird(30,200)
bgroup.add(flappy)
while True:
    clock.tick(60)
    screen.blit(sky,(0,0))
    if flappy.rect.bottom>=650:
        gameover=True
        flying=False
    bgroup.draw(screen)
    pipeg.draw(screen)
    screen.blit(ground,(scroll,650))
    bgroup.update()
    if len(pipeg)>0:
        if bgroup.sprites()[0].rect.left>pipeg.sprites()[0].rect.left \
        and bgroup.sprites()[0].rect.right>pipeg.sprites()[0].rect.right \
        and passing==False:
            passing=True
        if passing==True and bgroup.sprites()[0].rect.left>pipeg.sprites()[0].rect.right:
            score+=1
            passing=False
    scoretxt=font.render(str(score),True,'black')
    screen.blit(scoretxt,(100,50))
    if pygame.sprite.groupcollide(bgroup,pipeg,False,False) or flappy.rect.top<0:
        gameover=True
    if gameover==False:
       timenow=pygame.time.get_ticks()
       scroll-=5
       if timenow-lastpipe>pipefreq:
        pipeh=random.randint(-100,100)
        bottompipe=pipe(800,450+pipeh,-1)
        toppipe=pipe(800,450+pipeh,1)
        pipeg.add(bottompipe)
        pipeg.add(toppipe)
        lastpipe=timenow
       pipeg.update()
       if scroll<-35:
           scroll=0
    if gameover==True:
        screen.blit(restartbutton,(400,400))
        if pygame.mouse.get_pressed()[0]==0:
            gameover=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and gameover==False and flying==False:
            flying=True
    pygame.display.update()
    
