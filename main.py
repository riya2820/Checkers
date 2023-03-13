import pygame
import draft.py 

FPS = 60

WIN = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()
    #game = Game(WIN)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)

        '''
        if game.winner() != None:
            print(game.winner())
            run = False '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # row, col = get_row_col_from_mouse(pos)
                # game.select(row, col)

        # game.update()
    
    pygame.quit()

main()
