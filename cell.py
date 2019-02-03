import pygame.gfxdraw, pygame
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

class Cell(object):
	def __init__(self, i, j, w):
		self.i = i
		self.j = j
		self.w = w
		self.x = self.i * self.w
		self.y = self.j * self.w
		self.state = 0
		
	def render(self, screen):
		pygame.gfxdraw.rectangle(screen, (self.x, self.y, self.w, self.w), black)
		if self.state == 'X':
			pygame.draw.line(screen, red, (self.x, self.y), (self.x + self.w, self.y + self.w), 1)
			pygame.draw.line(screen, red, (self.x + self.w, self.y), (self.x, self.y + self.w), 1)
		elif self.state == 'O':
			pygame.draw.circle(screen, blue, (int(self.x + self.w * 0.5), int(self.y + self.w * 0.5)),
							   int(self.w * 0.5), 1)
	
	def contains(self, x, y):
		return self.x < x < self.x + self.w and self.y < y < self.y + self.w
	
	def drawX(self, screen):
		# pygame.draw.line(screen, red, (self.x, self.y), (self.x + self.w, self.y + self.w), 1)
		self.state = 'X'
	
	def drawO(self, screen):
		# pygame.draw.circle(screen, blue, (int(self.x + self.w * 0.5), int(self.y + self.w * 0.5)), int(self.w*0.5), 1)
		self.state = 'O'
	
	def check(self, player):
		# if player == 'X':
		# 	return self.state != 'X'
		# else:
		# 	return self.state != 'O'
		return self.state != 'X' and self.state != 'O'
	
		