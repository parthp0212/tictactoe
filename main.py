import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe!')

test_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

def VerticalLines():
    pygame.draw.line(screen, (0, 0, 0), [300, 100], [300, 700], 3)
    pygame.draw.line(screen, (0, 0, 0), [500, 100], [500, 700], 3)

def HorizontalLines():
    pygame.draw.line(screen, (0, 0, 0), [100, 300], [700, 300], 3)
    pygame.draw.line(screen, (0, 0, 0), [100, 500], [700, 500], 3)

def XPlayer(x, y):
    pygame.draw.line(screen, (0, 0, 0), [x - 50, y - 50], [x + 50, y + 50], 3)
    pygame.draw.line(screen, (0, 0, 0), [x - 50, y + 50], [x + 50, y - 50], 3)

def OPlayer(x, y):
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 50, 3)

def DrawBoard():
    for row in range(3):
        for column in range(3):
            x = 200 + column * 200
            y = 200 + row * 200
            if board[row][column] == "X":
                XPlayer(x, y)
            elif board[row][column] == "O":
                OPlayer(x, y)

def CheckWin():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return board[row][0]
        
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return board[0][column]
        
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[1][1]
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]

player1 = True
player2 = False
gameOver = False
winner = None

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

print(board)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            x, y = mouse_position # WORKS
            

            #subtract 100 to find the coords of the board, excludes the outside part
            #divide by 200 because each square is 200 x 200
            column = (x - 100) // 200
            row = (y - 100) // 200

            #COUNTER
            counter = 0


            #This is checked to see the which square the mouse button is exactly PRESSED.
            if 0 <= row < 3 and 0 <= column < 3:
                #Checks to see if that square is blank or not
                if board[row][column] == " ":
                    #If it is player 1's turn, then wherever they click in a box. IF EMPTY, X will be placed.
                    if player1:
                        board[row][column] = "X"
                        player1 = False
                        player2 = True
                        CheckWin()
                        print(board)
                    #If it is player 2's turn, then wherever they click in a box. IF EMPTY, O will be placed.   
                    elif player2:
                        board[row][column] = "O"
                        player2 = False
                        player1 = True
                        CheckWin()
                        print(board)
                    
                    result = CheckWin()
                    if result:
                        winner = result
                        gameOver = True
                        
    
    screen.fill((205, 205, 205))
    VerticalLines()
    HorizontalLines()
    DrawBoard()

    if gameOver:
        gameOverMessage = test_font.render(f"{winner} Wins!", True, (200, 0, 0))
        screen.blit(gameOverMessage, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
