import pygame;
import random;
import time;
pygame.init();
gameHeight=600;
gameWidth=300;
gameWindow=pygame.display.set_mode((gameWidth,gameHeight));
pygame.display.set_caption("A bit Racey");
gameSpeedCount=1;
score=0;
level=1;
paused=False;


clock=pygame.time.Clock();
block_x=random.randrange(0,gameWidth);
block_y=-600;
block_vel=3;
block_color=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255));
blocks=[];

class Car(object):
    def __init__(self,link,x,y):
        self.x=x;
        self.y=y;
        self.link=link;
    def draw(self):
         gameWindow.blit(pygame.image.load(self.link),(self.x,self.y));
         
class Fonts(object):
    def __init__(self,size,color,font,text,x,y):
        self.size=size;
        self.color=color;
        self.font=font;
        self.text=text;
        self.x=x;
        self.y=y;
    
    def draw(self):
        font=pygame.font.SysFont(self.font,self.size);
        surface=font.render(self.text,1,self.color);
        gameWindow.blit(surface,(self.x,self.y));

Player1Car= Car('L1.png',gameWidth/2,gameHeight-64);
# (self,size,color,font,text,x,y)
scores=Fonts(20,(0,0,0),'Arial','Score :'+str(score),3,3);
def Crashed():
    global blocks;
    blocks=[]
    text=pygame.font.SysFont('Arial',50);
    text1=text.render("You Crashed",1,(255,0,0));
    gameWindow.blit(text1,(40,(gameHeight/2)-11));    
    pygame.display.update() ;
    pygame.time.delay(1000);
    Player1Car.x=gameWidth-70;
    running=False;
    

def pauseGame():
    global paused;
    paused=True;
    
    while paused :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit();
                quit();
                
        mouse=pygame.mouse.get_pos();
        # if 45+30 >= mouse[0] and mouse[0] >= 45:
        # if gameHeight/2 +50 + 20 >=mouse[1] and mouse[1]> gameHeight/2 + 50:
        click=pygame.mouse.get_pressed();
        
        if 140 + 36 >=mouse[0] and mouse[0] >= 140:
            
            if (gameWidth+120-100) +30 >=mouse[1] and mouse[1] >= (gameWidth+120-100) + 30:
                pygame.draw.rect(gameWindow,(250,250,250),(140,(gameWidth+120)-100,36,30));
                if click[0] == 1:
                    paused=False;
                    
        
        else :
            pygame.draw.rect(gameWindow,(100,100,100),(140,(gameWidth+120)-100,36,30));
            
                
                
           
        
        text=pygame.font.SysFont('Arial',15);
        text1=text.render("Play",1,(0,0,0));
        gameWindow.blit(text1,(150,(gameWidth+120)-94));
        
        # mouse=pygame.mouse.get_pos();
        
        
        
        pygame.display.update();        
        text=pygame.font.SysFont('Arial',50);
        text1=text.render("Paused",1,(255,0,0));
        gameWindow.blit(text1,(90,(gameWidth+200)-240));    
        pygame.display.update() ;     
    
    
def redrawingWindow():
    gameWindow.fill((255,255,255));
    for block in blocks:
        block.draw();
    scores.draw();
    text=pygame.font.SysFont('Arial',20);
    text1=text.render("Level :"+str(level),1,(0,0,0));
    gameWindow.blit(text1,(gameWidth-90,6));
    
    Player1Car.draw();
    pygame.display.update();
    clock.tick(60);

class Block(object):
    def __init__(self,x,y,width,height,vel,color):
        self.x=x;
        self.y=y;
        self.vel=vel;
        self.width=width;
        self.height=height;
        self.color=color;
        self.hitbox=(self.x,self.y,self.width,self.height);
    
    def draw(self):
        pygame.draw.rect(gameWindow,self.color,(self.x,self.y,self.height,self.width));
        self.hitbox=(self.x,self.y,self.width,self.height);      
def gameIntro():
    #  def __init__(self,size,color,font,text,x,y):
    intro=True;
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit();
                quit();
        
        text=pygame.font.SysFont('Arial',50);
        text1=text.render("A bit Racey",1,(0,0,255));
        gameWindow.blit(text1,(45,(gameHeight/2)-11)); 
        mouse=pygame.mouse.get_pos();
        
        if 45+30 >= mouse[0] and mouse[0] >= 45:
            if gameHeight/2 +50 + 20 >=mouse[1] and mouse[1]> gameHeight/2 + 50:
                pygame.draw.rect(gameWindow,(100,100,100),(45,((gameHeight/2)+50),30,20));
                click=pygame.mouse.get_pressed();
                
                if click[0]==1:
                    pygame.time.delay(500);
                    intro=False;
                    running=True;
        else:
            
            pygame.draw.rect(gameWindow,(255,255,255),(45,((gameHeight/2)+50),30,20))
                   
        
        text=pygame.font.SysFont('Arial',15);
        text1=text.render("Play",1,(0,0,0));
        gameWindow.blit(text1,(47,((gameHeight/2)+50)));
        
        # print(pygame.mouse.get_pos());
        pygame.display.update();
        clock.tick(60);
    
running=True;

def playing():
    global gameHeight,gameWidth,gameWindow,block_x,level,block_y,block_vel,block_color,blocks,gameSpeedCount,score
    while running:
        
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit();
                with open("highestScores.txt","w") as highestSCores:
                    highestSCores.write("Highest Score :"+ str(score));
                    
                quit();
            
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_UP :
                    Player1Car.y-=20;
                
                if event.key ==pygame.K_DOWN :
                    Player1Car.y+=20;
                    
                if event.key == pygame.K_RIGHT :
                    Player1Car.x+=20;
                    
                if event.key ==pygame.K_LEFT :
                    Player1Car.x-=20;
                    
                    
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_p:
                    pauseGame();
            
            if Player1Car.x < 0:
                Crashed();
        
        
        if len( blocks ) < 2:
            blocks.append(Block(block_x,block_y,100,40,block_vel,block_color));
            score+=1;
            scores.text=  scores.text='Score :'+str(score);
            
          
            
            
           
        if int(score) % 10 == 0:
            gameSpeedCount += 0.01;  
            level += 0.005;
        
        for block in blocks:
            
            if len(blocks) > 1:
                
                if blocks[len(blocks)-1].y > gameHeight:
                    if len( blocks ) <1:
                        blocks.append(Block(block_x,block_y,100,40,block_vel,block_color));
        
                    
                    
            #    block.hitbox[0] >= Player1Car.x and (block.hitbox[0] < (gameWidth-Player1Car.x+64)) and (block.hitbox[1] >=Player1Car.y)
            block.y+=block.vel+gameSpeedCount;
            
            block.hitbox=(block.x + block.height,block.y+block.height,block.width,block.height);
            
            if block.y +block.hitbox[2] >= Player1Car.y:
                if block.hitbox[0] >=Player1Car.x and block.hitbox[0] <= Player1Car.x +64:
                    Crashed();
                
            
            if(block.y > gameHeight):
                blocks.pop(blocks.index(block));

            
        block_x=random.randrange(0,gameWidth);
        block_color=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255));
        redrawingWindow();
         
                    
     
   
        
            
gameIntro();
playing();