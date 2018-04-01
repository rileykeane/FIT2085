import unsorted_list_ADT
import tour

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

print(welcome_msg)

# initialising chess board
chess_board = tour.initialise_board(8)
tour.print_board(chess_board)

print(welcome_msg_2)
user_pos = input('Enter the Knights position: ')
if user_pos != 'q':
    user_pos = user_pos.split(',')

    new_pos = unsorted_list_ADT.List(2)
    unsorted_list_ADT.add_last(new_pos, int(user_pos[0]))
    unsorted_list_ADT.add_last(new_pos, int(user_pos[1]))

    tour.new_position(chess_board, new_pos, None)
    tour.print_board(chess_board)

    current_pos = unsorted_list_ADT.List(2)
    unsorted_list_ADT.add_last(current_pos, int(user_pos[0]))
    unsorted_list_ADT.add_last(current_pos, int(user_pos[1]))
else:
    quit_game = True

while not quit_game:
    user_pos = input('Enter the Knights position: ')

    if user_pos != 'q':
        user_pos = user_pos.split(',')
        new_pos[1][0] = int(user_pos[0])
        new_pos[1][1] = int(user_pos[1])
        tour.new_position(chess_board, new_pos, current_pos)
        current_pos[1][0] = int(user_pos[0])
        current_pos[1][1] = int(user_pos[1])
        tour.print_board(chess_board)
    else:
        quit_game = True


