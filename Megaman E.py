#Import the pygame library and random library
import pygame
from random import randint
#Initiate pygame
pygame.init()
#Initiating font
pygame.font.init()
#Setting font 1 and font 2
font=pygame.font.SysFont("calibri",150)
font2=pygame.font.SysFont("calibri",50)
font3=pygame.font.SysFont("calibri",80)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        #Sprites becomes the image
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        #Makes it a rectangle
        self.rect = self.image.get_rect()
        #Sets the center of the rectangle to the x and y position of the sprite
        self.rect.center = (x,y+5)
        #Allows for which direction the player is facing
        self.direct = direction

    def update(self):
        #Updates the movement of the bullet sprite
        if self.direct:
            #if direction is right, bullet shoots right
            self.rect.centerx += 15
        else:
            #else the bullet shoots left
            self.rect.centerx -= 15
        #Once it reaches the wall, the bullet disappears
        if self.rect.right >= 768:
            self.kill()
        if self.rect.left <=0:
            self.kill()

class Sword(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        #Sprites becomes the image
        pygame.sprite.Sprite.__init__(self)
        self.image = swordimg
        #Makes it a rectangle
        self.rect = self.image.get_rect()
        #Sets the center of the rectangle to the x and y position of the sprite

        #Allows for which direction the player is facing
        self.direct = direction
        if self.direct == False:
            #Makes the sword face the other direction
            self.image = pygame.transform.rotate(self.image,180)
            #Setting the position of the sword to the right
            self.rect.center = (x-45,y)
        else:
            #Setting the position of the sword to the left
            self.rect.center = (x+26,y+5)


class Enemy(pygame.sprite.Sprite): 
    def __init__(self,level):
        pygame.sprite.Sprite.__init__(self)
        #Random number either 0 or 1 determining if the enemy will be spawning from the left or from the right
        self.i=randint(0,1)
        #Setting a global variable in the class Enemy of level
        self.level=level
        #Setting enemy image as the enemy depending on the level
        #HP of enemy is dependent on level
        if self.level==1:
            self.enemyhp=40
            self.image = enemyimg
        elif self.level==2:
            self.enemyhp=80
            self.image = enemyimg2
        elif self.level==3:
            self.enemyhp=120
            self.image = enemyimg3
        elif self.level==4:
            self.enemyhp=140
            self.image = enemyimg4
        elif self.level==5:
            self.enemyhp=160
            self.image = enemyimg5
        elif self.level==6:
            self.enemyhp=700
            self.image = enemyimg
        elif self.level==7:
            self.enemyhp=1200
            self.image = enemyimg
        #Makes a rectangle in respect to the image
        self.rect = self.image.get_rect()
        if self.i==1:
            self.rect.center = (768,480)
        else:
            self.rect.center = (0,480)
    def update(self):
        if self.i==1:
            #Speed of the enemy/movement
            #If the enemy has not yet collided with the left wall, enemy moves to the left
            if self.rect.centerx>10:
                self.rect.centerx-=7
            else:
                #If the enemy is at the left then it begins to move to the right
                self.rect.centerx+=7
                #Sets i to the left
                self.i=0
        else:
            #If the enemy has not yet collided with the right wall, enemy moves to the right
            if self.rect.centerx<765:
                self.rect.centerx+=7
            else:
                #If the enemy is at the right then it beings to move to the left
                self.rect.centerx-=7
                #Sets i to the right
                self.i=1

class Airenemy(pygame.sprite.Sprite):
    def __init__(self,level):
        pygame.sprite.Sprite.__init__(self)
        #Setting image to the comet image
        self.image = comet
        #Makes a rectangle the size of the image
        self.rect=self.image.get_rect()
        #A random number from 0-768 that determines the x value of the comet spawn
        self.i=randint(0,768)
        #Setting the center of that comet to the random X and the top
        self.rect.center=(self.i,0)
        self.level=level
    def update(self):
        #Depending on level, the comet moves down a certain number of pixels everytime this class is called
        if self.level>=6:
            self.rect.centery+=27
        elif self.level==5:
            self.rect.centery+=20
        elif self.level==4:
            self.rect.centery+=16
        elif self.level==3:
            self.rect.centery+=13
        elif self.level==2:
            self.rect.centery+=10
        elif self.level==1:
            self.rect.centery+=7

#Function which displays the starting screen elements
def intro():
    #Initiating the while loop
    main=True
    while main:
        #Allows for the python shell to constantly run and not crash
        pygame.event.get()
        #Rendering font which will be displayed on screen
        welcometxt=font2.render("Welcome to Megaman E",1,(255,255,255))
        controlstxt=font2.render("Press Z for sword. Press X for gun.",1,(255,255,255))
        controlstxt2=font2.render("Arrow keys to move.",1,(255,255,255))
        continuetxt=font2.render("Press space to continue.",1,(255,255,255))
        #Displaying the background image
        screen.blit(backgroundimg,backgroundrect)
        #Displaying all the previously rendered text to the screen
        screen.blit(welcometxt,(130,150))
        screen.blit(controlstxt,(50,200))
        screen.blit(controlstxt2,(160,250))
        screen.blit(continuetxt,(120,300))
        #Checks for python events and allows for continuous input
        events = pygame.event.get()
        #Handles the inputs given by keyboard, mouse, etc.
        for event in events:
            #If the space bar is pressed the while loop will exit and the game will run
            keys_pressed=pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]==1:
                main=False
        #Updating the display with all the previously updated elements
        pygame.display.flip()    

        
#Sets the screen size (768x500)
screen_size= (768,500)

#Makes the variable Gun a sprite group
gun = pygame.sprite.Group()
swordgrp = pygame.sprite.Group()
enemygrp = pygame.sprite.Group()
airenemygrp=pygame.sprite.Group()
    
#sets the background image
backgroundimg=pygame.image.load("megamanbackground.jpg")
backgroundrect=backgroundimg.get_rect()

#Sets the player colour (rectangle displayed behind background)
playercolour=(10,10,10)

#Sets starting position of player
xplayerpos=0
yplayerpos=480


#Sets the starting speed/velocity to 0
xspeed=0
yspeed=0

#Checking variables that helps with gravity
yspeedcheck=0
ydowncheck=0
jumpcheck=0

#Counter that allows you to get hit by a meteor once and only once
hitonce=0

#Setting the values for level 1 (will be updated throughout the code via score)
level=1
timespawn=100

bulletmax=3

#Setting a bunch of variables to images
swordimg=pygame.image.load("WaveSword.png")
bulletimg=pygame.image.load("megaman-x-bullet.png")
playerimgright=pygame.image.load("RealMegamanright.png")
playerimgleft=pygame.image.load("RealMegamanleft.png")
enemyimg=pygame.image.load("gumba.png")
enemyimg2=pygame.image.load("shell.png")
enemyimg3=pygame.image.load("ghostman.png")
enemyimg4=pygame.image.load("slimeman.png")
enemyimg5=pygame.image.load("otherghost.png")
comet=pygame.image.load("Comet.png")

#Draws the screen
screen = pygame.display.set_mode(screen_size)

#Setting a default black background for the background image to be placed over
pygame.display.set_caption("Megaman E")
background=pygame.Surface(screen_size)
background=background.convert()
background.fill((0,0,0))


#Defines the starting position of player with size
playerpos=(xplayerpos,yplayerpos,20,20)

#Draws the rectange with the previous player variables behind the background
player=pygame.draw.rect(screen,playercolour,playerpos)

#Sets the while loop to start
running=True

#Sets the starting direction to the right
direction=True

#Setting both left and right movements to false
left=False
right=False

#Setting the timer,score, and player hp to default values
timer=0
score=0
playerhp=100

#Contains an empty list which will contain score values
scorelist=[]
averagescore=0

#Draws the floor and walls
floory=499
floor=pygame.draw.rect(screen,(150,20,20),(0,floory,800,1000))
leftwall=pygame.draw.rect(screen,(150,20,20),(-100,0,101,500))
rightwall=pygame.draw.rect(screen,(150,20,20),(738,0,100,500))

#Calls the function to display the starting screen
intro()

while running:
    #Incrementing the timer by 1 everytime the loop runs
    timer+=1
    #Spawns an enemy every X seconds
    if level<6:
        if timer==10000/timespawn:
            #Calls the class to create an enemy and update and limits the amount of enemies to 5
            if len(enemygrp.sprites())<5:
                enemy=Enemy(level)
            #Adds it to the enemygroup
            enemygrp.add(enemy)
            #Calls the class to create an enemy and update
            airenemy=Airenemy(level)
            #Adds the created enemy to the airenemygroup
            airenemygrp.add(airenemy)
            #Sets the timer to 0 to reset it and repeat the counter to 10000/timespawn
            timer=0
    #else if the level is greater than 5
    else:
        #If the timer is 10000/timespawn
        if timer==10000/timespawn:
            #If there is less than 1 enemy on the screen
            if len(enemygrp.sprites())<1:
                #Create an enemy
                enemy=Enemy(level)
            #Calls the class to create an enemy and update
            airenemy=Airenemy(level)
            #Adds the airenemy to the airenemygroup
            airenemygrp.add(airenemy)
            #Adds the enemy to the group
            enemygrp.add(enemy)
            #Sets the time to 0 to reset it and repeat the counter to 10000/timespawn
            timer=0
        
    
    #If player collided with left wall
    if player.colliderect(leftwall):
        #If the player is in the wall
        if xplayerpos<1:
            #Set the left movement to false to prevent further movement
            left=False
            #Set the x position of the player to be 1 pixel outside of the left wall
            xplayerpos=1
            #Set the overall x speed to 0 to prevent any movement
            xspeed=0
    #If the player collided with the right wall
    if player.colliderect(rightwall):
        #If the player is in the right wall
        if xplayerpos>748:
            #Set the right movement to false to prevent further movement
            right=False
            #Set the x position of the player to be 1 pixel outside of the left wall
            xplayerpos=748
            #Set the overall x speed to 0 to prevent any movement
            xspeed=0

    
    #Delay between new frames
    pygame.time.delay(30)
    
    #Defines the starting position of player with size
    playerpos=(xplayerpos,yplayerpos,20,20)

    #Draws the rectange with the previous player variables
    player=pygame.draw.rect(screen,playercolour,playerpos)

    #Clearsceen allows the function to print the background over the rect so you cannot see the rect
    screen.blit(backgroundimg,backgroundrect)      


    #Handles the inputs given by keyboard, mouse, etc.
    events = pygame.event.get()
    for event in events:
    
        keys_pressed=pygame.key.get_pressed()

        #Checking for left input
        if keys_pressed[pygame.K_LEFT]==1:
            #Set the left movement to true to initialize another if statement later on in the code
            left=True
            #Set direction to False (used in the classes to signify left and right, in this case I used False as left and True as right)
            direction=False
        #If left wasn't pressed
        else:
            #Set the xspeed to 0 to stop movement
            xspeed=0
            #Set left to False to avoid the if statement later on
            left=False

        #If the right key was pressed
        if keys_pressed[pygame.K_RIGHT]==1:
            #Set the right movement to true to initialize another if statement later on in the code
            right=True
            #Set the direction to True
            direction=True

        #If right wasn't pressed
        else:
            #Set the xspeed to 0 to stop movement
            xspeed=0
            #Set right to False to avoid the if statement later on
            right=False

        #If X is pressed and there are less Y bullets on the screen
        #The amount of bullets (Y) will change depending on the level (decreasing with higher levels)
        if keys_pressed[pygame.K_x] and len(gun.sprites())<=bulletmax:
            #Setting bullet to Bullet class
            bullet = Bullet(xplayerpos+20,yplayerpos,direction)
            #Adds the bullet to the gun sprite group
            gun.add(bullet)

        #If Z is pressed sword will summon
        if keys_pressed[pygame.K_z]:
            #Setting sword to Sword class
            sword=Sword(xplayerpos+20,yplayerpos,direction)
            #Adds sword to the sword spire group
            swordgrp.add(sword)

     #If left was pressed
        if left:
            #If the xspeed is less than -6
            if xspeed>-6:
                #Make xspeed -6
                xspeed-=6
                #Set left to false to prevent glitching movement
                left=False
 
        #If right is pressed
        if right:
            #If the xspeed is less than 6
            if xspeed<6:
                #Set the xspeed to 6
                xspeed+=6
                #Set right to false to prevent glitching movement
                right=False
        
        #If player on floor jump is possible
        if jumpcheck==0:
            #Set the yspeed to 0
            yspeed=0
            #If up is pressed
            if keys_pressed[pygame.K_UP]==1:
                #Set jumpcheck to 1 to only allow 1 jump
                jumpcheck=1
                #Set the initial yspeed for going upwards
                yspeed=20
 
   
   #Change the xplayer position depending on xspeed     
    xplayerpos+=xspeed
 
    #Jumping with gravity
    if jumpcheck==1:
        #If player is before the apex of the jump
        if yspeed>1 and ydowncheck==0:
            #Move the player at yspeed upwards
            yplayerpos-=yspeed
            #Make the yspeed slower as the player approaches the apex
            yspeed-=2
            #Set a counter that counts for the apex of the jump and allows for downward movement once it is reached
            yspeedcheck+=1
        #If the apex is reached
        if yspeedcheck>8:
            #Set the speed to 0
            yspeed=0
            #Set the speedcheck to 0 to allow for the next jump
            yspeedcheck=0
            #Set ydowncheck to 1 initating the downwards movement
            ydowncheck=1
        #If the player is past the apex and starting to move down
        if yspeed<=20 and ydowncheck==1:
            #Move the player at yspeed downwards
            yplayerpos+=yspeed
            #Increase the speed downwards the more the player falls
            yspeed+=2



    #Allowing for no clipping through the floor
    if player.colliderect(floor):   
        yplayerpos=floory-20
        #Resets the jumping and gravity mechanism
        jumpcheck=0
        yspeed=0
        yspeedcheck=0
        ydowncheck=0

    #Checks enemy position and player position
    for enemy in enemygrp:
        #If they collide player takes 5 damage
        if player.colliderect(enemy):
            playerhp-=5

    #Checks for comet positoin and player positoin
    for enemy2 in airenemygrp:
        #If they collide and it is unique (the first time that comet has collided with the player) then the player takes 50 damage
        if player.colliderect(enemy2) and hitonce==0:
            playerhp-=50
            hitonce=1
        #If the comet reaches the floor, it is removed from the group
        if enemy2.rect.top>510:
            enemy2.kill()
            hitonce=0


    #If the sword collides with an enemy/enemies take 40 damage
    stab = pygame.sprite.groupcollide(enemygrp,swordgrp,False,False)
    for thing in stab:
        #If the enemy is at 0 or negative HP after hit by the sword, it is removed from the group
        if thing.enemyhp - 40 <= 0:
            thing.kill()
            #If its the boss rush level you get 1000 per kill
            if level>=6:
                score+=1000
            else:
                #Get 50 points for killing an enemy with the sword
                score+=50
            #If the player is at 99 hp or less you get HP for killing enemies
            if playerhp<100:
                #Gets 20 hp for killing an enemy with a sword
                playerhp+=10
                #If the player overheals (HP > 100) you get a flat 100hp (no overhealing)
                if playerhp>100:
                    playerhp=100
        #If the enemy is still alive, it takes 40 damage from the sword
        else:
            thing.enemyhp -= 40

    #If a bullet collides with an enemy/enemies take 20 damager
    shoot = pygame.sprite.groupcollide(enemygrp,gun,False,True)
    for thing in shoot:
        #If the enemy is at 0 or negative HP after being hit by a bullet, it is removed from the group
        if thing.enemyhp - 20 <=0:
            thing.kill()
            #If its the boss rush level you get 1000 per kill
            if level>=6:
                score+=1000
            else:
                #Get 25 points for killing an enemy with a bullet
                score+=25
            #If the player is at 99 hp or less you get HP for killing enemies
            if playerhp<100:
                #Get 10 hp for killing an enemy with a bullet
                playerhp+=5
                #If the player overheals (HP > 100) you get a flat 100hp (no overhealing)
                if playerhp>100:
                    playerhp=100
        #If the enemy is still alive, it take 20 damage from the bullet
        else:
            thing.enemyhp -= 20
            
    #Drawing and updating the sprite groups
    gun.update()
    swordgrp.update()
    enemygrp.update()
    airenemygrp.update()
    gun.draw(screen)
    enemygrp.draw(screen)
    swordgrp.draw(screen)
    airenemygrp.draw(screen)

    #Drawing player image
    if direction:
        #If its right, draws the right player image and sets the position relative to the movements from the keyboard
        screen.blit(playerimgright,(xplayerpos-20,yplayerpos-30))
    else:
        #If its left, draws the left player image and sets the position relative to the movements from the keyboard
        screen.blit(playerimgleft, (xplayerpos-20,yplayerpos-30))


    #Emptying the sword group so it disappears on screen after being drawn
    swordgrp.empty()

    #Setting the levels depending on the score
    if score>=10000 and level==6:
        level=7
        #Faster spawns relative to previous level
        timespawn=2500
        #Maximum bullets of 20 on screen
        bulletmax=20
        #Rests timer to 0
        timer=0
        
    elif score>=5000 and level==5:
        level=6
        #Faster spawns relative to previous level
        timespawn=2500
        #Maximum bullets of 20 on screen
        bulletmax=20
        #Rests timer to 0
        timer=0
        #Emptying the enemy classes for just the last enemy
        enemygrp.empty()
        airenemygrp.empty()

    elif score>=2500 and level==4:
        level=5
        #Faster spawns relative to previous level
        timespawn=1000
        #Maximum bullets of 8 on screen
        bulletmax=8
        #Rests timer to 0
        timer=0

    elif score>=1000 and level==3:
        level=4
        #Faster spawns relative to previous level
        timespawn=500
        #Maximum bullets of 5 on screen
        bulletmax=5
        #Rests timer to 0
        timer=0

    elif score>=500 and level==2:
        level=3
        #Faster spawns relative to previous level
        timespawn=200
        #Maximum bullets of 4 on screen
        bulletmax=4
        #Rests timer to 0
        timer=0

    elif score>=100 and level==1:
        level=2
        #Faster spawns relative to previous level
        timespawn=200
        #Maximum bullets of 3 on screen
        bulletmax=3
        #Rests timer to 0
        timer=0
    
    #Setting the playerhp to a string to be displayed later on the screen
    playerhptxt=str(playerhp)
    #Setting the score to a string to be displayed later on the screen
    scoretxt=str(score)

    #If the player is alive, hp, and score will continue to appear
    if playerhp>0:
        #Setting the text values with font, colour, and anti aliasing
        playerhptext=font2.render(playerhptxt,1,(0,255,0))
        playerhptext2=font2.render("HP:",1,(0,255,0))
        scoretext=font2.render("Score:",1,(255,255,255))
        scoretext2=font2.render(scoretxt,1,(255,255,255))
        #Printing the previousely rendered words to the screen with position
        screen.blit(playerhptext,(70,20))
        screen.blit(playerhptext2,(5,20))
        screen.blit(scoretext,(470,20))
        screen.blit(scoretext2,(620,20))
        #Setting the level integer to a string
        leveltxt=str(level)

        #Setting the text values with font, colour, and anti aliasing
        leveltext=font2.render("Level:",1,(255,255,255))
        leveltext2=font2.render(leveltxt,1,(255,255,255))
        #Printing the previously rendered words to the screen with position
        screen.blit(leveltext,(165,20))
        screen.blit(leveltext2,(280,20))
    #Else, both the hp and the score will disappear and you will have a gameover screen
    else:
        if score>=10000:
            winnertxt=font3.render("Congratulations!",1,(255,255,255))
            winnertxt2=font3.render("You Win!",1,(255,255,255))
            screen.blit(winnertxt,(120,150))
            screen.blit(winnertxt2,(240,230))
        else:
            endscreen=font.render("Game Over!", 1,(255,255,255))
            screen.blit(endscreen,(25,150))
        running=False

    #Updates the screen with all the actions done above
    pygame.display.flip()

    #Used later to only have the current score added to the scorelist
    scoreaddcheck=1
    while not running:
        #If the score is new, it will be added to the list
        if scoreaddcheck==1:
            scorelist+=[score]
        #List is sorted from lowest to greatest
        scorelist.sort()
        #Finding the length of the list starting from 0>length
        scorelistlength=len(scorelist)
        #Finding the top score
        topscore1=scorelist[scorelistlength-1]
        #Converting the top score integer to a string to be displayed on the screen
        topscoretxt=str(topscore1)
        #Totalling the scorelist to help calculate average 
        averagescore=sum(scorelist)
        #Calculating average of the scoers
        averagescore1=averagescore/(scorelistlength)
        #Converting it to a string to be displayed on screen
        averagescoretxt=str(averagescore1)

        #Only allows for the new score to be added
        scoreaddcheck=0

        #Makes the computer constantly check for inputs to stop it from crashing
        pygame.event.get()

        #Rendering of all the end game text besides the GAME OVER!
        tryagaintxt=font2.render("Try again?",1,(255,255,255))
        tryagaininput=font2.render("Click Y/N",1,(255,255,255))
        topscore=font2.render("Top Score:",1,(255,255,255))
        topscore2=font2.render(topscoretxt,1,(255,255,255))
        averagescore=font2.render("Average Score:",1,(255,255,255))
        averagescore2=font2.render(averagescoretxt,1,(255,255,255))


        #Printing the previously rendeded texts to the screen
        screen.blit(tryagaintxt,(100,300))
        screen.blit(tryagaininput,(100,350))
        screen.blit(topscore,(320,300))
        screen.blit(topscore2,(550,300))
        screen.blit(averagescore,(320,350))
        screen.blit(averagescore2,(630,350))
        screen.blit(scoretext,(330,400))
        screen.blit(scoretext2,(460,400))
                               
        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_y]==1:
            #Restarts the game back to original values
            #Sets starting position of player
            xplayerpos=0
            yplayerpos=480

            #Sets the starting speed/velocity to 0
            xspeed=0
            yspeed=0

            #Checking variables that helps with gravity
            yspeedcheck=0
            ydowncheck=0
            jumpcheck=0

            #Counter that allows you to get hit by a meteor once and only once
            hitonce=0

            #Setting the values for level 1 (will be updated throughout the code via score)
            level=1
            timespawn=150
            bulletmax=3

            #Setting a default black background for the background image to be placed over
            pygame.display.set_caption("MEGAMAN")
            background=pygame.Surface(screen_size)
            background=background.convert()
            background.fill((0,0,0))

            #Defines the starting position of player with size
            playerpos=(xplayerpos,yplayerpos,20,20)

            #Draws the rectange with the previous player variables behind the background
            player=pygame.draw.rect(screen,playercolour,playerpos)

            #Sets the while loop to start
            running=True

            #Sets the starting direction to the right
            direction=True

            #Setting both left and right movements to false
            left=False
            right=False

            #Setting the timer,score, and player hp to default values
            timer=0
            score=0
            playerhp=100
            running=True

            #Emptying the groups so enemies aren't in their previous position (before the player died)
            enemygrp.empty()
            airenemygrp.empty()
            gun.empty()

            #Calls the function to display the starting screen for restart
            intro()

        #If N is pressed the game will exit
        if keys_pressed[pygame.K_n]==1:
            running=False
            break
        
        #Updates the screen with the information updated from the gameover screen
        pygame.display.update()

#If N is pressed, the shell will close      
pygame.quit()
        
