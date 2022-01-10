# CSE 210 W02 Prove: Solo Code Submission - Tic Tac Toe
# Author(s): Jared Brooks. 

import math

def main():

    run_game = True
    turn = 0
    
    grid_size = int(input(f"How big of a grid would you like to play tic tac toe on? "))
    spacing = round(math.log((grid_size**2), 10) + 0.5)
    game_state = create_initial_state(grid_size)

    while run_game == True:
        game_state, turn, run_game, winner = game_step(game_state, turn, grid_size, spacing)

    screen_print(game_state, spacing, grid_size)
    print(f"Congratulations to player {winner} for winning!\n")



def game_step(game_state, turn, grid_size, spacing):
    """This function will move the game along by one turn."""
    screen_print(game_state, spacing, grid_size)

    game_state, turn, win_combo = do_move(game_state, turn, grid_size)

    run_game, winner = check_for_winner(win_combo) 

    

    return game_state, turn, run_game, winner

    

def screen_print(game_state, spacing, grid_size):
    """Prints the screen of the game so the player can visualize it."""
    i_count = 0
    for i in game_state:
        i_count += 1
        for j in range(len(i)):

            if j + 1 != len(i):

                # Incorporate this? {:>5d}
                # {:>`spacing`d}

                printed_digit = i[j]
                if isinstance(printed_digit, int):
                    printed_digit += 1
                print(f" {printed_digit} |", end="")

            elif j + 1 == len(i):
                printed_digit = i[j]
                if isinstance(printed_digit, int):
                    printed_digit += 1
                print(f" {printed_digit}")

        if grid_size == 2 and i_count != len(game_state):
            print("---+---")
        elif grid_size == 3 and i_count != len(game_state):
            print("---+---+---")
        elif grid_size == 4 and i_count != len(game_state):
            print("---+---+---+---")
        elif i_count != len(game_state):
            print("----------------------------------------------------------------------------")


def create_initial_state(grid_size):
    """Creates the initial state of the game for the rest of the game to work off of."""
    # I want to change `number` to start at 1, and `choice` to -1 later.
    number = 0
    game_state = []

    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append(number)
            number += 1
        game_state.append(row)
    
    return game_state



def do_move(game_state, turn, grid_size):
    """Takes user input to turn a number in to an X or O depending on who's turn it is."""
    # Is the turn X's or O's?
    if turn == 0:
        turn = 1
        player = "X"
    elif turn == 1:
        turn = 0
        player = "O"


    Valid_Choice = False
    while Valid_Choice == False:

        user_choice = (int(input(f"{player}, where would you like to go?")) - 1)
        row_choice = game_state[user_choice // grid_size]

        if row_choice[user_choice % grid_size] != "X" and row_choice[user_choice % grid_size] != "O":
            row_choice[user_choice % grid_size] = player
            Valid_Choice = True

        else:
            print(f"Number {user_choice} has an {row_choice[user_choice % grid_size]} in it. Please choose another.")
        
    return game_state, turn, (user_choice, game_state, player, grid_size)



def check_for_winner(combo):
    """Checks to see if the active player's move just now was a winning one."""
    user_choice, game_state, player, grid_size = combo

    row_choice = game_state[user_choice // grid_size]

    win = False
    
        
        # Horizontal
        
    try:  
        # Choice plus two to the right.
        if   (game_state[user_choice // grid_size])[user_choice % grid_size] == player and (game_state[user_choice // grid_size])[(user_choice % grid_size) + 1] == player and (game_state[user_choice // grid_size])[(user_choice % grid_size) + 2] == player:
            win = True
    except:
        pass

        
    try:
        # Choice plus two to the left.       
        if (game_state[user_choice // grid_size])[user_choice % grid_size] == player and (game_state[user_choice // grid_size])[(user_choice % grid_size) - 1] == player and (game_state[user_choice // grid_size])[(user_choice % grid_size) - 2] == player:
            win = True
    except:
        pass

        
    try:
        # Choice plus one on either side.
        if (game_state[user_choice // grid_size])[user_choice % grid_size] == player and (game_state[user_choice // grid_size])[(user_choice % grid_size) - 1] == player and (game_state[user_choice // grid_size])[(user_choice % grid_size) + 1] == player:
            win = True
    except:
        pass



        # Vertical

    try:
        # Choice plus two down.
        if   (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) + 1])[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) + 2])[user_choice % grid_size] == player:
            win = True
    except:
        pass

    try:
        # Choice plus two up.
        if (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size - 1)])[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) - 2])[user_choice % grid_size] == player:
            win = True
    except:
        pass

    try:
        # Choice plus one up and one down.
        if (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) + 1])[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) - 1])[user_choice % grid_size] == player:
            win = True
    except:
        pass


        # Diagonal /

    try:
        # Choice plus two up-right
        if   (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) - 1])[(user_choice % grid_size) + 1] == player and (game_state[(user_choice // grid_size) - 2])[user_choice % grid_size + 2] == player:
            win = True
    except:
        pass

    try:
        # Choice plus two down-left
        if (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) + 1])[user_choice % grid_size - 1] == player and (game_state[(user_choice // grid_size) + 2])[user_choice % grid_size - 2] == player:
            win = True
    except:
        pass

    try:
        # Choice plus one up-right and one down-left.
        if (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) + 1])[user_choice % grid_size - 1] == player and (game_state[(user_choice // grid_size) - 1])[user_choice % grid_size + 1] == player:
            win = True
    except:
        pass
        

        # Diagonal \

    try:
        # Choice plus two down-right
        if   (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) + 1])[(user_choice % grid_size) + 1] == player and (game_state[(user_choice // grid_size) + 2])[user_choice % grid_size + 2] == player:
            win = True
    except:
        pass

    try:
        # Choice plus two up-left
        if (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) - 1])[user_choice % grid_size - 1] == player and (game_state[(user_choice // grid_size) - 2])[user_choice % grid_size - 2] == player:
            win = True
    except:
        pass

    try:
        # Choice plus one down-right and one up-left.
        if (row_choice)[user_choice % grid_size] == player and (game_state[(user_choice // grid_size) - 1])[user_choice % grid_size - 1] == player and (game_state[(user_choice // grid_size) + 1])[user_choice % grid_size + 1] == player:
            win = True
    except:
        pass

    

    # Is the game won?    
    if win:
        run_game = False
        winner = player
    else: 
        run_game = True
        winner = "none"
    
    return run_game, winner



if __name__ == "__main__":
    main()