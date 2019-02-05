from cell import Cell
import pygame

pygame.init()

WHITE = (255, 255, 255)

size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')


# def isWinner(board):
# # 	for i in range(3):
# # 		row = {board[i][0].state, board[i][1].state, board[i][2].state}
# # 		if len(row) == 1 and board[i][0].state != 0:
# # 			return board[i][0]
# #
# # 	for i in range(3):
# # 		column = {board[0][i].state, board[1][i].state, board[2][i]}
# # 		if len(column) == 1 and board[0][i] != 0:
# # 			return board[0][i]
# #
# # 	diag1 = {board[0][0].state, board[1][1].state, board[2][2].state}
# # 	diag2 = {board[0][2].state, board[1][1].state, board[2][0].state}
# # 	if len(diag1) == 1 or len(diag2) == 1 and board[1][1] != 0:
# # 		return board[1][1]
# #
# # 	return 0


def iswinner(grid, player):
    return ((grid[0][0].state == grid[0][1].state == grid[0][2].state == player) or
            (grid[1][0].state == grid[1][1].state == grid[1][2].state == player) or
            (grid[2][0].state == grid[2][1].state == grid[2][2].state == player) or

            (grid[0][0].state == grid[1][0].state == grid[2][0].state == player) or
            (grid[0][1].state == grid[1][1].state == grid[2][1].state == player) or
            (grid[0][2].state == grid[1][2].state == grid[2][2].state == player) or

            (grid[0][0].state == grid[1][1].state == grid[2][2].state == player) or
            (grid[0][2].state == grid[1][1].state == grid[2][0].state == player))


def isTie(grid):
    for i in range(3):
        if grid[0][i].state == 0:
            return False
    for i in range(3):
        if grid[1][i].state == 0:
            return False
    for i in range(3):
        if grid[2][i].state == 0:
            return False
    return True


def main(won, tie):
    clock = pygame.time.Clock()
    w = 100
    board = [[Cell(i, j, w) for i in range(3)] for j in range(3)]
    player = 'X'
    done = False
    gameOver = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if not gameOver:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for i in range(3):
                        for j in range(3):
                            if board[i][j].contains(mouseX, mouseY):
                                if player == 'X' and board[i][j].check(player):
                                    board[i][j].drawX(screen)
                                    if won(board, player):
                                        print('{} has won'.format(player))
                                        gameOver = True
                                    elif tie(board):
                                        print('It is a tie!')
                                        gameOver = True
                                    elif not won(board, player) and not tie(board):
                                        player = 'O'

                                if player == 'O' and board[i][j].check(player):
                                    board[i][j].drawO(screen)
                                    if won(board, player):
                                        print('{} has won'.format(player))
                                        gameOver = True
                                    elif tie(board):
                                        print('It is a tie!')
                                        gameOver = True
                                    elif not won(board, player) and not tie(board):
                                        player = 'X'
        screen.fill(WHITE)
        [[board[i][j].render(screen) for i in range(3)] for j in range(3)]
        if gameOver:
            font = pygame.font.SysFont("Helevetica", 75)
            text = font.render('Game Over', 1, (0, 255, 0))
            screen.blit(text, (5, 140))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main(iswinner, isTie)
