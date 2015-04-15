# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
ball_pos = [0, 0]
init_pos = [WIDTH / 2, HEIGHT / 2]
current_key = ' '
vel = [4,4]
time = 0
keyed= 0

# define event handlers
def tick():
    global time
    time = time + 1
    
def draw(canvas):
    if keyed ==1:
        canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    else:
        ball_pos[0] = init_pos[0] + time * vel[0]
        ball_pos[1] = init_pos[1] + time * vel[1]
        canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    if current_key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        canvas.draw_text(current_key, [10, 25], 20, "Red")  
        
def keydown(key):
    global current_key, keyed
    keyed=1
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel[0]
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel[0]
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel[1]
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel[1]  
      
    current_key = chr(key)

def keyup(key):
    global current_key, keyed
    current_key = ' '
    keyed = 0
    
# create frame 
f = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
t = simplegui.create_timer(100, tick)

# start frame
f.start()
t.start()