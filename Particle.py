import math

class Particle:

	def __init__(self, x, y, m, c):
		self.s = (x, y)
		self.v = (0, 0)
		self.a = (0, 0)
		self.f = (0, 0)
		self.m = m
		self.c = c

		self.trail = []
		self.trailLength = 5

	def update(self, delta):
		(fx, fy) = self.f
		(ax, ay) = self.a
		(vx, vy) = self.v
		(sx, sy) = self.s

		ax = fx / self.m
		ay = fy / self.m
		self.a = (ax, ay)

		vx += ax * delta
		vy += ay * delta
		self.v = (vx, vy)

		sx += vx * delta
		sy += vy * delta
		self.s = (sx, sy)

		self.trail.append((sx, sy))
		if len(self.trail) > self.trailLength:
			self.trail.pop(0)

	def draw(self, display):
		(sx, sy) = self.s
		display.drawPixel(sx, sy, self.c)
		for p in self.trail:
			(x, y) = p
			display.drawPixel(x, y, self.c)

	def getMass(self):
		return self.m

	def getPosition(self):
		return self.s

	def setPosition(self, sx, sy):
		self.s = (sx, sy)

	def setVelocity(self, vx, vy):
		self.v = (vx, vy)

	def setAcceleration(self, ax, ay):
		self.a = (ax, ay)

	def setForce(self, f):
		self.f = f

	def addForce(self, f):
		(f1x, f1y) = self.f
		(f2x, f2y) = f
		self.f = (f1x + f2x, f1y + f2y)

	def gravitationalAttrationTo(self, p):
		G = 1
		(px, py) = p.getPosition()
		(x, y) = self.s
		dx = (px - x)
		dy = (py - y)
		rS = (dx*dx + dy*dy)

		rS *= 50.0
		mF = G * p.m * self.m / rS
		r = math.sqrt(rS)

		return (mF * dx / r, mF * dy / r)
