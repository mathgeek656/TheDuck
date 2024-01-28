# Rebus puzzle
import pygame
import random
import time
from pygame.locals import (
    RLEACCEL,
    KEYDOWN,
    K_ESCAPE,
    QUIT,
    K_SPACE,
)

# initialize pygame
pygame.init()

#music
music = pygame.mixer.music.load('music/HappyGoLucky.mp3')

#screen width and height
SCREEN_WIDTH=600
SCREEN_HEIGHT=500

#Duck God
class Duck(pygame.sprite.Sprite):
    def __init__(self):
        super(Duck, self).__init__()
        self.surf = pygame.image.load("img/ducks_bowtie.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.x = int(SCREEN_WIDTH/2-16)
        self.y = SCREEN_HEIGHT-300
        self.rect = self.surf.get_rect(center= (self.x, self.y))

#Duck small
class Duck_small(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Duck_small, self).__init__()
        self.surf = pygame.image.load("img/duck_small.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect(center= (self.x, self.y))
        
#Duck red
class Duck_red(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Duck_red, self).__init__()
        self.surf = pygame.image.load("img/red_duck.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect(center= (self.x, self.y))
        
# ducks group
ducks = pygame.sprite.Group()
        
# draw text
def draw_text(surface, text, size, color, x, y):  
    font = pygame.font.SysFont ("Times", size, bold = True)
    label = font.render (text, 1, color)
    
    surface.blit(label,(x,y))

#the timer
start_time = time.time()
end_time = time.time()
#play game
def main(screen):
    # display screen
    running = True
    text1 = "Spawn Duck"
    text2 = "Lose"
    global start_time
    global end_time
    start_time = time.time()
    while running:
        # mouse
        mouse = pygame.mouse.get_pos()
        # /mouse
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if 10 < mouse[0] < 10+180:
                    if 350 < mouse[1] < 350+60:
                        if text1 == "Spawn Duck":
                            if random.randint(1,10) == 1:
                                red_duck = Duck_red(random.randint(10,SCREEN_WIDTH-10), random.randint(10,SCREEN_HEIGHT-150))
                                ducks.add(red_duck)
                                text1 = "Lose"
                                text2 = "Win"
                            else:
                                small_duck = Duck_small(random.randint(10,SCREEN_WIDTH-10), random.randint(10,SCREEN_HEIGHT-150))
                                ducks.add(small_duck)
                        else:
                            return "Lose"
                if 500 < mouse[0] < 500+90:
                    if 350 < mouse[1] < 350+60:
                        end_time = time.time()
                        return text2
                        
        screen.fill((64,100,200))
        
        #left button
        b_surf = pygame.Surface((180,60))
        b_surf.fill((162, 64, 227))
        screen.blit(b_surf,(10,350))
        draw_text(screen, text1, 30, (0,30,100), 20, 355)
        #\left button
        
        #right button
        b_surf = pygame.Surface((90,60))
        b_surf.fill((162, 64, 227))
        screen.blit(b_surf,(500,350))
        draw_text(screen, text2, 30, (0,30,100), SCREEN_WIDTH-85, 355)
        #\right button
        
        #spawns ducks
        for d in ducks:
            screen.blit(d.surf,d.rect)
        
        #display scrren
        pygame.display.flip()
    return "quit"

def main_menu():
    # display screen
    status = "neutral"
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    run = True
    duck = Duck()
    pygame.mixer.music.play(-1)
    while run:
        # mouse
        mouse = pygame.mouse.get_pos()
        # /mouse
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if int(SCREEN_WIDTH/2)-100 < mouse[0] < int(SCREEN_WIDTH/2)-100+270:
                    if 350 < mouse[1] < 350+70:
                        status = main(screen)
                        for d in ducks:
                            d.kill()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    for d in ducks:
                        d.kill()
        if status == "quit":
            run = False
        screen.fill((64,100,200))
        screen.blit(duck.surf,duck.rect)
        b_surf = pygame.Surface((170,70))
        b_surf.fill((162, 64, 227))
        screen.blit(b_surf,(int(SCREEN_WIDTH/2)-100,350))
        draw_text(screen, "PLAY", 40, (0,0,20), 230, 355)
        
        if status == "neutral":
            draw_text(screen, "Spawn the red duck and press the win button", 30, (0,0,20), 5, 5)
        elif status == "Lose":
            draw_text(screen, "Ha ha, you lose", 30, (0,0,20), 0, 0)
        elif status == "Win":
            time = str(round(end_time-start_time, 2))
            draw_text(screen, "You win! You took: " + time + " seconds", 30, (0,0,20), 0, 0)
        
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.quit()

pygame.display.set_caption('THE DUCK')
main_menu()
                
                
                
                
                
                
                
                