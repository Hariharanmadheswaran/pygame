import  pygame,time,random


pygame.init()


screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("SNAKE GAME")  # header of the screen

# setting the co-ordinate for snake to start from
lists=[20,60,100,140]     #x-axis
lists2=[0,0,0,0]          #y -axis


# images for snake, bomb ,egg and background but i not used
snakeimg=pygame.image.load("C:/Users/Hariharan.M/Downloads/block.jpg")
egg_img=pygame.image.load("C:/Users/Hariharan.M/Downloads/meals.jpg")
bombimg=pygame.image.load("C:/Users/Hariharan.M/Downloads/bomb.png")
# background=pygame.image.load("C:/Users/Hariharan.M/Downloads/fill_background.jpg")

# random co ordinate for egg to place
ax=random.randint(0,750)
ay=random.randint(0,550)

# for every 5 score increase a bomb is placed as riddle to make game tough
bomb_arr=[]    #initially there are zero

def collision():     # if egg coordinate and snake head meets ,then egg is ate by snake
    if (abs(ax-lists[-1])<35 or abs(ax-lists[-1]-40)<35) and (abs(ay-lists2[-1])<35 or abs(ay-lists2[-1]-40)<35):
        return True
    return False

def bomb_collision():  #if snake head touches bomb ,then game over
    for bx,by in bomb_arr:
        if (abs(bx-lists[-1])<39 ) and (abs(by-lists2[-1])<39):
            return True

    return False

def egg(ax,ay):       # screening the egg image
    screen.blit(egg_img,(ax,ay))
    # print(ax,ay)

def bomb(bx,by):      # screening the bomb image
    screen.blit(bombimg,(bx,by))


def snake():    # snake movement initially moves in x direction
    global move
    for i in range(len(lists)-1):
        lists2[i]=lists2[i+1]
        lists[i]=lists[i+1]



    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            move="down"

        if event.key == pygame.K_RIGHT:
            move="right"

        if event.key == pygame.K_LEFT:
            move="left"

        if event.key == pygame.K_UP:
            move="up"

    if move=="down":
        if lists2[-1]>550:
            lists2[-1]=0
        else:
            lists2[-1] += 40
    elif move=="up":
        if lists2[-1] <10:
            lists2[-1] = 600
        else:
            lists2[-1] -= 40
    elif move=="left":
        if lists[-1] <10:
            lists[-1] = 800
        else:
            lists[-1] -= 40
    elif move=="right":
        if lists[-1] > 750:
            lists[-1] = 0
        else:
            lists[-1] +=40

    for i in range(len(lists)-1,-1,-1):
        screen.blit(snakeimg,(lists[i],lists2[i]))

#  initiallising all the parameters

move="right"
snake_score=0
diff=0
running=True
display=True

while running:
    screen.fill((0,0,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


    snake()   #screens the snake

    egg(ax,ay)    #screens the egg

    for a,b in bomb_arr:  # screen the bomb
        bomb(a,b)

    if collision():    # check collision between snake and egg
        ax = random.randint(0, 750)
        ay = random.randint(0, 550)
        snake_score+=1

    if bomb_collision():     #if true come out/game over
        # running =False
        while display:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    display = False
            font = pygame.font.Font("freesansbold.ttf", 32)
            score = font.render(" YOUR SCORE  =" + str(snake_score), True, (255, 255,255))
            msg=font.render("THANK YOU FOR PLAYING ", True, (255,255,255))
            screen.blit(score, (200,260 ))
            screen.blit(msg,(200,300))
            pygame.display.update()
        running = False
    time.sleep(.2)

    if snake_score-diff==1: #if true place another bomb
        bomb_arr.append((random.randint(0,750),random.randint(0,550)))
        diff=snake_score

    pygame.display.update()

