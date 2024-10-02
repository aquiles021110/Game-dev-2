import pgzrun
TITLE='boing'
WIDTH=800
HEIGHT=500
gravity=2000
class ball:
  def __init__(self,x,y,radius,colour):
    self.x=x
    self.y=y
    self.vx=200
    self.vy=0
    self.radius=radius
    self.colour=colour
  def draw(self):
    screen.draw.filled_circle((self.x,self.y),self.radius,self.colour)
b1=ball(40,250,40,'red')    
b2=ball(200,250,20,'green')
b3=ball(600,300,10,'blue')
def draw():
  screen.clear()
  b1.draw()
  b2.draw()
  b3.draw()
def update(t):
  uy=b1.vy
  b1.vy+=gravity*t
  b1.y+=(uy+b1.vy)*0.5*t
  if b1.y>HEIGHT-b1.radius:
    b1.y=HEIGHT-b1.radius
    b1.vy=-b1.vy*0.9
  b1.x+=b1.vx*t
  if b1.x>WIDTH-b1.radius or b1.x<b1.radius:
    b1.vx=-b1.vx
#ball2
    uy=b2.vy
    b2.vy+=gravity*t
    b2.y+=(uy+b2.vy)*0.5*t
    if b2.y>HEIGHT-b2.radius:
        b2.y=HEIGHT-b2.radius
        b2.vy=-b2.vy*0.9
    b2.x+=b2.vx*t
    if b2.x>WIDTH-b2.radius or b2.x<b2.radius:
        b2.vx=-b2.vx
#ball3
    uy=b3.vy
  b3.vy+=gravity*t
  b3.y+=(uy+b3.vy)*0.5*t
  if b3.y>HEIGHT-b3.radius:
    b3.y=HEIGHT-b3.radius
    b3.vy=-b3.vy*0.9
  b3.x+=b3.vx*t
  if b3.x>WIDTH-b3.radius or b3.x<b3.radius:
    b3.vx=-b3.vx
def on_key_down(key):
  if key==keys.SPACE:
    b1.vy=-500
    b2.vy=-500
    b3.vy=-500
pgzrun.go()
