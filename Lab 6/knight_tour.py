import unsorted_list_ADT as list_ADT
import tour


def check_position(next_moves):
    valid_move = False
    new_pos = list_ADT.List(2)

    # continue to ask for position until a valid position is inputted
    while valid_move is False:
        # Getting position from user
        user_pos = input('Enter the Knights position: ')
        user_pos = user_pos.split(',')

        # storing position is a list ADT
        list_ADT.add_last(new_pos, int(user_pos[0]))
        list_ADT.add_last(new_pos, int(user_pos[1]))

        # Checking position is valid
        if next_moves is not None:
            for i in range(list_ADT.length(next_moves)):
                if next_moves[1][i] == new_pos:
                    return new_pos
        else:
            if 1 <= new_pos[1][0] <= 8 and 1 <= new_pos[1][1] <= 8:
                return new_pos

        # reset new_pos list ADT
        list_ADT.reset(new_pos)



quit_game = False
welcome_msg = "\nWelcome to the Knights Tour!\n" \
              "This aim of this game is to have the knight travel around the whole board and land on each spot exactly"\
              " once.\nThe position of the Knight is given by a 'K' and all the spots visited by the knight are given" \
              " by a '*'. Aim\nto turn every '0' on the board to a '*' and you will win!\n\n" \
              "Here is the chess board."

welcome_msg_2 = "As you can see everything is '0'. Lets change that by picking an initial position for the Knight." \
                "\n\nWhen entering a position, enter it in the form 'row, column' where the rows are given by the " \
                "numbers on the left\nand columns are given by the numbers on the bottom. * If you would like to " \
                "quit, enter 'q'"

menu_msg = "Select a choice...\n1: Position\n2: Quit"

print(welcome_msg)

# initialising chess board
chess_board = tour.initialise_board(8)
tour.print_board(chess_board)

current_pos = list_ADT.List(2)

while not quit_game:
    print(menu_msg)
    try:
        user_choice = int(input("Select a menu choice: "))

        if user_choice == 1:
            if list_ADT.length(current_pos) == 0:
                new_pos = check_position(None)
                tour.new_position(chess_board, new_pos, None)

            else:
                new_pos = check_position(next_moves)
                tour.new_position(chess_board, new_pos, current_pos)
                list_ADT.delete_item(current_pos, current_pos[1][0])
                list_ADT.delete_item(current_pos, current_pos[1][1])

            list_ADT.add_last(current_pos, new_pos[1][0])
            list_ADT.add_last(current_pos, new_pos[1][1])

            next_moves = tour.next_moves(chess_board, current_pos)

            # printing current tour
            tour.print_board(chess_board)
            # printing next moves
            moves = "Next possible moves:\n"
            for i in range(list_ADT.length(next_moves)):
                moves += str(next_moves[1][i][1][0]) + ',' + str(next_moves[1][i][1][1]) + '; '
            print(moves)

        elif user_choice == 2:
            quit_game = True
    except ValueError:
        print("Menu Choice is not valid")

