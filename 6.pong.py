# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 10:48:54 2016

@author: Martin
"""

# PONG!!!!!

import pygame, sys
import random


# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
PONG_TABLE_COL = (44, 162, 95)



SCREEN_SIZE = (500, 500) # window size is a 2-tuple measured in px

pygame.init() # initialize the pygame system

screen = pygame.display.set_mode(SCREEN_SIZE)

# Load images
tile = pygame.image.load("tile.png")

# Initialize the clock
clock = pygame.time.Clock()


#
#while True:
#	clock.tick(max_fps) # limit the refresh rate to a max of 60 cycles per second
#	
#	# Quit when the user closes the window
#	for event in pygame.event.get():
#		if event.type == pygame.QUIT: sys.exit()
#
#    screen.fill(PONG_TABLE_COL) # RGB white color tuple
#
# #   pygame.draw.circle(Surface, color, pos, radius, width = 0)
##    pygame.draw.circle(screen, (255, 255, 255), (150, 150), 20, width = 0)
#    pygame.draw.circle(screen, WHITE, (150, 150), 20, 0)
##	screen.blit(tile, (200, 100)) # Draw the tile on the screen
#
#	pygame.display.update() # Display what was drawn this turn
#


PADDLE_LEN = 100
PADDLE_WIDTH = 10
BALL_WIDTH = 15
BALL_SPEED_FACTOR = 1

FPS = 60
N_BALLS = 11
SPEED_ACC = 1.1
DIRECT_CHANGE = 0.5
PADDLE_SPEED = 8

def initial_screen():



    screen.fill(PONG_TABLE_COL) # RGB white color tuple

    screen.fill(PONG_TABLE_COL)
    myfont1 = pygame.font.SysFont("monospace", 60)
    myfont2 = pygame.font.SysFont("monospace", 20)
    myfont3 = pygame.font.SysFont("monospace", 20)
    myfont4 = pygame.font.SysFont("monospace", 20)

    # render text
    label1 = myfont1.render("bestPONG", 1, WHITE)
    label2 = myfont2.render("W/S - left player", 1, WHITE)
    label3 = myfont3.render("UP/DOWN - right player", 1, WHITE)
    label4 = myfont4.render("press SPACE to start", 1, WHITE)    
    
    screen.blit(label1, (200, 150))
    screen.blit(label2, (50, 300))
    screen.blit(label3, (50, 350))
    screen.blit(label4, (250, 450))

    pygame.display.update()   
    
    while(True):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
        
        space_pressed = pygame.key.get_pressed()[pygame.K_SPACE]

        if space_pressed:
            break


def drawing(ball_pos, paddle1_pos, paddle2_pos, score):
     
    screen.fill(PONG_TABLE_COL) # RGB white color tuple
    pygame.draw.circle(screen, WHITE, (round(ball_pos[0]), round(ball_pos[1])), BALL_WIDTH)
    pygame.draw.line(screen, WHITE, (PADDLE_WIDTH, 0), (PADDLE_WIDTH, SCREEN_SIZE[0]), 2)
    pygame.draw.line(screen, WHITE, (SCREEN_SIZE[1] - PADDLE_WIDTH, 0), 
                                     (SCREEN_SIZE[1] - PADDLE_WIDTH, SCREEN_SIZE[0]), 2)
    pygame.draw.rect(screen, WHITE, (0, paddle1_pos[0], PADDLE_WIDTH, PADDLE_LEN))
    pygame.draw.rect(screen, WHITE, (paddle2_pos[1], paddle2_pos[0], PADDLE_WIDTH, PADDLE_LEN))


    myfont = pygame.font.SysFont("monospace", 40)

    # render text
    label = myfont.render(str(score[0]) + ":" + str(score[1]), 1, WHITE)
    screen.blit(label, (200, 100))

    pygame.display.update()


def ball_update(score, ball_pos, ball_speed, paddle1_pos, paddle2_pos):

    # Ball position    
    ball_pos = (ball_pos[0] + ball_speed[0], ball_pos[1] + ball_speed[1])


    paddle1_top = paddle1_pos[0]
    paddle1_mid = paddle1_pos[0] + PADDLE_LEN / 2
    paddle1_bot = paddle1_pos[0] + PADDLE_LEN

    paddle2_top = paddle2_pos[0]
    paddle2_mid = paddle2_pos[0] + PADDLE_LEN / 2
    paddle2_bot = paddle2_pos[0] + PADDLE_LEN

    ball_hit_wall_left = (ball_pos[0] - BALL_WIDTH) < 0 - PADDLE_WIDTH
    ball_hit_wall_right = (ball_pos[0] + BALL_WIDTH) > SCREEN_SIZE[0] + PADDLE_WIDTH

    ball_left_edge_x = ball_pos[0] - BALL_WIDTH
    ball_right_edge_x = ball_pos[0] + BALL_WIDTH

    ball_hit_paddle_left = ball_left_edge_x <= paddle1_pos[1] and \
    ball_left_edge_x >= (paddle1_pos[1] + ball_speed[0]) and \
    (paddle1_top <= (ball_pos[1] + BALL_WIDTH) and paddle1_bot >= (ball_pos[1] + BALL_WIDTH)) 
    
    ball_hit_paddle_right = ball_right_edge_x >= paddle2_pos[1] and \
    ball_right_edge_x <= (paddle2_pos[1] + ball_speed[0]) and \
    (paddle2_top <= (ball_pos[1] + BALL_WIDTH) and paddle2_bot >= (ball_pos[1] + BALL_WIDTH))

    # Odraz od paddle    
    if  ball_hit_paddle_left or ball_hit_paddle_right:
        ball_speed = (-ball_speed[0] * SPEED_ACC, ball_speed[1] * SPEED_ACC)
        
        if ball_hit_paddle_left:
            ball_speed = (ball_speed[0], ball_speed[1] - DIRECT_CHANGE * (paddle1_mid - ball_pos[1]) / PADDLE_WIDTH)
        elif ball_hit_paddle_right:
            ball_speed = (ball_speed[0], ball_speed[1] - DIRECT_CHANGE * (paddle2_mid - ball_pos[1]) / PADDLE_WIDTH)
         
# DIRECT_CHANGE
         
    # Odraz od steny
    if (ball_pos[1] - BALL_WIDTH) < 0 or (ball_pos[1] + BALL_WIDTH) > SCREEN_SIZE[1]:
        ball_speed = (ball_speed[0], -ball_speed[1])       
        
    
    if ball_hit_wall_left or ball_hit_wall_right:
        ball_pos = (250, 250)
        ball_speed = (random.choice([-2.5, -2, -1.5, 1.5, 2, 2.5]), random.choice([-2, -1, 1, 2]))
        
        if ball_hit_wall_left:
            score = (score[0], score[1] + 1)
        else:
            score = (score[0] + 1, score[1])
        
    return score, ball_pos, ball_speed

def main():
    
    # initial state
    ball_pos = (250, 250)
    ball_speed = (3, 1)
    paddle1_pos = (250 - PADDLE_LEN / 2, PADDLE_WIDTH)
    paddle2_pos = (250 - PADDLE_LEN / 2, SCREEN_SIZE[1] - PADDLE_WIDTH)
    score = (0, 0)
    time = 0
    
    
    while True:
   
        clock.tick(FPS)    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if time == 0:
            initial_screen() 
    
        time += 1
                
        key_press = pygame.key.get_pressed()
             
        # Paddle position
        if key_press[pygame.K_w] == 1 and (paddle1_pos[0]) >= 0:
            paddle1_pos = (paddle1_pos[0] - PADDLE_SPEED, paddle1_pos[1])
        elif key_press[pygame.K_s] == 1 and (paddle1_pos[0]) <= SCREEN_SIZE[1] - PADDLE_LEN:
            paddle1_pos = (paddle1_pos[0] + PADDLE_SPEED, paddle1_pos[1])        
        
        if key_press[pygame.K_UP] == 1 and (paddle2_pos[0]) >= 0:
            paddle2_pos = (paddle2_pos[0] - PADDLE_SPEED, paddle2_pos[1])            
        elif key_press[pygame.K_DOWN] == 1 and (paddle2_pos[0]) <= SCREEN_SIZE[1] - PADDLE_LEN:
            paddle2_pos = (paddle2_pos[0] + PADDLE_SPEED, paddle2_pos[1])   
        
            
        [score, ball_pos, ball_speed] = ball_update(score, ball_pos, ball_speed, paddle1_pos, paddle2_pos)            
        
        if score[0] >= N_BALLS or score[1] >= N_BALLS:
            
            if score[0] >= N_BALLS:
                win_msg = ("Left Won")
            elif score[1] >= N_BALLS:
                win_msg = ("Right Won")
                
            screen.fill(PONG_TABLE_COL)
            myfont1 = pygame.font.SysFont("monospace", 60)
            myfont2 = pygame.font.SysFont("monospace", 40)

            # render text
            label1 = myfont1.render(win_msg, 1, WHITE)
            label2 = myfont2.render(str(score[0]) + ":" + str(score[1]), 1, WHITE)
            screen.blit(label1, (150, 200))
            screen.blit(label2, (200, 100))
        
            pygame.display.update()
            
            pygame.quit()
            sys.exit()                      
                
        else:
            drawing(ball_pos, paddle1_pos, paddle2_pos, score)    
        
    
main()



    
    
    
    