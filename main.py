import pygame
# https://colab.research.google.com/drive/1OsMLEiYVjp33UbcxWRDMvi7p_cLXYqoS?usp=sharing

pygame.init()
RED = (255,0,0)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball?")
clock = pygame.time.Clock()

done = False
circleX = 250
circleY = 0
dX = 5
dY = 10
dYchange = 0.5 #this is controlled by the up an down arrows
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)




while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dYchange = dYchange - 0.05
            print(dYchange)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dYchange = dYchange + 0.05
            print(dYchange)
    screen.fill(RED)
    # render text
    label = myfont.render("Use up and down arrows to control the bounce", True, (255, 255, 0))
    screen.blit(label, (10, 10))
    dY = dY * 0.98
    dY = dY + dYchange

    circleY = circleY + dY
    circleX = circleX + dX
    if circleY + dY > 500 or circleY < 0:
        dY = -dY

    if circleX + dX > 500 or circleX < 0:
        dX = -dX
    # print(dY, circleY)
    pygame.draw.circle(screen,(255,255,0),[circleX,circleY],10)
    pygame.display.flip()
    clock.tick(20)
pygame.quit()