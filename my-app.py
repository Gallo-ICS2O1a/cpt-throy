#Jump
jump_height = 15

#Gravity
gravity = 2.5

#Speed
speed = 5

#Movement
key_state = []
for _ in range(233):
    key_state.append(False)

#Player
player_pos = PVector(300, 300)
p_size = 40

def setup():
    size(1200, 600)

def draw():
    global player_pos
    global key_state
    global gravity
    background(0)
    
    #Player
    fill(0, 0, 255)
    ellipse(player_pos.x, player_pos.y, p_size, p_size)
    
    #gravity on player
    # player_pos.y += gravity
    
    #Movement
    if keyPressed:
        if key_state[37]:
            player_pos.x -= speed
        elif key_state[39]:
            player_pos.x += speed
            
        if key_state[38]:
            player_pos.y = player_pos.y - jump_height

            
def keyPressed():
    global key_state 
    key_state[keyCode] = True
    
def keyReleased():
    global key_state
    key_state[keyCode] = False

        
