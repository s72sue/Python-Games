# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PLAYER_SIDE = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vel_x = random.randrange(2, 4)
    vel_y = random.randrange(1, 3)  
  
    if ( direction == RIGHT ):
       ball_vel = [vel_x, -vel_y]  
    if ( direction == LEFT ):   
       ball_vel = [-vel_x, -vel_y]  
 
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, PLAYER_SIDE  # these are numbers
    global score1, score2  # these are ints
    
    score1, score2 = 0, 0
    paddle1_pos = (HEIGHT - PAD_HEIGHT)/2
    paddle2_pos = (HEIGHT - PAD_HEIGHT)/2
    paddle1_vel = paddle2_vel = 0
    
    PLAYER_SIDE = not PLAYER_SIDE
    spawn_ball(PLAYER_SIDE)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball postion
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    # update horizontal velocity for bouncing from side walls
    # left wall case
    if ( ball_pos[0] <= BALL_RADIUS + PAD_WIDTH ):
        if ( paddle1_pos <= ball_pos[1] <= (paddle1_pos+PAD_HEIGHT) ):
            ball_vel[0] = - ball_vel[0]
        else:    
            spawn_ball(RIGHT)
            score2 += 1
    
    # right wall case               
    if ( ball_pos[0] >=  WIDTH - (BALL_RADIUS + PAD_WIDTH) ):   
        if ( paddle2_pos <= ball_pos[1] <= (paddle2_pos+PAD_HEIGHT) ):
            ball_vel[0] = - ball_vel[0]
        else:   
            spawn_ball(LEFT)
            score1 += 1
        
    # update horizontal velocity for bouncing from top and bottom walls
    if ( ball_pos[1] <= BALL_RADIUS or ball_pos[1] >=  HEIGHT - BALL_RADIUS ) :
        ball_vel[1] = - ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos_temp = paddle1_pos + paddle1_vel
    paddle2_pos_temp = paddle2_pos + paddle2_vel
    if ( paddle1_pos_temp >= 0 and paddle1_pos_temp <= HEIGHT - PAD_HEIGHT ):
        paddle1_pos = paddle1_pos_temp
    if ( paddle2_pos_temp >= 0 and paddle2_pos_temp <= HEIGHT - PAD_HEIGHT ):
        paddle2_pos = paddle2_pos_temp
    
    # draw paddles
    canvas.draw_line([PAD_WIDTH/2, paddle1_pos],[PAD_WIDTH/2, paddle1_pos+PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos],[WIDTH- PAD_WIDTH/2, paddle2_pos+PAD_HEIGHT], PAD_WIDTH, "White")
    
    # draw scores
    canvas.draw_text( str(score1), (185, 40), 40, "White")
    canvas.draw_text( str(score2), (400, 40), 40, "White")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    # constant velocity
    vel = 4     
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel   
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0   
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0  

        
def restart_handler():
    new_game()
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart_handler, 100)


# start frame
new_game()
frame.start()

