import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("bg.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bee"] = pygame.image.load("bee.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
groundx=0

class Bee: 
    speed=5
    g=0.5
    bee= pygame.Rect(100,250,30,30)

    def gravity(self):
        self.speed=self.speed+self.g
        self.bee.y= self.bee.y + self.speed

    def flap(self): 
        self.speed=-10
    
    #Add a display() function to show the bee on the screen
        

bee=Bee()

while True:    
    screen.fill((50,150,255))
    screen.blit(images["bg"],[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bee.flap()
                        
    bee.gravity()
    
    groundx =groundx-5
    
    if groundx< -330:
        groundx=0

    screen.blit(images["bee"],bee.bee) 
    screen.blit(images["base"],[groundx,550])
    #Call the display() method of bee object to display the bee on the screen. 
      
    pygame.display.update()
    clock.tick(30)
    
    
    

