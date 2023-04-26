import pygame
import random

colors = [
    (0, 0, 0),                  #negru
    (208, 12, 12),              #rosu
    (235, 117, 5),              #portocaliu
    (214, 214, 20),             #galben
    (62, 202, 17),              #verde
    (17, 182, 212),             #albastru deschis
    (6, 42, 240),               #albastru inchis
    (102, 6, 240),              #mov
    (204, 17, 99),              #roz
]

class Figure:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.figures = [
            [[1, 5, 9, 13], [4, 5, 6, 7]],
            [[4, 5, 9, 10], [2, 6, 5, 9]],
            [[6, 7, 9, 10], [1, 5, 6, 10]],
            [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
            [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
            [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
            [[1, 2, 5, 6]],
        ]
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

class Tetris:

    def __init__(self, height, width, start_time):
        self.height = height
        self.width = width
        self.field = [[0 for _ in range(width)] for _ in range(height)]
        self.level = 2
        self.score = 0
        self.state = "start"
        self.time_terminat = 0
        self.x = 100
        self.y = 80
        self.zoom = 30
        self.figure = None
        self.start_time = start_time

    def new_figure(self):
        self.figure = Figure()
        self.figure.x = 3
        self.figure.y = 0

    def intersects(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or self.field[i + self.figure.y][j + self.figure.x] > 0:
                        return True
        return False

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            if all(self.field[i]):
                lines += 1
                for i1 in range(i, 1, -1):
                    self.field[i1] = self.field[i1 - 1]
                    self.field[1] = [0 for _ in range(self.width)]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover" 
            self.time_terminat = pygame.time.get_ticks() - self.start_time

    def go_left(self):
        self.figure.x -= 1
        if self.intersects():
            self.figure.x += 1

    def go_right(self):
        self.figure.x += 1
        if self.intersects():
            self.figure.x -= 1

    def rotate(self):
        self.figure.rotate()
        if self.intersects():
            self.figure.rotate()
            self.figure.rotate()
            self.figure.rotate()

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

    def start_tetris(game):
        pygame.init()

        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GRAY = (80, 80, 82)
        BACKGROUND = (37,9,2)

        started = False
        done = True

        size = (500, 710)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Tetris")

        screen.fill(BACKGROUND)
        fontStart = pygame.font.SysFont('Verdana', 25, True, False)
        textStart = fontStart.render("Press Space to start", True, WHITE)
        screen.blit(textStart, [100, 250])
        pygame.display.update()

        ok = 0

        while not started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game.start_time = pygame.time.get_ticks()
                        done = False
                        screen.fill((37,9,2))
                        ok = 1
                        break
            if ok == 1:
                break

        # Loop until the user clicks the close button.

        clock = pygame.time.Clock()
        clock_game = pygame.time.get_ticks()
        fps = 60
        counter = 0
        pressing_down = False

        while not done:
            # print("mda")
            if game.figure is None:
                game.new_figure()
            counter += 1
            if counter > 100000:
                counter = 0

            if counter % (fps // game.level // 2) == 0 or pressing_down:
                if game.state == "start":
                    game.go_down()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_r:
                        game.rotate()
                    if event.key == pygame.K_LEFT:
                        game.go_side(-1)
                    if event.key == pygame.K_RIGHT:
                        game.go_side(1)
                    if event.key == pygame.K_SPACE:
                        game.go_space()
                    if event.key == pygame.K_ESCAPE:
                        #game.start_time = pygame.time.get_ticks()
                        game.__init__(20, 10, pygame.time.get_ticks())

            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        pressing_down = False

            screen.fill(BLACK)

            for i in range(game.height):
                for j in range(game.width):
                    pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                    if game.field[i][j] > 0:
                        pygame.draw.rect(screen, colors[game.field[i][j]],
                                        [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

            if game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in game.figure.image():
                            pygame.draw.rect(screen, colors[game.figure.color], [game.x + game.zoom * (j + game.figure.x) + 1,
                                            game.y + game.zoom * (i + game.figure.y) + 1, game.zoom - 2, game.zoom - 2])

            font = pygame.font.SysFont('Verdana', 25, True, False)
            font1 = pygame.font.SysFont('Verdana', 50, True, False)
            font2 = pygame.font.SysFont('Verdana', 20, True, False)
            font3 = pygame.font.SysFont('Verdana', 20, True, False)

            text = font.render("Score: " + str(game.score), True, WHITE)
            text2 = font3.render("Time: " + str(int((pygame.time.get_ticks() - game.start_time)/1000)) + " seconds", True, WHITE)

            text_game_over = font1.render("Game Over", True, (236,203,217))
            text_game_over1 = font1.render("Press ESC", True, (195, 125, 146))
            text_game_over2 = font2.render("to try again", True, (195, 125, 146))
            text_score_game_over = font2.render("Score: " + str(game.score), True, WHITE)
            text_Time_game_over = font3.render("Time: " + str(int(game.time_terminat / 1000)) + " seconds", True, WHITE)


            screen.blit(text, [0, 0])
            screen.blit(text2, [0,30])

            if game.state == "gameover":
                screen.fill(BACKGROUND)
                screen.blit(text_game_over, [100, 250])
                screen.blit(text_score_game_over, [105, 310])
                screen.blit(text_game_over1, [105, 350])
                screen.blit(text_game_over2, [300, 400])
                screen.blit(text_Time_game_over, [105, 335])  

            pygame.display.flip()
            clock.tick(fps)

        pygame.quit()

