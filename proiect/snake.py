import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
import ctypes

class square(object):
    rows = 20
    w = 700
    def __init__(self, start, dirnx=1, dirny=0, color = (195, 125, 146)): 
        self.pos = start
        self.dirnx = 1 
        self.dirny = 0
        self.color = color

    def moveSquare(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes = False):
        distance = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*distance + 1, j*distance + 1, distance - 2, distance - 2))
        if eyes :
            center = distance // 2
            rCircle = 3
            centerCircle = (i * distance + center - rCircle, j * distance + 8)
            centerCircle2 = (i * distance + distance - rCircle * 2, j * distance + 8)
            pygame.draw.circle(surface, (0,0,0), centerCircle, rCircle)
            pygame.draw.circle(surface, (0,0,0), centerCircle2, rCircle)



class snake(object):
    body = []
    turns = {}                                      #dictionar care tine minte locul unde facem o intoarcere, o miscare
    def __init__(self, color, pos):
        self.color = color
        self.head = square(pos)
        self.body.append(self.head)
        self.dirnx = 0                              #directia in care se misca
        self.dirny = 1


    def moveSnake(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]


                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]


        for i, s in enumerate(self.body):
            p = s.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                s.moveSquare(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else :
                if s.dirnx == -1 and s.pos[0] <= 0:
                    s.pos = (s.rows-1, s.pos[1])                    #daca ajunge in margfinea din stanga trece in partea dreapta a ferestrei
                elif s.dirnx == 1 and s.pos[0] >= s.rows-1:
                    s.pos = (0, s.pos[1])                           #daca ajunge in marginea din drepta a ecranului, trece in partea stanga
                elif s.dirny == 1 and s.pos[1] >= s.rows - 1:
                    s.pos = (s.pos[0], 0)                           #daca ajunge in marginea de jos a ecranului, trece in partea de sus
                elif s.dirny == -1 and s.pos[1] <= 0 : 
                    s.pos = (s.pos[0], s.rows - 1)                  #daca ajunge in marginea de sus a ecranului, trece in partea de jos   
                else: s.moveSquare(s.dirnx, s.dirny)                      #doar facem mutarea daca nu e niciun caz


    def reset(self, pos):
        self.body = []
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
        self.head = square(pos)
        self.body.append(self.head)


    def addSquare(self):
        snakeTail = self.body[-1]
        dx, dy = snakeTail.dirnx, snakeTail.dirny

        if dx == 1 and dy == 0:
            self.body.append(square((snakeTail.pos[0]-1,snakeTail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(square((snakeTail.pos[0]+1,snakeTail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(square((snakeTail.pos[0],snakeTail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(square((snakeTail.pos[0],snakeTail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy


    def draw(self, surface):
        for i, s in enumerate(self.body):
            if i==0:
                s.draw(surface, True)
            else:
                s.draw(surface)


def drawGrid(w, rows, surface):
    sizeBetween = w // rows 
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween
        pygame.draw.line(surface,(255,255,255),(x, 0), (x, w))
        pygame.draw.line(surface,(255,255,255),(0,y), (w, y))

    

def redrawWindow(surface):
    global rows, width, s, squareSnack
    surface.fill((104, 83, 77))
    s.draw(surface)
    squareSnack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSquareSnack(rows, snakeItem):
    positions = snakeItem.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return(x,y)

def message_box(msg1, msg2):
    ctypes.windll.user32.MessageBoxW(0, msg1, msg2, 1)
    

def start_snake():
    global width, rows, s, squareSnack
    pygame.init()
    
    width = 700
    height = 700
    rows = 20
    
    pygame.display.set_caption("Snake")
    win = pygame.display.set_mode((width, height))

    s = snake((195, 125, 146), (10,10))
    squareSnack = square(randomSquareSnack(rows, s), color = (126, 189, 195))
    flag = True

    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(7)
        s.moveSnake()
        if s.body[0].pos == squareSnack.pos:
            s.addSquare()
            squareSnack = square(randomSquareSnack(rows, s), color = (126, 189, 195))
        
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                
                message_box("Joaca din nou!!! Ai avut scorul: " + str(len(s.body)), "Ai pierdut! :(((")
                s.reset((10,10))
                break
                
        redrawWindow(win)
    pass
