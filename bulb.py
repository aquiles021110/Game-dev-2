import pygame
pygame.init()
screen=pygame.display.set_mode((200,200))
screen.fill('white')
pygame.display.update()
while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit()
  event=pygame.event.poll()
  if event.type==pygame.MOUSEBUTTONDOWN:
    img1=pygame.image.load('Image20241009152322.jpg')
    screen.blit(img1,(0,0))
    pygame.display.update()
  elif event.type==pygame.MOUSEBUTTONUP:
    img2=pygame.image.load('Image20241009152327.jpg')
    screen.blit(img2,(0,0))
    pygame.display.update()
      
