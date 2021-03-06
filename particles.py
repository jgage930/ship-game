# this file will contain all the stuff for making particles
import pygame, random, math

class Particle:
    def __init__(self, x, y, xvel, yvel, radius, color) -> None:
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.radius = radius
        self.color = color

    def render(self, win):
        self.x += self.xvel
        self.y += self.yvel

        self.radius -= 0.5
        pygame.draw.circle(
            win,
            self.color,
            (self.x, self.y),
            self.radius
        )

class Explosion:

    def __init__(self, center:tuple) -> None:
        self.particles = []
        self.x, self.y = center
        self.colors = [
            (255, 0, 0),
            (255, 215, 0),
            (255, 69, 0)
        ]

        # render a finite number of particles
        for _ in range(random.randint(20, 50)):
            # pick a random angle
            theta = random.uniform(-1 * math.pi, math.pi)

            # pick a random speed
            speed = random.randint(5, 20)

            particle = Particle(
                self.x,
                self.y,
                speed * math.cos(theta),
                speed * math.sin(theta),
                random.randint(2, 15),
                random.choice(self.colors)
            )
            self.particles.append(particle)
    
    def drawParticles(self, screen):
        for particle in self.particles:
            particle.render(screen)
            if particle.radius <= 0:
                self.particles.remove(particle)