import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROW, COL = 6, 7
PLAYER1_COLOR = (255, 0, 0)  # Red
PLAYER2_COLOR = (0, 0, 255)  # Blue
BG_COLOR = (255, 255, 255)  # White

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

# Set up font
font = pygame.font.Font(None, 36)

# Game variables
player_turn = 1
game_over = False
board = [[0 for _ in range(COL)] for _ in range(ROW)]

# Function to draw game board
def draw_board():
    screen.fill(BG_COLOR)
    for row in range(ROW):
        for col in range(COL):
            color = (200, 200, 200)  # Gray
            if board[row][col] == 1:
                color = PLAYER1_COLOR
            elif board[row][col] == 2:
                color = PLAYER2_COLOR
            pygame.draw.circle(screen, color, (col * 80 + 40, row * 80 + 40), 35)

# Function to check for win
def check_win(player):
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == player:
                # Check horizontal
                if col < COL - 3 and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                    return True
                # Check vertical
                if row < ROW - 3 and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                    return True
                # Check diagonal (top-left to bottom-right)
                if row < ROW - 3 and col < COL - 3 and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                    return True
                # Check diagonal (bottom-left to top-right)
                if row > 2 and col < COL - 3 and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                    return True
    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            col = event.pos[0] // 80
            for row in range(ROW - 1, -1, -1):
                if board[row][col] == 0:
                    board[row][col] = player_turn
                    if check_win(player_turn):
                        game_over = True
                        print(f"Player {player_turn} wins!")
                    player_turn = 2 if player_turn == 1 else 1
                    break

    draw_board()
    pygame.display.update()
