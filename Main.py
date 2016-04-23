import Graphics
from Graphics import Display
from pygame import *
import pygame
from ParticleSource import ParticleSource
from Particle import Particle
import sys

winw = 3*1280//4
winh = 3*720//4
display = Display((winw, winh))

source = ParticleSource()
# source.emitParticles(10, 0.1, 10, 10)
source.generateParticleField(20, 100, (winw, winh))
pygame.display.set_caption("Gravity Simulator")

r = winw / 40

# pointMass1 = Particle(r + winw / 2, winh / 2, 100000, Graphics.BLUE)
# pointMass1.setVelocity(0, 20)
# pointMass2 = Particle(-r + winw / 2, winh / 2, 100000, Graphics.BLUE)
# pointMass2.setVelocity(0, -20)
#
# source.addParticle(pointMass1)
# source.addParticle(pointMass2)

pause = False
refresh = False
display.refresh()
display.setTimeDistortionFactor(display.timeDistortionFactor/2)

while (display.isRunning()):

	if refresh:
		display.refresh()

	for event in display.events:
		b1 = event.type == KEYDOWN or event.type == QUIT
		b2 = event.type == QUIT or event.type == K_ESCAPE
		if b1 and b2:
			pygame.quit()
			sys.exit()
			break

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if pause:
					pause = False
				else:
					pause = True

			if event.key == K_ESCAPE:
				display.stop()
				break

			if event.key == pygame.K_UP:
				display.setTimeDistortionFactor(display.timeDistortionFactor + 0.1)

			if event.key == pygame.K_DOWN:
				display.setTimeDistortionFactor(display.timeDistortionFactor - 0.1)

			if event.key == pygame.K_r:
				source.generateParticleField(20, 100, (winw, winh))
				display.fill(Graphics.BLACK)

			if event.key == pygame.K_x:
				refresh = not refresh

	source.draw(display)
	if not pause:
		source.update(display.getDelta())

	display.show()

pygame.quit()
sys.exit()
