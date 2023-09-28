import pygame
import sys
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
pygame.display.set_caption("Ball and Tube")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
bojapozadine=(80,150,250)
screen.fill(bojapozadine)


class Particle:
    def __init__(self, pos, size):
        self.x, self.y = pos
        self.size = size
        self.colour = (255, 255, 255)
        self.thickness = 30
        self.speed=1
    def move(self):
        self.y+=self.speed

    def update(self, dt):
        pass
    def display(self):
        pygame.draw.line(screen,(50,50,120),(self.x-40,SCREEN_HEIGHT),(self.x-40,80),5)
        pygame.draw.line(screen,(50,50,120),(self.x+40,SCREEN_HEIGHT),(self.x+40,80),5)
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
        
lopta=Particle((400, 300), 30)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    dt = clock.tick(50)/1000
    
    
    lopta.display()
    pygame.display.flip()

pygame.mixer.quit()
pygame.quit()