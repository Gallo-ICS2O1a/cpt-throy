class Ball():
    def __init__(self, x, y):
        global velocity
        global gravity
        self.pos = PVector(x, y)
        self.bsize = 40
        self.c = color(255, 0, 0)
   
    def display(self):
        fill(self.c)
        ellipse(self.pos.x, self.pos.y, self.bsize, self.bsize )
        

class Player():
    def __init__(self):
        self.pos = PVector(mouseX, 580)
        self.bsize = 40
        self.c = color(0, 255, 0)
        
    def collisionDetect(self, x1, y1, w1 , x2, y2, w2):
    
        self.r = w1/2
        self.a = x1 - x2
        self.b = y1 - y2
        self.c = sqrt(self.a**2 + self.b**2)
        
        if self.c <= self.r*2:
            return(True)
            
            
        else:
            return(False)

    
    def display(self):
        fill(self.c)
        ellipse(self.pos.x, self.pos.y, 40, 40)
              
    
score = 0
velocity = 0
gravity = 10
screen = 0

def setup():
    size(300, 600)
    
def draw():
    global score
    global gravity
    global velocity
    global screen
    background(0)
    
    if screen == 0:
        background(255)
        fill(255)
        rect(75, 100, 150, 100)
        textSize(32)
        fill(0)
        text("PLAY", 115, 160)
        if mouseX >= 75 and mouseX <= 225 and mouseY >= 100 and mouseY <= 200:
            if mousePressed == True:
                screen = 1
    
    
    if screen == 1:
        ball1 = Ball(0, 0)
        velocity += gravity
        ball1.pos.y += velocity
        
        if ball1.pos.y - 40 >= height:
            velocity = 0
            ball1.pos.y = 0
            gravity += velocity
            ball1.pos.y += velocity
            ball1.pos.x = random(0, width)
            score += 1
        
        ball1.display()
        player = Player()
        player.display()
        player.collisionDetect(player.pos.x, player.pos.y, player.bsize, ball1.pos.x, ball1.pos.y, ball1.bsize)
        
        if player.collisionDetect(player.pos.x, player.pos.y, player.bsize, ball1.pos.x, ball1.pos.y, ball1.bsize) == True:
            score = 0
            velocity = 0
            ball1.pos.y = 0
            gravity += velocity
            ball1.pos.y += velocity
            ball1.pos.x = random(0, width)
            
        #Scoreboard
        fill(0, 255, 0)
        textSize(30)
        text(score, 50, 50)
    
