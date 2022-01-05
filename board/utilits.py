def position_columns():
    return {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


def position_rows():
    return {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}


def colors():
    return ['black', 'white']


def notation(ax):
    position = int(ax[:1])
    value = int(ax[1:])

    columns = position_columns()
    rows = position_rows()

    if position == 0:
        return list(rows.keys())[list(rows.values()).index(value)]
    elif position == 1:
        return list(columns.keys())[list(rows.values()).index(value)]
