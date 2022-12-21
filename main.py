import pygame

class Ball:
	def __init__(self, x ,y , radius):
		self.x = x
		self.y = y
		self.dX = 5
		self.dY = 10
		self.dYchange = 0.5  # this was controlled by the up an down arrows
		self.radius = radius

	def move(self):
		self.dY = self.dY * 0.98
		self.dY = self.dY + self.dYchange

		self.x = self.x + self.dX
		self.y = self.y + self.dY
		if self.y > 500 or self.y < 0:
			self.dY = -self.dY

		if self.x > 500 or self.x < 0:
			self.dX = -self.dX
	def draw(self):
		pygame.draw.circle(screen, (255, 255, 0), [self.x, self.y], self.radius)

ball = Ball(0,0,12)


pygame.init()
RED = (255,0,0)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball?")
clock = pygame.time.Clock()

done = False

myfont = pygame.font.SysFont("monospace", 15)

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			ball.dYchange = ball.dYchange - 0.05

		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			ball.dYchange = ball.dYchange + 0.05

	screen.fill(RED)
	# render text
	label = myfont.render("Use up and down arrows to control the bounce", True, (255, 255, 0))
	screen.blit(label, (10, 10))
	# print(dY, circleY)
	ball.move()
	ball.draw()


	pygame.display.flip()
	clock.tick(20)
pygame.quit()