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

font = pygame.font.SysFont('arial', 36)

def display_font(screen, msg, color, pos):
    text_surface = font.render(msg, True, color)
    screen.blit(text_surface, pos)

def create_generation(bars, n):
    total_fitness = 0
    probabilities = []
    new_bars = []

    for bar in bars:
        total_fitness += bar.fitness
    for bar in bars:
        probabilities.append(bar.fitness / total_fitness)

    for i in range(n):
        stk = bars
        prob_stk = probabilities
        
        parent1 = random.choices(stk, weights=probabilities, k=1)[0]
        idx = stk.index(parent1)
        stk.pop(idx)
        prob_stk.pop(idx)

        parent2 = random.choices(stk, weights=probabilities, k=1)[0]

        offspring = parent1.reproduce(parent2)

        new_bars.append(offspring)

    return new_bars

def main():

    running = True
    bars = []
    n_bars = 10 
    for i in range(n_bars):
        bar = Bar(WIDTH // 2, X_LINE, 2, G)
        bars.append(bar)
    bar_idx = 0
    generation = 0
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(WHITE)
        display_font(SCREEN, "Generation : " + str(generation), (255, 165, 0), (0, 0))
        pygame.draw.line(SCREEN, BLACK, (0, X_LINE), (WIDTH, X_LINE), 2)
        bars[bar_idx].draw(screen = SCREEN, base_color = BLACK, bar_color = BROWN, pin_color = WHITE)
        
        
        bars[bar_idx].change_dynamic_params()
        bars[bar_idx].self_change_of_acc()
        
        if bars[bar_idx].fallen:
            bar_idx += 1

        if bar_idx >= n_bars:
            # bars = create_generation(bars)
            bar_idx = 0

        print(bar_idx)

        CLOCK.tick(FPS)
        pygame.display.flip()



if __name__ == '__main__':
    main()
