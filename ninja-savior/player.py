import math,pygame,random

# encoding movement information for AI
class DNA():
	def __init__(self):
		self.moves = []

	def evolution(self,newInfo):
		self.moves.append(newInfo)


def mutate(mutationRate):
	if random.random() < mutationRate:
		return random.randrange(0,4)



# character object coding
class Character():
	def __init__(self,WIDTH,HEIGHT,tx,ty):
		self.size = 25
		self.x = self.size*2
		self.y = HEIGHT//2
		self.vel = 20
		self.pLeft = ['player_left_1','player_left_2','player_left_3','player_left_4','player_left_5',]
		self.pRight = ['player_right_1','player_right_2','player_right_3','player_right_4','player_right_5']
		self.imgs=self.pRight
		self.currentImg=0
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT

		# for AI specific
		self.lost = False
		self.tx, self.ty = tx,ty
		self.maxDis = math.sqrt( (self.x-self.tx)**2 + (self.y-self.ty)**2 )
		self.fitness = int((2 - (math.sqrt( (self.x-self.tx)**2 + (self.y-self.ty)**2 ))/(self.maxDis) )*100)
		self.dna = DNA()
		self.dnaMovesDone = 0


	def actions(self,mode):
		if mode == "MANUAL":
			if pygame.key.get_pressed()[pygame.K_LEFT]:
				self.x-=self.vel
				self.imgs = self.pLeft
				if self.currentImg ==0 or self.currentImg ==1:
					self.currentImg = 2
				else:
					self.currentImg += 1
					if self.currentImg == len(self.imgs):
						self.currentImg = 2
			elif pygame.key.get_pressed()[pygame.K_RIGHT]:
				self.x+=self.vel
				self.imgs= self.pRight
				if self.currentImg ==0 or self.currentImg ==1:
					self.currentImg = 2
				else:
					self.currentImg += 1
					if self.currentImg == len(self.imgs):
						self.currentImg = 2

			elif pygame.key.get_pressed()[pygame.K_UP]:
				self.y -= self.vel
				if self.currentImg ==0 or self.currentImg ==1:
					self.currentImg = 2
				else:
					self.currentImg += 1
					if self.currentImg == len(self.imgs):
						self.currentImg = 2
			elif pygame.key.get_pressed()[pygame.K_DOWN]:
				self.y += self.vel
				if self.currentImg ==0 or self.currentImg ==1:
					self.currentImg = 2
				else:
					self.currentImg += 1
					if self.currentImg == len(self.imgs):
						self.currentImg = 2
			else:
				if self.currentImg == 0 :
					self.currentImg=1
				elif self.currentImg == 1:
					self.currentImg=0
				else:
					self.currentImg = 0

		elif mode == "AI":
			if self.dnaMovesDone == len(self.dna.moves):
				t = random.randrange(0,4)
				if t == 0:
					self.x += self.vel
				elif t == 1:
					self.x-=self.vel
				elif t == 2:
					self.y += self.vel
				elif t==3:
					self.y-=self.vel

				self.dna.evolution(t)
				self.fitness = int((2 - (math.sqrt( (self.x-self.tx)**2 + (self.y-self.ty)**2 ))/(self.maxDis) )*100)
			else:
				t = self.dna.moves[self.dnaMovesDone]
				if t == 0:
					self.x += self.vel
				elif t == 1:
					self.x-=self.vel
				elif t == 2:
					self.y += self.vel
				elif t==3:
					self.y-=self.vel

				self.dnaMovesDone += 1
				self.fitness = int((2 - (math.sqrt( (self.x-self.tx)**2 + (self.y-self.ty)**2 ))/(self.maxDis) )*100)


	def isDead(self,enemy,WIDTH,HEIGHT):
		if self.x < 0 or self.x > WIDTH-self.size or self.y < 0 or self.y>HEIGHT-self.size:
			self.lost = True
			return True
		elif self.isCollide(enemy):
			self.lost = True
			return True
		else:
			return False

	def isCollide(self,enemy):
		if enemy.x< self.x < enemy.x+enemy.size and enemy.y<self.y<enemy.y+enemy.size:
			return True
		else:
			return False


	def display(self, screen):
		img = pygame.transform.scale(pygame.image.load("sprites/"+self.imgs[self.currentImg]+".png"),(self.size,self.size))
		screen.blit(img, (self.x,self.y))


	def reproduce(self,partner,mutationRate):
		child = Character(self.WIDTH,self.HEIGHT,self.WIDTH-75,150)
		mid = len(self.dna.moves)//2
		child.dna.moves = self.dna.moves[:mid] + partner.dna.moves[mid+1:]
		for i in range(0,len(child.dna.moves)):
			result = mutate(mutationRate)
			if result != None:
				child.dna.moves[i] = result

		return child
