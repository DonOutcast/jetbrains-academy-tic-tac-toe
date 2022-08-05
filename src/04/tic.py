user_input = input()
array = [char if char in "XO" else "_" for char in user_input]


def print_grid(masiv: list) -> None:
    """This is function print your answer in grid game."""
    print("-" * 9 + "\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n".format(*stroka) + "-" * 9)


def o_wins(spisok: list) -> None:
    """This is function print how win and some rules in the game."""
    possible_wins = [spisok[0] + spisok[1] + spisok[2], spisok[3] + spisok[4] + spisok[5], spisok[6] + spisok[7] + spisok[8],
                     spisok[0] + spisok[3] + spisok[6], spisok[1] + spisok[4] + spisok[7], spisok[2] + spisok[5] + spisok[8],
                     spisok[0] + spisok[4] + spisok[8], spisok[2] + spisok[4] + spisok[6]]
    if 'X' * 3 in possible_wins and 'O' * 3 not in possible_wins:
        print("X wins")
    elif 'O' * 3 in possible_wins and 'X' * 3 not in possible_wins:
        print("O wins")
    elif "_" not in array:
        print("Draw")
    elif '_' in array and 'X' * 3 not in possible_wins and 'O' * 3 not in possible_wins and array.count("X") == array.count("O"):
        print("Game not finished")
    else:
        print("Impossible")
        

def cordination(masiv: list) -> None:
    cordination_x, cordination_y = input().split()
    if not cordination_x.isdigit() and not cordination_y.isdigit():
        print("You should enter numbers!")
    elif cordination_x > '3' or cordination_x < '1' or cordination_y > '3' or cordination_y < '1':
        print('Coordinates should be from 1 to 3!')
    

# print_grid(array)
# o_wins(array)
