import pygame


# define constants
WIDTH = 480
HEIGHT = 320
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 10

# WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ECS Project")


# function to set window fill color
def window_fill(color):
    WIN.fill(color)


# main driver function
def main():
    clock = pygame.time.Clock()
    run = True

    toggle = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        window_fill(WHITE)
        pygame.PixelArray(WIN)[240:, :160] = 0xFF0000
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()