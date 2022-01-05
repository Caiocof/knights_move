from board.utilits import position_columns
from board.utilits import position_rows
from board.utilits import notation

from itertools import product


def knight_moves(data):
    col = data[:1]
    row = int(data[1:])

    columns = position_columns()
    rows = position_rows()

    if col not in columns or row not in rows:
        return {'error': True, 'message': 'position not found'}

    x = rows[row]
    y = columns[col]

    moves_k = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
    moves_k = [([notation(f'0{x}'), notation(f'1{y}')]) for x, y in moves_k if x >= 0 and y >= 0 and x < 8 and y < 8]

    moves = []
    for move in moves_k:
        moves.append(f'{move[1]}{move[0]}')

    # moves = [([x, y]) for x, y in moves_k if x >= 0 and y >= 0 and x < 8 and y < 8]
    # position = [x, y]
    # print_board([position, moves])

    return {'error': False, 'result': moves}


def print_board(datas):
    line = 8
    table = []
    for i in range(line):
        table.append(list('0' * 8))

    knight_position, move_position = datas

    x_position, y_position = knight_position

    table[x_position][y_position] = 'K'

    for move in move_position:
        x_move, y_move = move
        table[x_move][y_move] = 'M'

    for line in table:
        print(' '.join(line))
