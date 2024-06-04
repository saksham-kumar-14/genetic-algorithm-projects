import pygame, random
from player import Character
from enemies import Enemy

pygame.init()
WIDTH, HEIGHT = 1000,700
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("ninja savior")
CLOSE_WINDOW = False
CLOCK = pygame.time.Clock()
MODE = "AI"
LOST = False
mutationRate = 0.1

def set_text(string, coordx, coordy, fontsize, color):
    font = pygame.font.Font('freesansbold.ttf', fontsize) 
    text = font.render(string, True, color) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)

def startingScreen():
	global SCREEN,MODE,CLOSE_WINDOW
	btw,bth=100,75
	aix,aiy=200,HEIGHT//2
	aiColor, manualColor = (0,0,0),(0,0,0)
	manualx,manualy=WIDTH-200,HEIGHT//2
	m_text= set_text("MANUAL",(manualx*2+btw)//2,(manualy*2+bth)//2,16,(255,255,255))
	ai_text= set_text("AI",(aix*2+btw)//2,(aiy*2+bth)//2,16,(255,255,255))

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				CLOSE_WINDOW = True

		SCREEN.fill((255,255,255))

		ai = pygame.draw.rect(SCREEN,aiColor,pygame.Rect(aix,aiy,btw,bth))
		manual = pygame.draw.rect(SCREEN,manualColor,pygame.Rect(manualx,manualy,btw,bth))

		if aix<pygame.mouse.get_pos()[0]<aix+btw and aiy<pygame.mouse.get_pos()[1]<aiy+bth:
			aiColor = (100,100,100)
			if True in pygame.mouse.get_pressed():
				MODE = "AI"
				running = False
		else:
			aiColor = (0,0,0)
		if manualx<pygame.mouse.get_pos()[0]<manualx+btw and manualy<pygame.mouse.get_pos()[1]<manualy+bth:
			manualColor = (100,100,100)
			if True in pygame.mouse.get_pressed():
				MODE = "MANUAL"
				running = False
		else:
			manualColor = (0,0,0)


		SCREEN.blit(ai_text[0],ai_text[1])
		SCREEN.blit(m_text[0],m_text[1])

		CLOCK.tick(60)
		pygame.display.flip()


# main game


def main():
	global LOST, MODE,SCREEN, CLOSE_WINDOW
	running = True
	playersNO = 1
	enemiesNo = 5
	allEnemies = []
	time = 0
	temp = 0
	totalGenerations = 1
	for i in range(0,enemiesNo):
		new = Enemy( random.randrange(100,WIDTH),random.randrange(0,HEIGHT-100) )
		allEnemies.append(new)

	if MODE == "MANUAL":
		player = Character(WIDTH,HEIGHT,WIDTH-75,150)
	elif MODE == "AI":
		playersNo = 10
		allPlayers = []
		for i in range(playersNo):
			new = Character(WIDTH,HEIGHT,WIDTH-75,150)
			allPlayers.append(new)



	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				CLOSE_WINDOW = True

		#background
		SCREEN.fill((200,200,200))
		pygame.draw.rect(SCREEN,(0,200,0),pygame.Rect((WIDTH-75),75,75,75))


		# player stuff
		if MODE == "AI":
			for i in allPlayers:
				print(i.fitness,i.x,i.y)
			print("ffffffffffffffffffffffffffffffffffffffffffffffffffffff")
		if MODE == "MANUAL":
			player.actions(MODE)
			player.display(SCREEN)
		elif MODE == "AI":
			for i in range(0,len(allPlayers)):
				if not allPlayers[i].lost:
					allPlayers[i].actions(MODE)
					allPlayers[i].display(SCREEN)


		# enemies
		for i in range(0,len(allEnemies)):
			allEnemies[i].display(SCREEN)

			if MODE == "MANUAL":
				if player.isDead(allEnemies[i],WIDTH,HEIGHT):
					LOST = True
					running = False
			if MODE == "AI":
				aliveFound = False
				for j in allPlayers:
					j.isDead(allEnemies[i],WIDTH,HEIGHT)

					if j.lost == False:
						aliveFound = True

				LOST = not aliveFound

		# game win
		if MODE == "MANUAL":
			if player.x > WIDTH-75 and player.y < 150:
				LOST = False
				running = False
		else:
			for j in allPlayers:
				if j.x > WIDTH-75 and j.y < 150:
					LOST = False 
					running = False


		# time counter
		temp += 1
		if temp == 60:
			time += 1
			temp = 0

			if MODE == "AI":
				for i in allPlayers:
					if not i.lost:
						i.fitness += 1


		# making new generations for Ai and rejecting parents on basis of time taken
		if (MODE == "AI" and LOST) or time>20:
			print("new generation creating...................................")
			matingPool = []
			for i in range(0,len(allPlayers)):
				for j in range(0,allPlayers[i].fitness):
					matingPool.append(allPlayers[i])
				a= random.choice(matingPool)
				b= random.choice(matingPool)
				child = a.reproduce(b,mutationRate)
				allPlayers[i] = child

			totalGenerations += 1
			LOST = False
			time = 0

		t = set_text("TIME: "+str(time),WIDTH//2,25,16,(0,0,0))
		SCREEN.blit(t[0],t[1])
		t = set_text("Total Generation: "+str(totalGenerations),200,25,20,(0,0,0))
		SCREEN.blit(t[0],t[1])

		CLOCK.tick(120)
		pygame.display.flip()

def gameOver():
	global SCREEN
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		t = set_text("GAME OVER", WIDTH//2,HEIGHT//2,50,(255,100,100))
		SCREEN.blit(t[0],t[1])
		pygame.display.flip()

def gameWin():
	global SCREEN
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		t = set_text("GAME WIN", WIDTH//2,HEIGHT//2,50,(255,255,100))
		SCREEN.blit(t[0],t[1])
		pygame.display.flip()


if __name__ == '__main__':
	startingScreen()
	print(MODE)
	print(CLOSE_WINDOW)

	if not CLOSE_WINDOW:
		main()

	if not CLOSE_WINDOW:
		if LOST:
			gameOver()
		else:
			gameWin()

	pygame.quit()