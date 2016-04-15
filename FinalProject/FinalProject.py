import pygame
import random

#Open the settings and highscore files then read and assign them to variables
settings_file = open("settings.txt", "r+")
highscore_file = open("highscore.txt", "r+")
windowx = int(settings_file.readline())
windowy = int(settings_file.readline())
highscore = highscore_file.readline()

pygame.init()  #initialize pygame

screen = pygame.display.set_mode((windowx, windowy))

circle_list = pygame.sprite.Group()

class Circle(pygame.sprite.Sprite):  #Class for clickable circle
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("circle.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
    

def placement():
    global makeCircle
    makeCircle = Circle()
    makeCircle.rect.x = random.randrange(windowx)
    makeCircle.rect.y = random.randrange(windowy)
    if makeCircle.rect.left < 0:
        makeCircle.rect.left = 0
    if makeCircle.rect.top < 0:
        makeCircle.rect.top = 0
    if makeCircle.rect.right > windowx:
        makeCircle.rect.right = windowx
    if makeCircle.rect.bottom > windowy:
        makeCircle.rect.bottom = windowy   
    circle_list.add(makeCircle)
 
       
def game():
    pygame.display.set_caption("Click Circle")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    placement()
    clock = pygame.time.Clock()
    done = True
    start_time = pygame.time.get_ticks()  #Starting time for timer
    score = 0  #Initiate score
    
    while done:
        time = (pygame.time.get_ticks()-start_time)/1000  #Get current timer time

        clock.tick(60)
        global makeCircle, highscore
        if time <= 60:
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                
                    if pos[0] > makeCircle.rect.left and pos[0] < makeCircle.rect.right and pos[1] > makeCircle.rect.top and pos[1] < makeCircle.rect.bottom:
                        circle_list.remove(makeCircle)
                        score += 1
                        screen.blit(background, (0, 0))
                        placement()

                elif event.type == pygame.QUIT:
                    done = False
            circle_list.draw(screen)
        else:
            circle_list.remove(makeCircle)
            screen.blit(background, (0, 0))
            myfont = pygame.font.SysFont(None, 36)
            label = myfont.render("You Scored: %d" % (score), 1, (255, 255,255))
            labelpos = label.get_rect()
            labelpos.centerx = screen.get_rect().centerx
            labelpos.centery = screen.get_rect().centery
            screen.blit(label, labelpos)
            if score < int(highscore):
                highscore_label = myfont.render("The Highscore is: %s" % (highscore), 1, (255, 255,255))
                highpos = highscore_label.get_rect()
                highpos.centerx = screen.get_rect().centerx
                highpos.centery = screen.get_rect().centery + 30
                screen.blit(highscore_label, highpos)
            else:
                highscore_label = myfont.render("You Got A New Highscore, Old Highscore: %s" % (highscore), 1, (255, 255,255))
                highpos = highscore_label.get_rect()
                highpos.centerx = screen.get_rect().centerx
                highpos.centery = screen.get_rect().centery + 30
                screen.blit(highscore_label, highpos)
                highscore_file.seek(0, 0)
                s = str(score)
                highscore_file.write(s)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
        pygame.display.flip()
    
  
if __name__ == "__main__":
    game()
    settings_file.close()
    highscore_file.close()