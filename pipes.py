from settings import *
from difficult import diff



class Pipe(pygame.sprite.Sprite):

	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/pipe1.png')
		self.rect = self.image.get_rect()

		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_gap/(1 + (diff()/5)))]
		if position == -1:
			self.rect.topleft = [x, y + int(pipe_gap/(1 + (diff()/5)))]

	def update(self):
		self.rect.x -= scroll_speed + diff()
		if self.rect.right < 0:
			self.kill()
