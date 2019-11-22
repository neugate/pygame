import sys
import pygame
from pygame.locals import QUIT

DISPLAY_X = 1000
DISPLAY_Y = 600

pygame.init()
SURFACE = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
FPSCLOCK = pygame.time.Clock()

def main():
    display_load = 0
    sysfont = pygame.font.SysFont("Meiryo", 100)
    
    
    

    while True:
        display_load += 1
        count = "count:" + str(display_load)
        message = sysfont.render(count, True, (0,0,255))
        message_rect = message.get_rect(center=(DISPLAY_X/2, DISPLAY_Y/2))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        SURFACE.fill((255,255,255))
        SURFACE.blit(message, message_rect)
        pygame.display.update()
        FPSCLOCK.tick(1000)

if __name__ == "__main__":
    main()