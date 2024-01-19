# Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов). Можете использовать как правила, так и хардкод, на своё усмотрение. 
# Главное, чтобы в игру можно было поиграть через терминал с вашего компьютера.

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(): 
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def play_game():
    current_player = 'X'
    while True:
        display_board()
        print(f"Ходит игрок {current_player}")
        row = int(input("Введите номер строки (от 0 до 2): "))
        col = int(input("Введите номер столбца (от 0 до 2): "))

        if board[row][col] != ' ':
            print("Недопустимый ход! Попробуйте еще раз.")
            continue

        board[row][col] = current_player

        winner = check_winner()
        if winner:
            display_board()
            print(f"Игрок {winner} победил!")
            break

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            display_board()
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()