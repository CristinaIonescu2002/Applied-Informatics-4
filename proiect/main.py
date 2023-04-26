import pygame
from tetris import *
from snake import *
from pong import *

def game1():
    game = Tetris(20, 10, 0)
    game.start_tetris()

def game2():
    start_snake()

def game3():
    start_pong()

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill((37,9,2))
    pygame.display.set_caption("Pygame Games")

    tetris = pygame.image.load("tetris.png").convert_alpha()
    tetris = pygame.transform.scale(tetris, (100,100))

    snake = pygame.image.load("snake5.png").convert_alpha()
    snake = pygame.transform.scale(snake, (128,128))

    pong = pygame.image.load("pong.png").convert_alpha()
    pong = pygame.transform.scale(pong, (120,90))

    WHITE = (236,203,217)
    GREEN = (195, 125, 146)
    PURPLE = (131,188,255)
    BLUE = (151,210,251)

    font1 = pygame.font.SysFont('Verdana', 30, True, False)
    font2 = pygame.font.SysFont('Verdana', 25, True, False)
    font3 = pygame.font.SysFont('Verdana', 20, True, False)

    titlu = font1.render("Choose your game:", True, WHITE)
    t_snake = font2.render("Snake", True, GREEN)
    t_tetris = font2.render("Tetris", True, PURPLE)
    t_pong = font2.render("Pong", True, BLUE)
    press = font3.render("press", True, WHITE)
    press_tetris = font3.render("[ 1 ]", True, PURPLE)
    press_snake = font3.render("[ 2 ]", True, GREEN)
    press_pong = font3.render("[ 3 ]", True, BLUE)

    screen.blit(titlu, (150, 10))
    screen.blit(press, ((85, 330)))
    screen.blit(press, ((280, 330)))
    screen.blit(press, ((485, 330)))
    screen.blit(press_tetris, ((90, 360)))
    screen.blit(press_snake, ((285, 360)))
    screen.blit(press_pong, ((490, 360)))

    screen.blit(tetris, (64, 210))
    screen.blit(t_tetris, (75, 150))

    screen.blit(snake, (250, 200))
    screen.blit(t_snake, (270, 150))

    screen.blit(pong, (450, 215))
    screen.blit(t_pong, (475, 150))

    pygame.display.flip()

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game1()
                if event.key == pygame.K_2:
                    game2()
                if event.key == pygame.K_3:
                    game3()

    pygame.quit()

if __name__ == '__main__':
    main()
