import pygame
import math
import random
import time
import sys
import os



SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



pygame.init()
pygame.display.set_caption("Ball and Tube")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


bojapozadine=(80,150,250)
screen.fill(bojapozadine)

high=100
low=SCREEN_HEIGHT

fps=60

g=9.81
ro_vazduha=1.3
v_vazduha=0


desired_height=200
kd = -1
kv =  0.02

max_dv=0.1




class Slider:
    
    def __init__(self, x, y, width, height, color, min_value, max_value):
        
        self.outline = pygame.Rect(x, y, width, height)
        self.handle = pygame.Rect(x, y - height, height * 2, height * 3)
        
        self.color = color
        
        self.min_value = min_value
        self.max_value = max_value
        
        self.value = min_value

    
    def draw(self, screen):
        
        pygame.draw.rect(screen, BLACK, self.outline)
        pygame.draw.rect(screen, self.color, self.handle)

    
    def update(self):
        
        if pygame.mouse.get_pressed()[0] and self.handle.collidepoint(pygame.mouse.get_pos()):
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            self.handle.centerx = mouse_x
            
            self.handle.clamp_ip(self.outline)
            
            self.value = (self.handle.centerx - self.outline.x) / self.outline.width * (self.max_value - self.min_value) + self.min_value

    
    def get_value(self):
        return self.value
    


font = pygame.font.Font(None, 32)
slider = Slider(100, 200, 200, 20, RED, 0, 900)







class Particle:
    def __init__(self, pos, speed, mass, r):
        
        self.size = 2*r*100
        self.colour = (255, 255, 255)
        self.thickness = 2*r*100
        

        self.x, self.y = pos
        self.speed=speed
        self.acceleration=0
        
        self.mass=mass
        self.r=r
        self.v_loptice=(4/3)*self.r**3*math.pi
        self.v0=math.sqrt(4*(self.mass*g-ro_vazduha*g*self.v_loptice)/(ro_vazduha*self.r**2*math.pi))
        


    def flip_y(self):
        self.speed*=-0.5
        self.y += self.speed/fps

    def move(self):
        self.y+=self.speed/fps

    def update(self):
        self.acceleration=g*((lopta.mass-ro_vazduha*lopta.v_loptice)/lopta.mass) - (ro_vazduha*lopta.r**2*math.pi)/(4*lopta.mass)*(2*v_vazduha*lopta.v0-lopta.v0**2)
        self.speed=self.speed+self.acceleration
        if self.y>low-100*2*lopta.r:
            self.flip_y()
        self.move()

    def display(self):
        self.x=int(self.x)
        pygame.draw.line(screen,(0,0,0),(self.x+60,desired_height),(self.x+80,desired_height),5)
        pygame.draw.line(screen,(50,50,120),(self.x-40,SCREEN_HEIGHT),(self.x-40,80),5)
        pygame.draw.line(screen,(50,50,120),(self.x+40,SCREEN_HEIGHT),(self.x+40,80),5)
        pygame.draw.circle(screen, self.colour, (self.x, int(self.y)), int(self.size), int(self.thickness))
        






lopta=Particle((400, SCREEN_HEIGHT-200), 0,0.0027,0.02)
x=0





while running: 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    desired_v_vazduha = lopta.v0 + (desired_height - lopta.y) / 100 * kd + lopta.speed * kv

    if desired_v_vazduha>v_vazduha:
        if (desired_v_vazduha-v_vazduha)>max_dv:
            v_vazduha+=max_dv
        else:
            v_vazduha=desired_v_vazduha

    if desired_v_vazduha<v_vazduha:
        if (-desired_v_vazduha+v_vazduha)>max_dv:
            v_vazduha-=max_dv
        else:
            v_vazduha=desired_v_vazduha


    
    # x=float(slider.get_value())
    # dt = clock.tick(60)/1000
    slider.update()
    desired_height=SCREEN_HEIGHT-slider.get_value()
    screen.fill(bojapozadine)
    slider.update()
    text = font.render(f"Value: {slider.get_value():.2f}", True, BLACK)
    text2=font.render(f"motor intensity: {v_vazduha:.4f}",True,BLACK)
    slider.draw(screen)
    screen.blit(text, (100, 250))
    screen.blit(text2, (700, 350))



    lopta.update()
    lopta.display()
    pygame.display.flip()
    time.sleep(1/fps)







print(low-high)
# Visina tube je 830 piksela


pygame.quit()