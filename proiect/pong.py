import pygame
from tkinter import *

Width, Height =Tk().winfo_screenwidth()/1.5 , Tk().winfo_screenheight()/1.5

# Frames per second
FPS = 60

# # Range of colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (208, 12, 12)
orange = (235, 117, 5)
yellow = (214, 214, 20)
green = (62, 202, 17)
light_blue = (17, 182, 212) 
dark_blue = (6, 42, 240)
violet = (102, 6, 240)
pink = (204, 17, 99)

paddle_width, paddle_height = 20, Height/5

class Paddle :
	def __init__(self, x, y, width, height) :
		self.x = self.original_x = x
		self.y = self.original_y = y
		self.width = width
		self.height = height
		self.color = white

	def set_color(self, color) :
		self.color = color

	def draw(self, win) :
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

	def move(self, up = True) :
		if up :
			self.y -= Height/100
		else :
			self.y += Height/100

	def reset(self) :
		self.x = self.original_x
		self.y = self.original_y


class Ball :
	def __init__(self, x, y, radius) :
		self.x = x
		self.y = y
		self.radius = radius
		self.x_vel = Width/120
		self.y_vel = 0
		self.color = white

	def set_color(self, color) :
		self.color = color

	def draw(self, win) :
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

	def move(self) :
		self.x += self.x_vel
		self.y += self.y_vel

	def reset(self) :
		self.x_vel *= -1
		self.y_vel = 0
		self.x = Width / 2
		self.y = Height / 2


# Selects the colors for the elements
def choose_color(win, element, object, font1, font2) :
	titlu = font1.render("Choose the color for the " f"{object}:", True, light_blue)
	text = font2.render("Press:", True, white)
	text_w = font2.render("a -> WHITE", True, white)
	text_r = font2.render("r -> RED", True, red)
	text_o = font2.render("o -> ORANGE", True, orange)
	text_y = font2.render("y -> YELLOW", True, yellow)
	text_g = font2.render("g -> GREEN", True, green)
	text_l = font2.render("l -> LIGHT BLUE", True, light_blue)
	text_d = font2.render("d -> DARK BLUE", True, dark_blue)
	text_v = font2.render("v -> VIOLET", True, violet)
	text_p = font2.render("p -> PINK", True, pink)
	text_final = font2.render("Press SPACE when you are happy with your choice", True, white)

	win.fill(black)
	win.blit(titlu, (Width/2 - Width/4.5, Height/10))
	win.blit(text, (Width/8, Height/3))
	win.blit(text_w, (Width/6, Height/2 ))
	win.blit(text_r, (Width * 2.2/6, Height/2))
	win.blit(text_o, (Width * 3.4/6, Height/2))
	win.blit(text_y, (Width * 4.6/6, Height/2 ))
	win.blit(text_g, (Width/12, Height/2 + Height/8))
	win.blit(text_l, (Width * 3.3/12, Height/2 + Height/8))
	win.blit(text_d, (Width * 5.6/12 , Height/2 + Height/8))
	win.blit(text_v, (Width * 7.9/12, Height/2 + Height/8))
	win.blit(text_p, (Width * 10.2/12, Height/2 + Height/8))
	win.blit(text_final, (Width/2 - Width/4, Height/1.25))

	pygame.display.update()

	run = True

	while run :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				# Check if the choice is made
				if event.key == pygame.K_SPACE :
					run = False
					break

				# Select a color
				if event.key == pygame.K_a:
					element.set_color(white)
					element.draw(win)
					pygame.display.update()

				if event.key == pygame.K_r:
					element.set_color(red)
					element.draw(win)
					pygame.display.update()

				if event.key == pygame.K_o:
					element.set_color(orange)
					element.draw(win)
					pygame.display.update()

				if event.key == pygame.K_y:
					element.set_color(yellow)
					element.draw(win)
					pygame.display.update()

				if event.key == pygame.K_g:
					element.set_color(green)
					element.draw(win)
					pygame.display.update()

				if event.key == pygame.K_l:
					element.set_color(light_blue)
					element.draw(win)
					pygame.display.update()

				if event.key == pygame.K_d:
					element.set_color(dark_blue)
					element.draw(win)
					pygame.display.update()

				if event.key == pygame.K_v:
					element.set_color(violet)
					element.draw(win)
					pygame.display.update()

				if event.key == pygame.K_p:
					element.set_color(pink)
					element.draw(win)
					pygame.display.update()
					    

# Used to draw the elements needed for the game
def draw_elements(win, paddles, ball, score_A, score_B, score) :
	win.fill(black)

	score_A_text = score.render(f"{score_A}", 1, light_blue)
	score_B_text = score.render(f"{score_B}", 1, light_blue)

	win.blit(score_A_text, (Width / 4 - score_B_text.get_width() / 2, 20))
	win.blit(score_B_text, (Width * 3 / 4 - score_A_text.get_width() / 2, 20))

	for paddle in paddles :
		paddle.draw(win)
	
	ball.draw(win)

	pygame.display.update()


# Sets the movement for the paddles
def handle_paddle_movement(keys, left_paddle, right_paddle) :
	if keys[pygame.K_w] and left_paddle.y - Height/100 >= 0 :
		left_paddle.move(up = True)

	if keys[pygame.K_s] and left_paddle.y + Height/100 + left_paddle.height <= Height :
		left_paddle.move(up = False)

	if keys[pygame.K_UP] and right_paddle.y - Height/100 >= 0 :
		right_paddle.move(up = True)

	if keys[pygame.K_DOWN] and right_paddle.y + Height/100 + right_paddle.height <= Height :
		right_paddle.move(up = False)


# Check for collision with the ceiling and the paddles
def handle_collision(ball, left_paddle, right_paddle) :
	# Collision with the ceiling
	if ball.y + ball.radius >= Height :
		ball.y_vel *= -1
	elif ball.y - ball.radius <= 0 :
		ball.y_vel *= -1

	# Collision with the paddles
	if ball.x_vel < 0 :
		if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height :
			if ball.x - ball.radius <= left_paddle.x + left_paddle.width :
				ball.x_vel *= -1.01

				middle_y = left_paddle.y + left_paddle.height / 2
				dif = middle_y - ball.y
				reduction = (left_paddle.height / 2) / (Height / 100)
				ball.y_vel = -dif / reduction
	else :
		if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height :
			if ball.x - ball.radius >= right_paddle.x - right_paddle.width:
				ball.x_vel *= -1.01

				middle_y = right_paddle.y + right_paddle.height / 2
				dif = middle_y - ball.y
				reduction = (right_paddle.height / 2) / (Height / 100)
				ball.y_vel = -dif / reduction


def start_pong() :
	pygame.init()

	Win = pygame.display.set_mode((Width, Height))
	pygame.display.set_caption("Pong")

	# Used fonts for the texts
	font1 = pygame.font.SysFont("Ariel", 50, True, False)
	font2 = pygame.font.SysFont("Ariel", 40, True, False)
	font3 = pygame.font.SysFont("Ariel", 100, "bold")

	# Creating the paddles and the ball
	left_paddle = Paddle(Width/50, Height/2 - paddle_height/2, paddle_width, paddle_height)
	choose_color(Win, left_paddle, "LEFT PADDLE", font1, font2)
	
	right_paddle = Paddle(Width - Width/50 - paddle_width, Height/2 - paddle_height/2, paddle_width, paddle_height)
	choose_color(Win, right_paddle, "RIGHT PADDLE", font1, font2)

	ball = Ball(Width / 2, Height / 2, Width/125)
	choose_color(Win, ball, "BALL", font1, font2)

	score_A = 0
	score_B = 0

	run = True
	clock = pygame.time.Clock()

	while run :
		# Prevents from running more than 60 fps - regulates the speed
		clock.tick(FPS)

		draw_elements(Win, [left_paddle, right_paddle], ball, score_A, score_B, font3)
		
		# Checks if the players want to quit the game
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()

		# Set the movement of the paddles and the ball
		keys = pygame.key.get_pressed()

		handle_paddle_movement(keys, left_paddle, right_paddle)
		ball.move()

		handle_collision(ball, left_paddle, right_paddle)
		

		# Collision with the walls
		if ball.x + ball.radius >= Width or ball.x - ball.radius <= 0 :
			if ball.x + ball.radius >= Width :
				score_A += 1
			elif ball.x - ball.radius <= 0 :
				score_B += 1	

			ball.reset()
			left_paddle.reset()
			right_paddle.reset()

		# Check if the game has ended
		if score_A >= 10 or score_B >= 10 :
			run = False

	run = True

	while run :
		# Prevents from running more than 60 fps - regulates the speed
		clock.tick(FPS)

		if score_A == 10 :
			end_game = font1.render("Left Player WON", True, light_blue)
		else :
			end_game = font1.render("Right Player WON", True, light_blue)
			
		text = font2.render("Press SPACE to restart the game", True, white)

		Win.fill(black)
		Win.blit(end_game, (Width / 2 - Width / 10, Height / 2))
		Win.blit(text, (Width / 2 - Width / 6.5, Height / 2 + Height / 10))
		pygame.display.update()

		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				run = False
				break
	
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_SPACE:
					start_pong()

	pygame.quit()


# if __name__ == '__main__' :
# 	start_pong()