import math,random,pygame
#import tkinter as tk
w = 420
win = pygame.display.set_mode((w,w))
vy = 0
x = 10
y = 420//3
birdImg = pygame.image.load("queenB.png")
xt,xt2 = w,w+250
h,h2 = random.randint(200,w-150),random.randint(200,w-150)
def bird(x,y):
    win.blit(birdImg,(x,y))
    
def lost(x,y,xt,height):
    if y>=w-79 or (y<=height-146 and x>=xt-31 and x<=xt+32) or (y>=height-23
                                                                and x>=xt-32 and x<=xt+32):
        #messagebox.showinfo("Flappy","A U PICKU MATERINU!!!")
        return True

def game(xt,height):
    
    global vx,vy,g,a,win
    lower = pygame.image.load("tube2.png")
    upper = pygame.image.load("tube1.png")
    win.blit(upper,(xt,height-320-145))
    win.blit(lower,(xt,height))

def main():
    while True:
        bg = pygame.image.load("bck.png")
        global win,x,y,vy,xt,xt2,h,h2
        w = 420
        xt,xt2 = w,w+250
        h,h2 = random.randint(200,w-150),random.randint(200,w-150)
        y = w//3
        win.blit(bg,(0,0))
        bird(x,y)
        pygame.display.update()
        vy = 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vy=max(-2,vy-2.5)
                while True:
                    vy = min(vy + 0.012,1.5)
                    y+=vy
                    win.blit(bg,(0,0))
                    xt-=1
                    xt2-=1
                    if xt2 <= x-52:
                        xt2 = w
                        h2 = random.randint(80,w)
                    if xt <= x-52:
                        xt = w
                        h = random.randint(80,w)
                    game(xt,h)
                    game(xt2,h2)
                    bird(x,y)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                          vy=max(-2,vy-2.5)
                    if lost(x,y,xt,h) or lost(x,y,xt2,h2):
                        main()     
main()
