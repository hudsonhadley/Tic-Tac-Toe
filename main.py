import pygame

from settings import WINDOW_SIZE, BACKGROUND_COLOR, BOARD_SIZE, BOARD_TOP_LEFT, BOARD_COLOR, SPOT_SIZE

from board import Board

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TicTacToe")

board = Board()


playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False



    screen.fill(BACKGROUND_COLOR)


    pygame.display.flip()

pygame.quit()
