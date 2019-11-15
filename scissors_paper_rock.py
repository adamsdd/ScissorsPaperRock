import numpy as numpy

# n/n+1   P  K  N
#   P
#   K
#   N
historic_results = numpy.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])

# -1 = gamer won, 0 = draw, 1 = pc won
games_results = []

# Value is a beaten figure
winnerMap = {
    'K': 'N',
    'P': 'K',
    'N': 'P'
}


def get_beaten_figure(figure):
    return winnerMap.get(figure)


def get_winner(gamer_figure, pc_figure):
    win = None
    if gamer_figure == pc_figure:
        win = 0
    elif get_beaten_figure(gamer_figure) == pc_figure:
        win = -1
    else:
        win = 1

    games_results.append(win)
    return win


def get_index_for_matrix(figure):
    index = None
    if figure == 'P':
        index = 0
    elif figure == 'K':
        index = 1
    elif figure == 'N':
        index = 2

    return index


def get_figure_for_index(index):
    figure = None
    if index == 0:
        figure = 'P'
    elif index == 1:
        figure = 'K'
    elif index == 2:
        figure = 'N'

    return figure


def get_max_value_index_from_historic_for_first_index(index):
    return numpy.unravel_index(historic_results[index].argmax(), historic_results.shape).__getitem__(1)


def increment_historic_results(last_figure, current_figure):
    first_index = get_index_for_matrix(last_figure)
    second_index = get_index_for_matrix(current_figure)
    historic_results[first_index][second_index] += 1


def get_pc_figure(figure):
    first_index = get_index_for_matrix(figure)
    second_index = get_max_value_index_from_historic_for_first_index(first_index)
    return get_figure_for_index(second_index)


def translate_win(winner):
    result = None
    if winner == 0:
        result = 'Draw!'
    elif winner == 1:
        result = 'Pc Won!'
    elif winner == -1:
        result = 'Gamer Won!'

    return result


def main():
    last_input_figure = None
    game = 1
    while 1:
        print("Input your figure: ")
        input_figure = input().upper()
        if input_figure != 'K' and input_figure != 'P' and input_figure != 'N':
            print("Please, input correct figure (P or K or N)")
        else:
            if game == 1 or game == 2:
                pc_figure = 'P'
            else:
                pc_figure = get_pc_figure(last_input_figure)

            winner = get_winner(input_figure, pc_figure)
            print("Your value = " + input_figure)
            print("PC value = " + pc_figure)
            print(translate_win(winner))
            if last_input_figure is not None:
                increment_historic_results(last_input_figure, input_figure)

            last_input_figure = input_figure
            game += 1


main()
