import pgzrun


WIDTH=600
HEIGHT=600
TITLE="PAQUETA CRISPS"
gravity=1000

class Ball():
    def __init__(self):
        self.type="football"
        self.color="red"
        self.radius=50
        self.x=300
        self.y=300
        self.vx=80
        self.vy=0
        
    
        
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius, self.color)


object=Ball()
def draw():
    screen.fill("green")
    object.draw()





def update(dt): 
    uy=object.vy
    object.vy+=gravity * dt 
    object.y+=(uy + object.vy) * 0.5
    if object.y>=HEIGHT-object.radius:
        object.vy=object.vy * -0.9
        object.y=HEIGHT-object.radius
    object.x+=object.vx * dt
    if object.x>=WIDTH-object.radius:
        object.vx=object.vx* -1
        object.x=WIDTH-object.radius
    if object.x<object.radius:
        object.x=object.radius
        object.vx=object.vx *-1


    












































pgzrun.go()