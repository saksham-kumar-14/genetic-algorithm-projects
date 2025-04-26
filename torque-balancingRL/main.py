import pygame
from bar import Bar

pygame.init()
pygame.display.set_caption("Reinforcement learning example")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (210, 105, 30)
WIDTH, HEIGHT = 1200, 650
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
X_LINE = HEIGHT - 100

G = 9.8
FPS = 60 
CLOCK = pygame.time.Clock()

def main():

    running = True
    bar = Bar(WIDTH // 2, X_LINE, 2, G)
    print(bar.dna.actions)
              
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(WHITE)
        pygame.draw.line(SCREEN, BLACK, (0, X_LINE), (WIDTH, X_LINE), 2)
        bar.draw(screen = SCREEN, base_color = BLACK, bar_color = BROWN, pin_color = WHITE)
        bar.change_dynamic_params()
        bar.self_change_of_acc()

        CLOCK.tick(FPS)
        pygame.display.flip()



if __name__ == '__main__':
    main()
