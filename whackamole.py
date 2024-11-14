import pygame
import random


def main():
    try:
        pygame.init()

        #set screen size and initial parameters
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        #grab mole
        mole_image = pygame.image.load("mole.png")

        #starting screen
        screen.fill("light green")

        #mole initial position
        x_pos = 0
        y_pos = 0
        screen.blit(mole_image, mole_image.get_rect(topleft=(x_pos, y_pos)))

        #main
        while running:
            for event in pygame.event.get():
                #closes game if 'x' window close
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #getting event of mouse click
                    (x,y) = event.pos
                    #comparing it to the position of mole, and setting new location
                    if (x//32, y//32) == (x_pos,y_pos):
                        screen.fill("light green")
                        x_pos = random.randrange(0, 20)
                        y_pos = random.randrange(0, 16)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(x_pos * 32, y_pos * 32)))


            #draw horizontal lines
            for x in range(0, 640, 32):
                pygame.draw.line(screen, "darkgreen", (x,0), (x,640), 1)
            #draw vertical lines
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "darkgreen", (0,y), (640,y), 1)

            #updates screen
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
