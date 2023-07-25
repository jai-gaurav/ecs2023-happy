import pygame
from random import choice

# define constants
WIDTH = 480
HEIGHT = 320
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 24
EXPRESSIONS = ["LOOK_LEFT"]
IDLETIME = 100

# global variables
frame = 0
animationOngoing = False
cur_emotion = "IDLE"

# WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ECS Project")


########################
### CUSTOM FUNCTIONS ###
########################

# function to display emotion sprite
def dispEmote(emoteName):
    global frame
    global animationOngoing
    global cur_emotion
    path = "Expressions\\{folder}\\{emotion}_{frame_no}.png".format(
        folder = emoteName.capitalize(), 
        emotion = emoteName.lower(),
        frame_no = frame
        )
    
    try:
        img = pygame.image.load(path).convert()
        WIN.blit(img, (0, 0))
        pygame.display.update()
        frame += 1
    except FileNotFoundError:
        frame = 0
        animationOngoing = False
        cur_emotion = "IDLE"
    
    
    

# main driver function
def main():
    global frame
    global animationOngoing
    global cur_emotion
    clock = pygame.time.Clock()
    run = True
    tick = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # logic to change to new expression
        if not(animationOngoing) and (tick==0):
            animationOngoing = True
            cur_emotion = choice(EXPRESSIONS)
            print("New expression:", cur_emotion)
        
        dispEmote(cur_emotion)
        tick = (tick+1)%IDLETIME

    pygame.quit()


if __name__ == "__main__":
    main()