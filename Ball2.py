import simplegui
import random

# Initialize globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [0, 0]
    ball_vel= [0, 0]
         
    if direction == RIGHT:
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        ball_vel = [random.randrange(2, 4), -random.randrange(1, 3)]
    if direction == LEFT:
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        ball_vel = [-random.randrange(2, 4), -random.randrange(1, 3)]

def spawn_paddle():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    paddle1_pos = [[PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT], [PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]] 
    paddle2_pos = [[WIDTH - PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]] 
    paddle1_vel = 0
    paddle2_vel = 0

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    if score1 >= score2:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)
    spawn_paddle()
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    #draw the scores
    canvas.draw_text(str(score1), [WIDTH / 4, 25], 24, 'White')
    canvas.draw_text(str(score2), [WIDTH / 1.33, 25], 24, 'White')
    
    #draw the ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    #draw paddle 1
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, "Blue")
  
    #draw paddle 2
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, "Red")
  
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= (WIDTH-1) - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]  
    elif ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
      
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -12
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 12
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -12
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 12

def keyup(key):
    global paddle1_vel, paddle2_vel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game,200)

# start frame
new_game()
frame.start()