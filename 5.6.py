print('^'*7, "Крестики-нолики", '^'*7)

board = list(range(1, 10))
field = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
rows = ['A', 'B', 'C']


def draw_board(board):
    print('_'*11)
    print('   1  2  3')
    for i in range(3):
        print(rows[i], '', field[i*3], '', field[i*3+1], '', field[i*3+2])
    print('_'*11)


def game_input(player_input):
    correct_input = False
    while not correct_input:
        player_answer = input('Очередь игрока ' + player_input + '. Введите номер клетки начиная с латинской буквы: ')
        if len(player_answer) != 0:
            if player_answer[0].upper() in 'ABC':
                try:
                    int(player_answer[1:])
                except:
                    print('Некорректно введен второй символ. Попробуйте еще раз.')
                    continue
                if 1 <= int(player_answer[1:]) <= 3:
                    if player_answer[0].upper() == 'A':
                        player_answer = int(player_answer[1])
                    elif player_answer[0].upper() == 'B':
                        player_answer = int(player_answer[1]) + 3
                    elif player_answer[0].upper() == 'C':
                        player_answer = int(player_answer[1]) + 6
                    else:
                        print('Клетки с таким комером нет. Попробуйте еще раз.')
                        continue
                else:
                    print('Клетки с таким комером нет. Попробуйте еще раз.')
                    continue
            else:
                print('Некорректно введен первый символ. Попробуйте еще раз.')
                continue
        else:
            print('Вы ничего не ввели. Попробуйте еще раз.')
            continue
        if str(field[player_answer - 1]) not in 'XO':
            field[player_answer - 1] = player_input
            board[player_answer - 1] = player_input
            correct_input = True
        else:
            print('Эта клетка уже занята. Попробуйте еще раз.')


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)
                 )
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def xo_game(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            game_input('X')
        else:
            game_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print('Игрок ' + str(tmp) + ' выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_board(board)


xo_game(board)

input('Нажмите Enter для выхода: ')