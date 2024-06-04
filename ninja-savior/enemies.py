import pygame, random

class Enemy:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.size = 25

		self.imgs = ['sprites/ELeft.png','sprites/ERight.png']
		self.currentImg=self.imgs[0]

	def display(self,screen):
		img = pygame.transform.scale(pygame.image.load(self.currentImg),(self.size,self.size))
		screen.blit(img, (self.x,self.y))
		if self.currentImg == self.imgs[0]:
			self.currentImg = self.imgs[1]
		elif self.currentImg == self.imgs[1]:
			self.currentImg = self.imgs[0] 