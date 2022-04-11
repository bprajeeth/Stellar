import random
import pygame

pygame.init()
black=(0,0,0)
white=(255,255,255)
yellow=(255,255,0)
green=(0,255,0)
rblue=(65,105,225)


def checkguess(window,value,word,attempt): #function to check if entered word is right and also to over write boxes with their respective colours
    font = pygame.font.Font(None, 50) 
    word_list=list(word)
    val=list(value)
    boxcolour=[white,white,white,white,white,white]
    for i in range(6):
        if(val[i] in word_list):
            boxcolour[i]=yellow
        if(val[i] == word_list[i]):
            boxcolour[i]=green
    #print(boxcolour)         

    for i in range(6):
        displetter=font.render(val[i],True,black)
        pygame.draw.rect(window,boxcolour[i],pygame.Rect(45+(i*10+i*60),50+(attempt*(15+60)),60,60))
        window.blit(displetter,((50+(i*10+i*60)),(55+(attempt*(20+60)))))


    if(boxcolour == [green,green,green,green,green,green]):
        return True    

width=500
height=600
lossmessage="Better Luck Next Time!"
winmessage="To Infinity and Beyond!"
f=open("wordletext.txt","r")
wordlist=f.readlines()
word=wordlist[random.randint(0,len(wordlist)-1)].upper()
print("word = ",word)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Stellar') 
window.fill(rblue,(0,0,width,height)) 
run=True
win=False
val=""
FPS=30
clock=pygame.time.Clock()
font = pygame.font.Font(None, 40) 
font2 = pygame.font.SysFont("Comic Sans",30)
attempt=0
title=font2.render("Stellar",True,(255,69,0))
window.blit(title,(182,8))
for i in range(5):
    for j in range(6):
        pygame.draw.rect(window,white,pygame.Rect(45+(j*10+j*60),50+(i*(15+60)),60,60))
while (run):

    for event in pygame.event.get():
        if(attempt <= 6):
            if(event.type == pygame.QUIT):
                run=False

            if(event.type == pygame.KEYDOWN):
                x=event.unicode
                val=val+ x.upper()              
        
                if(event.key == pygame.K_BACKSPACE):
                    val = val[0:-2]
                    #print("val = ",val)

                if(len(val)>6 and (event.unicode).isalpha()):
                    val=val[:-2]+val[-1]   

                if((event.key == pygame.K_RETURN) and len(val)>6):
                        win=checkguess(window,val,word,attempt)                
                        attempt=attempt+1
                        val=""
                        check_word=True

    window.fill(rblue,(0,430,500,200))           
    if(win == True):
        dispwin=font.render(winmessage,True,white)
        window.blit(dispwin,(95,500))    
    if(attempt == 5):
        disploss=font.render(lossmessage,True,white)
        actual_word=font.render("OG Word = "+word[:-1],True,white)
        window.blit(disploss,(100,500))         
        window.blit(actual_word,(100,540))
    guess=font.render(val,True,white)
    window.blit(guess,(170,450))             
    pygame.display.update()
    clock.tick(FPS)


