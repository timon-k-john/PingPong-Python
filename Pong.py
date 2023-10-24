#Pong testing

import pygame as P
import sys
import random

#initialting and creating window
P.init()
pong = P.display.set_mode((600,400))
P.display.set_caption("Pong")
clock = P.time.Clock()

#x and y coordinates
b_x = 300
b_y = 200

dash1_x = 15
dash1_y = 180
dash1_v = 5

dash2_x = 580
dash2_y = 180
dash2_v = 5

#directions
left = True
right = False
up = False
down = False
d_down = True
d_up = True

a = b = 0

#score
scr1 = 0
scr2 = 0

multi = False

#game over screen
def gameover():
    global scr1,scr2,multi

    font_1 = P.font.Font('freesansbold.ttf', 64)
    text_1 = font_1.render('PONG', True, (255,255,255))# ,(6,288,288)) 
    textRect_1 = text_1.get_rect()
    textRect_1.center = (300,100)

    pong.blit(text_1, textRect_1)

    if scr1 == scr2 == 0:
        font_6 = P.font.Font('freesansbold.ttf', 25)
        text_6 = font_6.render("1. Multi Player", True, (255,255,255))# ,(6,288,288)) 
        textRect_6 = text_6.get_rect()
        textRect_6.center = (294,215)

        font_7 = P.font.Font('freesansbold.ttf', 25)
        text_7 = font_7.render("2. Single Player", True, (255,255,255))# ,(6,288,288)) 
        textRect_7 = text_7.get_rect()
        textRect_7.center = (294,250)

        font_8 = P.font.Font('freesansbold.ttf', 25)
        text_8 = font_8.render("3. Exit", True, (255,255,255))# ,(6,288,288)) 
        textRect_8 = text_8.get_rect()
        textRect_8.center = (294,285)

        pong.blit(text_6, textRect_6)
        pong.blit(text_7, textRect_7)
        pong.blit(text_8, textRect_8)

    else:
        
        font_2 = P.font.Font('freesansbold.ttf', 64)
        text_2 = font_2.render(str(scr1), True, (255,255,255))# ,(6,288,288)) 
        textRect_2 = text_2.get_rect()
        textRect_2.center = (150,300)

        font_3 = P.font.Font('freesansbold.ttf', 64)
        text_3 = font_3.render(str(scr2), True, (255,255,255))# ,(6,288,288)) 
        textRect_3 = text_3.get_rect()
        textRect_3.center = (450,300)

        
        font_4 = P.font.Font('freesansbold.ttf', 15)
        text_4 = font_4.render("Press SPACE to continue", True, (255,255,255))# ,(6,288,288)) 
        textRect_4 = text_4.get_rect()
        textRect_4.center = (294,235)

        font_5 = P.font.Font('freesansbold.ttf', 15)
        text_5 = font_5.render("Press 'r' to Restart", True, (255,255,255))# ,(6,288,288)) 
        textRect_5 = text_5.get_rect()
        textRect_5.center = (294,255)
    
        pong.blit(text_2, textRect_2)
        pong.blit(text_3, textRect_3)
        pong.blit(text_4, textRect_4)
        pong.blit(text_5, textRect_5)

    P.display.update()

    #game pause
    wait = True
    while wait:
        for event in P.event.get():
            if event.type == P.QUIT:
                P.quit()

            k = P.key.get_pressed()
            
            if scr1 == scr2 == 0:
                if k[P.K_1]:
                    multi = True
                    wait = False

                if k[P.K_2]:
                    multi = False
                    wait = False


                if k[P.K_3]:
                    P.quit()
                    
            else:
                if k[P.K_SPACE]:
                    wait = False

                if k[P.K_r]:
                    scr1 = scr2 = 0
                    wait = False
                    
                #if k[P.K_m]:
                    

g_over = True

#main loop
while True:

    #Checking if game over
    if g_over:
        dash1_y = 180
        dash2_y = 180
        #pong.fill((0,0,0))
        gameover()
        g_over = False
        a = 0    
        
    pong.fill((0,0,0)) 

    clock.tick(60)    #FPS

    #Quiting
    for event in P.event.get():
        if event.type == P.QUIT:
            P.quit()
            sys.exit()

    #initial ball speed
    if a == 0 :
        s_x = 5 
        s_y = 0
        b_x = 300
        b_y = 200
        a += 1
        
    #ball hit lower wall
    if b_y >= 390:
        up = True
        down = False
        s_x = 5
        s_y = 5

    #ball hit upper wall
    if b_y <= 10:
        up = False
        down = True
        s_x = 5
        s_y = 5

    #ball hit dash1
    if b_x <= 25:
        #dash1 at 1
        if dash1_y <= b_y < dash1_y + 15:
            up = True
            down = False
            left = False
            right = True
            s_x = 4
            s_y = 5

        #dash1 at 2
        if dash1_y + 15 <= b_y < dash1_y + 30 and b_y != (dash1_y)/2:
            up = True
            down = False
            left = False
            right = True
            s_x = 5
            s_y = 4

        #dash1 at 3
        if dash1_y + 30 <= b_y < dash1_y + 45 and b_y != (dash1_y)/2:
            down = True
            up = False
            left = False
            right = True
            s_x = 5
            s_y = 4

        #dash1 at 4
        if dash1_y + 45 <= b_y <= dash1_y + 60:
            down = True
            up = False
            left = False
            right = True
            s_x = 4
            s_y = 5

    #dash2
    if b_x >= 575:
        #ball hit dash2 at 1
        if dash2_y <= b_y < dash2_y + 15:
            up = True
            down = False
            left = True
            right = False
            s_x = 4
            s_y = 5

        #dash2 at 2
        if dash2_y + 15 <= b_y < dash2_y + 30 and b_y != (dash2_y)/2:
            up = True
            down = False
            left = True
            right = False
            s_x = 5
            s_y = 4
        
        #dash2 at 3
        if dash2_y + 30 <= b_y < dash2_y + 45 and b_y != (dash2_y)/2:
            down = True
            up = False
            left = True
            right = False
            s_x = 5
            s_y = 4

        #dash2 at 4
        if dash2_y + 45 <= b_y <= dash2_y + 60:
            down = True
            up = False
            left = True
            right = False
            s_x = 4
            s_y = 5

    #Checking who lost
    if b_x < 21:
        g_over = True
        scr2 += 1
        
    if b_x > 579:
        g_over = True
        scr1 += 1
        
    #Checking which direction to go
    if left == True and right == False:
        b_x -= s_x
        
    if left== False and right == True:
        b_x += s_x

    if up == True and down == False:
        b_y -= s_y
        
    if up == False and down == True:
        b_y += s_y
        

    #Checking which keys are pressed
    keys = P.key.get_pressed()
    
    if dash1_y <= 5:         #dash1 hit upper wall
        if keys[P.K_s]:
            dash1_y +=5

    elif dash1_y >= 335:     #dash1 hit lower wall
        if keys[P.K_w]:
            dash1_y -=5
    else:                   #dash 1 hit no wall
        if keys[P.K_w]:
            dash1_y -= 5

        if keys[P.K_s]:
            dash1_y += 5

    #Singleplayer (dash2 is a bot)
    if multi == False:
        if left == True:
            if dash2_y >180:
                dash2_y -= 5

            if dash2_y < 180:
                dash2_y += 5
        
        if right == True and b_x >= 300:
            if dash2_y + 24 >= b_y:
                dash2_y -= 5

            if dash2_y + 35 <= b_y:
                dash2_y += 5
        
    else:
        #same for dash2
        if dash2_y <= 5: 
            if keys[P.K_DOWN]:
                dash2_y +=5

        elif dash2_y >= 335:
            if keys[P.K_UP]:
                dash2_y -=5
        else:
            if keys[P.K_UP]:
                dash2_y -= 5

            if keys[P.K_DOWN]:
                dash2_y += 5

    #Drawing each things
    P.draw.circle(pong,(255,255,255),(b_x,b_y),10)                  #Ball
 
    P.draw.rect(pong,(255,255,255),P.Rect(dash1_x,dash1_y,5,60))    #Player 1
    P.draw.rect(pong,(255,255,255),P.Rect(dash2_x,dash2_y,5,60))    #Player 2
    P.draw.rect(pong,(255,255,255),P.Rect(298,0,4,400))             #Half line
    P.draw.rect(pong,(255,255,255),P.Rect(0,0,600,400),5)           #Border
    
    P.display.update()
