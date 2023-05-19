from pipes import *
from buttons import *
from settings import *

bs_file = open("best_score.txt", "r+")
best_score = int(bs_file.read())
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Flappy Woodland')
pygame.display.set_icon(icon)
font = pygame.font.Font('img/Pixeled.ttf', 40)
flying = False
game_over = False
last_pipe = pygame.time.get_ticks() - pipe_frequency
pass_pipe = False

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def Draw_score():
    draw_text(str(score), font, white, int(40), 20)

def Draw_best():
    draw_text(str(best_score), font, white, int(40), 80)

def reset_game():
	pipe_group.empty()
	player.rect.x = 100
	player.rect.y = int(screen_height / 2)
	score = 0
	return score

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range(1, 8):
			img = pygame.image.load(f'img/bird{num}.png')
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False

	def update(self):
		if flying == True:
			self.vel += 0.5
			if self.vel > 8:
				self.vel = 8
			if self.rect.bottom < 768:
				self.rect.y += int(self.vel)
		if game_over == False:
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.vel = -10
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
			self.counter += 1
			flap_cooldown = 5
			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
			self.image = self.images[self.index]
			self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
		else:
			self.image = pygame.transform.rotate(self.images[self.index], -90)

##################################

player_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
player = Player(275, int(screen_height / 2))
player_group.add(player)
run = True

while run:


	clock.tick(fps)
	#3th layer
	screen.blit(bg3, (bg_x3, 0))
	screen.blit(bg3, (bg_x3 + 1498, 0))
	#2nd layer
	screen.blit(bg2, (bg_x2, 0))
	screen.blit(bg2, (bg_x2 + 1498, 0))
	#1st layer
	screen.blit(bg1, (bg_x1, 0))
	screen.blit(bg1, (bg_x1 + 1498, 0))

	player_group.draw(screen)
	player_group.update()
	pipe_group.draw(screen)

	# HUD
	Draw_score()
	Draw_best()

	if len(pipe_group) > 0:
		if player_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and player_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
			pass_pipe = True
		if pass_pipe == True:
			if player_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				pass_pipe = False


	#ground
	screen.blit(ground1_img, (ground_x1, 668))
	screen.blit(ground1_img, (ground_x1+900, 668))
	#game states

	if pygame.sprite.groupcollide(player_group, pipe_group, False, False) or player.rect.top < 0:
		game_over = True

	if player.rect.bottom >= 768:
		game_over = True
		flying = False

	if game_over == False and flying == False:
		play.draw() == True



	#GAME STARTED

	if game_over == False and flying == True:
		time_now = pygame.time.get_ticks()

		bg_x1 -= scroll_speed*0.75
		if bg_x1 <= -1498:
			bg_x1 = 0
		bg_x2 -= scroll_speed * 0.50
		if bg_x2 <= -1498:
			bg_x2 = 0
		bg_x3 -= scroll_speed * 0.25
		if bg_x3 <= -1498:
			bg_x3 = 0
		ground_x1 -= scroll_speed*1.25
		if ground_x1 <=-900:
			ground_x1 = 0

		if time_now - last_pipe > pipe_frequency:
			pipe_height = random.randint(-100, 100)
			btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
			top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

		pipe_group.update()

	if game_over == True:
		if restart.draw() == True:
			game_over = False
			score = reset_game()
			best_score = best_score
			flying = True

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
			flying = True

	if score > best_score:
		best_score = score
		bs_file.seek(0)
		bs_file.write(str(best_score))


	pygame.display.update()

pygame.quit()
bs_file.close()
