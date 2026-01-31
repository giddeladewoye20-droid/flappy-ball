import pgzrun


WIDTH=600
HEIGHT=600
TITLE="PAQUETA CRISPS"

class Ball():
    def __init__(self):
        self.type="football"
        self.color="red"
        self.radius=100
        self.x=300
        self.y=300
    
        
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius, self.color)
     

object=Ball()
def draw():
    screen.fill("green")
    object.draw()





def update():
    pass










































pgzrun.go()