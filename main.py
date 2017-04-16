#variable names of images for loading images from the folder
bif="bg3.jpg"
bar1="bar1_new.jpg"
bar2="bar2_new.jpg"
bar3="bar3_new.png"
bar4="bar4_new.png"
brick="brick.jpg"
#g1="fun.png"
def tileblit(src, dst):                      #http://archives.seul.org/pygame/users/May-2003/msg00057.html
    srcw, srch = src.get_size()              #http://archives.seul.org/pygame/users/May-2003/msg00058.html
    dstw, dsth = dst.get_size()
    for y in range(0, dsth, srch):
        for x in range(0, dstw, srcw):
            dst.blit(src, (x, y))

#all imports
import pygame, sys, random, pygame.mixer
from pygame.locals import *

#initialising pygame
pygame.init()

screen=pygame.display.set_mode((1229,700),0,32)    #create window
pygame.display.set_caption('Table Tennis Pygame')  #window title

#converting image for compatibility
table=pygame.image.load(bif).convert()
roger=pygame.image.load(bar1).convert()
nadal=pygame.image.load(bar2).convert()
murray=pygame.image.load(bar3).convert()
novak=pygame.image.load(bar4).convert()
src=pygame.image.load(brick).convert()
#animation=pygame.image.load(g1).convert()


#colors
color = (138,65,530)
background_color = (82,0,4)
white = (255,255,255)
black = (0,0,0)
menu_color = (0,99,99)
ball_color = (255,145,1)
ball_color_2 = (255,0,1)
ready_color = (27,43,1)

#initialising variables
d = 10
maxscore = 11
count = 0
level = 1
h1=240; h2=240
w1=550; w2=550             #center = 1229/2 and width = 152 so horizontal bar starts from center-(152/2) =~ 539
screenshot = 0
BallX=625; BallY=310
BallSpeedX= -1; BallSpeedY= 1
Player1_score = 0; Player2_score = 0
play = False; ready = False
pause = False; serve = False
temp = True
h_score=615; h_menu=665              #height from top
ready_radius=50;pause_radius = 60    #pause circle is larger then ready, this is not radious of ball
menu_width = 160; menu_height = 40

#initialising text labels
welcomefont = pygame.font.SysFont("Comic Sans MS", 60)
myfont = pygame.font.SysFont("Comic Sans MS", 30)
myfont2 = pygame.font.SysFont("ActionIsShaded", 40)
myfont3 = pygame.font.SysFont("ActionIsShaded", 35)
EXIT = myfont2.render("Exit",1,black)
NextLevel = myfont2.render("Next Level",1,black)
NewGame = myfont3.render("New Game",1,black)
Start = welcomefont.render("WELCOME",1,black)
Play = myfont2.render("Play",1,black)
Begin = myfont2.render("Click",1,white)
Paused = myfont2.render("Paused",1,white)
Pause = myfont2.render("Pause",1,black)
Resume = myfont2.render("Resume", 1, black)
Music = myfont2.render("Background Music is ON", 1, black)
Mute = myfont2.render("Press M to toggle music", 1, black)



#for sound effects
pygame.mixer.music.load('back2.ogg')
pygame.mixer.music.play(-1, 0.0) #-1 means infinite times play, 0.0 means start music from 0.0 second of back2.ogg
musicPlaying = True
AirHorn=pygame.mixer.Sound('Air Horn.wav')  # horn tune whenever a new game start
#tak = pygame.mixer.Sound('tak.wav')
balken = pygame.mixer.Sound('bump.wav')
paddle = pygame.mixer.Sound('paddle1.wav')

#for game background
#background=pygame.draw.rect(screen, background_color, (-0,0,1229,700),0) #rect(Surface, color, Rect, width=0) -> Rect
#tileblit(animation,screen);
#pygame.time.delay(2000);
tileblit(src,screen);
screen.blit(Start, (500,100)) #It means write Start on screen starting from 570,100 
screen.blit(Mute, (500,350))
if(musicPlaying):
    s = "( Music is ON )"
else:
    s = "( Music is OFF )"
Music = myfont2.render(s, 1, black)
screen.blit(Music, (550,200))

#
clock = pygame.time.Clock()
time = 0; t_level = 0
total_seconds = 0; t_s_level = 0
seconds = 0; s_level = 0
minutes = 0; m_level = 0

output_string = "swaro"

def present_play():           #shows present screen
    #create screen
    tileblit(src,screen);
    screen.blit(table, (15,10))
    player1 = myfont.render("Player 1", 1, white)
    player2 = myfont.render("Player 2", 1, white)
    s  = str(Player1_score)
    player1_score = myfont.render(s,1,white)
    s = str(Player2_score)
    player2_score = myfont.render(s,1,white)
    divider = myfont.render("-",1,white)
    ##positioning them in place on the screen
    screen.blit(player1, (310, h_score))
    screen.blit(player2, (910, h_score))
    screen.blit(player1_score, (565,h_score))
    screen.blit(player2_score, (665,h_score))
    screen.blit(divider, (620,h_score))
    #text = myfont2.render(output_string, True, black)
    screen.blit(roger, (30,h1))
    screen.blit(nadal, (1166,h2))
    if(level == 2):
        screen.blit(murray, (w1,562))
        screen.blit(novak, (w2,25))

def home():
    tileblit(src,screen);
    if(musicPlaying):
        s = "( Music is ON )"
    else:
        s = "( Music is OFF )"
    screen.blit(Start, (500,100))
    Music = myfont2.render(s, 1, black)
    screen.blit(Music, (550,200))
    screen.blit(Mute, (500,350))

def close():
    pygame.quit()
    sys.exit()

#infinite loop running
while True:
    #watch()
    for event in pygame.event.get():
        if event.type == QUIT:
            close()
        if (event.type == KEYDOWN):
            if (event.key == K_RETURN):
                serve = True
            if (event.key == K_m):
                if(musicPlaying):
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.load('back2.ogg')
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
                home()
            if(event.key == K_x):
                s = "screenshot/screen_"+str(screenshot)+".jpg"
                pygame.image.save(screen,s)
                screenshot+=1
        #for mouse clicks
        if (event.type == MOUSEBUTTONDOWN):
            mouse_x,mouse_y = pygame.mouse.get_pos()
            #for New game or Start button
            if(30<mouse_x and mouse_x<190) and (660<mouse_y and mouse_y<700):
                #means game is running and the tab is for New Game
                if(play):
                    home();
                    #parameters back to initial values
                    play  = False
                    ready = False
                    pause = False
                    serve = False
                    h1=240; h2=240
                    w1 = 550; w2 = 550
                    time = 0; t_level = 0
                    total_seconds = 0; t_s_level = 0
                    seconds = 0; s_level = 0
                    minutes = 0; m_level = 0
                #means game is not running, Main menu is being shown so the tab works as Play
                else:
                    #start playing
                    play = True
                Player1_score =  0
                Player2_score = 0
                BallX = 625
                BallY = 310
                level = 1
            #for Pause Button
            if(240<mouse_x and mouse_x<400) and (660<mouse_y and mouse_y<700):
                #Pause or Resume in Play mode 
                if(play):
                    if((Player1_score == maxscore or Player2_score == maxscore) and level == 1):
                        play = True
                        Player1_score =  0
                        Player2_score = 0
                        ready = False
                        BallX=625
                        BallY = 310
                        # reset level time
                        m_level = 0
                        s_level = 0
                        t_s_level = 0
                        t_level = 0
                        level = 2
                        
                    elif ((Player1_score == maxscore or Player2_score == maxscore) and level == 2):
                        close()
                    elif(pause):
                        pause = False
                        pygame.mixer.music.play(-1,0.0)
                        musicPlaying = True
                    else:
                        pause = True
                        pygame.mixer.music.stop()
                        musicPlaying = False
                #Exit in the Main Menu mode
                else:
                    close()
            #for Exit Button during Play mode
            if((450<mouse_x and mouse_x<610) and (660<mouse_y and mouse_y<700)and play and not((Player1_score == maxscore or Player2_score == maxscore) and level == 2)):
                close()
            #for ready button
            if(620-ready_radius<mouse_x and mouse_x<620+ready_radius and 310-ready_radius<mouse_y and mouse_y<310+ready_radius):
                if(not ready):
                    ready = True
                    AirHorn.play()
                    pygame.time.delay(2000)  ####

    keys = pygame.key.get_pressed()
    #different events
    if((Player1_score == maxscore or Player2_score == maxscore)and play):
        present_play()
        output_string = "Total: {0:02}:{1:02}".format(minutes, seconds)
        text = myfont2.render(output_string, True, black)
        output_string = "Leval: {0:02}:{1:02}".format(m_level, s_level)
        text_level = myfont2.render(output_string, True, black)
	# apply it to text on a label
        label = myfont2.render("Game   Over", 1, black)
        if Player1_score == maxscore:
            label2 = myfont2.render("Player   1 Wins!",1,black)
        elif Player2_score == maxscore:
            label2 = myfont2.render("Player   2 Wins!",1,black)
        screen.blit(label, (530,270))
        screen.blit(label2, (525,320))
    elif(play):
        present_play()   #load last screen
        output_string = "Total: {0:02}:{1:02}".format(minutes, seconds)
        text = myfont2.render(output_string, True, black)
        output_string = "Leval: {0:02}:{1:02}".format(m_level, s_level)
        text_level = myfont2.render(output_string, True, black)
        #for the TT-ball
        if(BallX-25 > 625):
            ball=pygame.draw.circle(screen, ball_color_2, (BallX,BallY),25,0)
        else:
            ball=pygame.draw.circle(screen, ball_color, (BallX,BallY),25,0)
        #if users are ready to play the game. Game starts.
        if(ready):
            if( not pause):
                if(serve):
                    '''
                    count+=1;
                    if(count>2000):
                        BallSpeedX+=2
                        BallSpeedY+=2
                        count=0
                        '''
                    time += clock.tick()
                    if(time > 1000):
                        total_seconds+= 1
                        t_s_level+= 1
                        time = 0
                    
                    minutes = total_seconds // 60
                    m_level = t_s_level // 60
                    seconds = total_seconds % 60
                    s_level = t_s_level %60
					
                #check for player bat movements
                    if(keys[K_i] and h2>25):
                        h2-=1
                    if(keys[K_k] and h2<443):
                        h2+=1
                    ##
                    if(keys[K_w] and h1>25):
                        h1-=1
                    if(keys[K_s] and h1<443):
                        h1+=1
                    if(level == 2):
                        if(keys[K_j] and w2>30):
                            w2-=1
                        if(keys[K_l] and w2<1048):   #1166+33-152 = 1199-152 = 1047
                            w2+=1
                        if(keys[K_a] and w2>30):
                            w1-=1
                        if(keys[K_d] and w2<1048):
                            w1+=1
                    #keeping the ball moving by pixels equal to magnitude of BallSpeedX/Y per loop
                    if(BallSpeedX > 0):
                        if (BallX+25 < 1166):
                            BallX += BallSpeedX
                        elif(BallY-25 < h2+152 and BallY+25 > h2 ):
                            BallSpeedX = -BallSpeedX
                            paddle.play()
                        #player2 missed the ball, +1 to player1 and ready for next point
                        else:
                            BallX = 625
                            BallY = 310
                            if(m_level == 0 and s_level <20 ):  #bonus score if win before 20 second
                                Player1_score += 2
                            else:
                                Player1_score += 1
                            serve = False      
                    elif(BallSpeedX < 0):
                        if(BallX-25 > 63):
                            BallX += BallSpeedX
                        elif(BallY-25 < h1+152 and BallY+25 > h1 ):
                            BallSpeedX = -BallSpeedX
                            paddle.play()
                            #tak.play()
                        #player1 missed the ball so +1 to player2 and ready for next point
                        else:
                            BallX = 625
                            BballY = 310
                            if(m_level == 0 and s_level <20 ):  #bonus score if score before 20 second
                                Player1_score += 2
                            else:
                                Player1_score += 1
                            serve = False

                    if(BallSpeedY > 0):
                        if(level == 2):
                            if(BallY+25 < 563):                               
                                BallY += BallSpeedY
                            elif(BallX-25 < w1+152 and BallX+25 > w1 ):
                                BallSpeedY = -BallSpeedY
                                paddle.play()
                            else:
                                BallY = 310
                                BallX = 625
                                Player2_score += 1
                                serve = False
                        else:
                            if (BallY+25 < 595):
                                BallY += BallSpeedY
                            else:
                                BallSpeedY = -BallSpeedY
                                balken.play()
                    elif(BallSpeedY < 0):
                        if(level == 2):
                            if(BallY-25 > 58):                               #10+15+33=58
                                BallY += BallSpeedY
                            elif(BallX-25 < w2+152 and BallX+25 > w2 ):
                                BallSpeedY = -BallSpeedY
                                paddle.play()
                            else:
                                BallY = 310
                                BallX = 625
                                Player1_score += 1
                                serve = False
                        else:
                            if(BallY-25 > 25):
                                BallY += BallSpeedY
                            else:
                                BallSpeedY = -BallSpeedY
                                balken.play()
                else:
                    if(keys[K_i] and h2>25):
                        h2-=1
                    if(keys[K_k] and h2<443):
                        h2+=1
                    if(keys[K_w] and h1>25):
                        h1-=1
                    if(keys[K_s] and h1<443):
                        h1+=1
                    if(level == 2):
                        if(keys[K_j] and w2>30):
                            w2-=1
                        if(keys[K_l] and w2<1048):   #1166+33-152 = 1199-152 = 1047
                            w2+=1
                        if(keys[K_a] and w2>30):
                            w1-=1
                        if(keys[K_d] and w2<1048):
                            w1+=1
                    if(level == 1):
                        if(keys[K_UP]):
                            if(BallY-25>25):
                                BallY -= 1
                        if(keys[K_DOWN]):
                            if(BallY+25<595):
                                BallY += 1
            else:
                ready_ball=pygame.draw.circle(screen, ready_color, (620,310), pause_radius,0)
                screen.blit(Paused, (575,300))
        #if users are not ready, then asking user for ready permission
        else:
            ready_ball=pygame.draw.circle(screen, ready_color, (620,310), ready_radius,0)
            screen.blit(Begin, (590,300))

    
    rect_newgame=pygame.draw.rect(screen, menu_color, (30,660,menu_width,menu_height),0)
    if(play):
        screen.blit(NewGame,(45,h_menu))
    else:
        screen.blit(Play,(80,h_menu))
    #For Exit button

    rect_exit=pygame.draw.rect(screen, menu_color, (240,660,menu_width,menu_height),0)   #width = 160 height = 40
    if(play):
        rect_time=pygame.draw.rect(screen, menu_color, (800,660,180,menu_height),0)
        screen.blit(text_level, [810, h_menu])
        rect_time=pygame.draw.rect(screen, menu_color, (1000,660,180,menu_height),0)
        screen.blit(text, [1010, h_menu])
        #screen.blit(NewGame,(1010,h_menu))
        if((Player1_score == maxscore or Player2_score == maxscore) and level == 2):            #case when level 2 is end => we need only exit and new game option
            screen.blit(EXIT,(290,h_menu))
        else:                                                                                   #case when either level 1 or 2 is going or level 1 is complite
            rect_exit=pygame.draw.rect(screen, menu_color, (450,660,menu_width,menu_height),0)  #3rd rectengle as exit
            screen.blit(EXIT, ( 500,h_menu))
            if(Player1_score == maxscore or Player2_score == maxscore):                         #case when level 1 is complete but player didn't decide to play level 2
                screen.blit(NextLevel,(255,h_menu))                                             #in above case show next level on 2nd menu 
            elif(not pause):                                                                    #in game is going on in any level then 2nd menu is pause
                screen.blit(Pause,(285,h_menu))
            else:
                screen.blit(Resume, (275,h_menu))
    else:
        screen.blit(EXIT,(290,h_menu))
    
    #update display after every loop
    pygame.display.update()
