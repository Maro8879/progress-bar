from os import system
from os import name
from math import floor


def progress_bar(data, process=None, cls=True, color='92'):
    system('color')
    elem_counter = 0
    print(f'\033[1;{color}m{0:.2f}% | [{"█" * floor(0) + "░" * int(100 - floor(0))}]\033[0;0m')
    for elem in data:
        # process
        process(elem) if process is not None else None
        # loading bar
        elem_counter += 1
        percent = elem_counter/len(data) * 100
        system('cls' if name == 'nt' else 'clear') if cls is True else ''
        print(f'\033[1;{color}m{percent:.2f}% | [{"█" * floor(percent) + "░" * int(100 - floor(percent))}]\033[0;0m')

