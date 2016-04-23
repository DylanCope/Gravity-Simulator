from Particle import Particle
import random

class ParticleSource:

    def __init__(self, x=0, y=0):
        self.particles = []
        self.x = x
        self.y = y
        self.particlesToEmit = []
        self.depenseRate = 0

    def emitParticles(self, num, dispenseRate, vMax, dim):
        (vxMax, vyMax) = vMax
        (winw, winh) = dim
        self.dispenseRate = dispenseRate
        self.particlesToEmit = []
        while emitted < num:

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            c = (r, g, b)

            x = random.randint(0, winw)
            y = random.randint(0, winh)

            newParticle = Particle(x, y, 1, c)

            vx = random.randint(-vxMax, vxMax)
            vy = random.randint(-vyMax, vyMax)

            newParticle.setVelocity(vx, vy)
            self.particlesToEmit.append(newParticle)

    def generateParticleField(self, num, vMax, dim):
        (winw, winh) = dim
        self.particles = []
        for i in range(0, num):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            c = (r, g, b)

            x = random.randint(0, winw)
            y = random.randint(0, winh)

            newParticle = Particle(x, y, random.randint(100, 1000), c)

            vx = random.randint(-vMax, vMax)
            vy = random.randint(-vMax, vMax)

            newParticle.setVelocity(vx, vy)

            self.particles.append(newParticle)

        sun1 = Particle(7*winw / 16, winh / 2, 10e7, (255, 255, 100))
        sun1.setVelocity(0, 40)
        sun2 = Particle(9*winw / 16, winh / 2, 10e7, (255, 255, 100))
        sun2.setVelocity(0, -40)
        self.particles.append(sun1)
        self.particles.append(sun2)

    def addParticle(self, p):
        self.particles.append(p)

    def update(self, delta):

        if len(self.particlesToEmit) > 0:
            n = int(self.dispenseRate * delta)
            i = 0
            while i < n:
                i += 1
                self.particles.append(self.particlesToEmit.pop())

        for p1 in self.particles:
            p1.setForce((0, 0))
            for p2 in self.particles:
                if p1.s != p2.s:
                    p1.addForce(p1.gravitationalAttrationTo(p2))

            p1.update(delta)

    def draw(self, display):
        for p1 in self.particles:
            p1.draw(display)
