
import pygame,random,math,time
from pygame import mixer



pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("space invaders") #setting header to screen window


#images for respective characters
background=pygame.image.load("C:/Users/Hariharan.M/Downloads/space.png")
eneimg=pygame.image.load("C:/Users/Hariharan.M/Downloads/Alien.jpg")

playerimg=pygame.image.load("C:/Users/Hariharan.M/Downloads/tdtd.png")
bullet=pygame.image.load("C:/Users/Hariharan.M/Downloads/bullet222.png")



# ene_x=random.randint(0,699)
# ene_y=random.randint(0,50)
switch1=[True for i in range(6)]
switch2=[True for i in range(6)]
# denote number of enemies
ene_arr=[[random.randint(0,699),random.randint(0,50)]   for i in range(6)]

font=pygame.font.Font("freesansbold.ttf",32)
# print(ene_arr)



def player(x,y):  #player position
    screen.blit(playerimg,(x,y))


# background music ,i took vijay song...:)
mixer.music.load("C:/Users/Hariharan.M/Music/New folder/Vinnai-Kaapan-Oruvan.mp3")
mixer.music.play(1)


def show_score(x,y):  # show the score at the top screen
    score=font.render("score ="+str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))

def enemy(x,y):   # display the enemy image
    screen.blit(eneimg,(x,y))

def collision(ene_x,ene_y,bul_x,bul_y):   #if collision enemy disappear
    d=math.sqrt(((bul_x-ene_x)**2)+((ene_y-bul_y)**2))
    # print(d)
    if d<70:
        return True
    return False

# initialise all the characters
plx=380
ply=420
cha=0
score_val=0
bul_x=380
bul_y=420
fire=False


running=True
now=time.time()  # for time long a new alien appear before us

while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                cha=-0.3             #change in x

            if event.key == pygame.K_RIGHT:
                cha=0.3
            if event.key == pygame.K_SPACE:
                fire = True
                bul_x = plx
                bul_y=ply
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT  or event.key == pygame.K_RIGHT:
                cha=0
    plx+=cha
    if plx <= 0:
        plx = 0
    elif plx >= 770:
        plx = 770

    player(plx,ply)
    i=0
    for q in ene_arr:
        # print(q)
        if q[0] <= 700 and switch1[i]:
            q[0] = q[0] + 0.3

        elif q[0] >= 0 and not switch2[i]:
            q[0] = q[0] - 0.3
        else:
            switch1[i] = False if switch1[i] == True else True
            switch2[i] = False if switch2[i] == True else True
            q[1] += 30
        # print( ene_arr)
        enemy(q[0], q[1])
        i+=1

    if fire:
        screen.blit(bullet, (bul_x, bul_y))
        bul_y -= 0.2
    elimination=[]
    for q in ene_arr:
        if collision(q[0],q[1],bul_x,bul_y) and fire:
            # ene_x = random.randint(0, 699)
            # ene_y = random.randint(0, 50)
            print(ene_arr)
            score_val+=1
            elimination.append(q)
            bul_x,bul_y=plx,ply
            fire=False
    ene_arr=[q for q in ene_arr if q not in elimination]

    if time.time()-now>10:
        ene_arr.append([random.randint(0,650),random.randint(0,50)])
        switch1.append(True)
        switch2.append(True)
        now=time.time()
    show_score(0,0)
    pygame.display.update()