import pygame
from random import choice
import expressions

# define constants
WIDTH = 480
HEIGHT = 320
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 24
EXPRESSIONS = [
    expressions.IDLE,
    expressions.LOOK_LEFT,
    expressions.LOOK_RIGHT,
    expressions.LOOK_UP,
    expressions.LOOK_DOWN,
    expressions.LOOK_TOP_LEFT,
    expressions.LOOK_TOP_RIGHT,
    expressions.LOOK_BOTTOM_LEFT,
    expressions.LOOK_BOTTOM_RIGHT
    ]
IDLETIME = 10
VELOCITY = 5

# global variables
frame = 0
animationOngoing = False
cur_expression = expressions.IDLE
left_eye_cord = [140, 80]
right_eye_cord = [280, 80]
left_eye_vel = [0, 0]
right_eye_vel = [0, 0]

targetCoords = [[140, 80], [280, 80]]
currentCoords = [[140, 80], [280, 80]]


# WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ECS Project")


########################
### CUSTOM FUNCTIONS ###
########################

# function to update target coordinates
def updateTargetCoords(expression):
    global targetCoords
    targetCoords[0][0] = expression.left_eye_x
    targetCoords[0][1] = expression.left_eye_y
    targetCoords[1][0] = expression.right_eye_x
    targetCoords[1][1] = expression.right_eye_y
    

# function to move eyes to target coordinates
def updateCurrentCoords():
    global targetCoords
    global currentCoords
    global VELOCITY
    
    # function to update current coordinates
    def updateCoords(eye_ind, axis_ind):
        if currentCoords[eye_ind][axis_ind] < targetCoords[eye_ind][axis_ind]:
            currentCoords[eye_ind][axis_ind] += VELOCITY
            if currentCoords[eye_ind][axis_ind] > targetCoords[eye_ind][axis_ind]:
                currentCoords[eye_ind][axis_ind] = targetCoords[eye_ind][axis_ind]
    
        elif currentCoords[eye_ind][axis_ind] > targetCoords[eye_ind][axis_ind]:
            currentCoords[eye_ind][axis_ind] -= VELOCITY
            if currentCoords[eye_ind][axis_ind] < targetCoords[eye_ind][axis_ind]:
                currentCoords[eye_ind][axis_ind] = targetCoords[eye_ind][axis_ind]
        
    # moving left eye along X and Y axis
    updateCoords(0, 0)
    updateCoords(0, 1)
    
    # moving right eye along X and Y axis
    updateCoords(1, 0)
    updateCoords(1, 1)
    
    # print("Current:", currentCoords)


# function to display an eye
def dispEye(eye, eyeType='idle'):
    global currentCoords
    
    path = "Expressions\\Eye\\{Type}.png".format(Type = eyeType)
    try:
        img = pygame.image.load(path).convert_alpha()
    except FileNotFoundError:
        path = "Expressions\\Eye\\idle.png"
        img = pygame.image.load(path).convert_alpha()
            
    if eye == 'left':
        WIN.blit(img, currentCoords[0])
    elif eye == 'right':
        WIN.blit(img, currentCoords[1])



# main driver function
def main():
    global frame
    global animationOngoing
    global cur_expression
    global targetCoords, currentCoords
    clock = pygame.time.Clock()
    run = True
    tick = 0

    # intial starter position
    path = "Expressions\\Eye\\idle.png"
    img = pygame.image.load(path).convert_alpha()
    WIN.fill(WHITE)
    WIN.blit(img, currentCoords[0])
    WIN.blit(img, currentCoords[1])
    pygame.display.update()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # change expression if animation not in progress
        if not(animationOngoing) and (tick==0):
            animationOngoing = True
            cur_expression = choice(EXPRESSIONS)
            # cur_expression = expressions.Expression("Cross_Eyed", )
            print("New expression:", cur_expression.getName())
            print("Target:", cur_expression.getCoords())
            updateTargetCoords(cur_expression)
            
        if targetCoords == currentCoords:
            animationOngoing = False
        else:
            WIN.fill(WHITE)
            updateCurrentCoords()
            dispEye('left')
            dispEye('right')
        
        tick = (tick+1)%IDLETIME
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()