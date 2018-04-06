import unsorted_list_ADT as list_ADT
import tour


def get_position():
    try:
        user_pos = input('Enter the Knights position: ')
        user_pos = user_pos.split(',')

        if len(user_pos) > 2:
            raise IndexError('Position must only be 2 integers')

        # storing position in a list ADT
        pos = list_ADT.List(2)
        list_ADT.add_last(pos, int(user_pos[0]))
        list_ADT.add_last(pos, int(user_pos[1]))
    except (ValueError, IndexError):
        raise ValueError("Position is not valid. Position must be integers, row and column entered as 'r,c'")

    return pos


def new_game():
    # Local variables
    current_pos = None
    new_pos = None
    next_moves = None

    print("\nWelcome to the Knights Tour!\n"
          "This aim of this game is to have the knight travel around the whole board and land on each spot exactly once"
          "\nThe position of the Knight is given by 'K' and all the spots visited by the knight are given by '*'. Aim"
          "\nto turn every '0' on the board to a '*' and you will win!\n\nLets get started...")

    # setting up a new tour
    the_tour = tour.initialise_tour(8)
    tour.print_tour(the_tour)

    print('\nLets choose an initial position for the knight\n'
          'Select position from the menu below\n')

    quit_game = False
    while not quit_game:
        print('Select a menu choice\n'
              '1. Position\n'
              '2. Undo\n'
              '3. Start Over\n'
              '4. Exit')

        # getting menu choice from user
        user_choice = None
        valid_choice = False
        while not valid_choice:
            try:
                user_choice = int(input('Enter a menu choice: '))
                if 1 <= user_choice <= 4:
                    valid_choice = True
            except ValueError:
                print('Please make sure menu choice is an integer 1 - 4, try again\n')

        # MENU CHOICE - Position
        if user_choice == 1:
            # printing next moves
            if next_moves is not None:
                moves_str = "\nNext possible moves:\n"
                for i in range(list_ADT.length(next_moves)):
                    move = list_ADT.get_item(next_moves, i)
                    moves_str += str(list_ADT.get_item(move, 0)) + ',' + str(list_ADT.get_item(move, 1)) + '; '
                print(moves_str)

            # reading position from the user
            valid_pos = False
            while not valid_pos:
                try:
                    new_pos = get_position()
                    if tour.check_position(the_tour, new_pos, next_moves) is True:
                        valid_pos = True
                    else:
                        print('Position is not allowed, try again')
                except ValueError:
                    print('Position is not a valid input, try again')

            # updating the tour with the new position
            tour.new_position(the_tour, new_pos, current_pos)
            current_pos = new_pos
            tour.print_tour(the_tour)
            next_moves = tour.next_moves(the_tour, current_pos)

        # MENU CHOICE - Start Over
        if user_choice == 3:
            print('\n\n')
            current_pos = None
            new_pos = None
            next_moves = None

            # setting up a new tour
            the_tour = tour.initialise_tour(8)
            tour.print_tour(the_tour)

        # MENU CHOICE - Exit
        if user_choice == 4:
            quit_game = True


def main():
    print('The Knights Tour\n'
          '----------------\n'
          'Select a menu choice\n'
          '1. New Game\n'
          '2. Tutorial\n'
          '3. Difficulty\n'
          '4. Exit')

    valid_choice = False
    while not valid_choice:
        try:
            user_choice = int(input('Enter a menu choice: '))
            if 1 <= user_choice <= 4:
                valid_choice = True
            else:
                print('Not a valid menu choice\n')
        except ValueError:
            print('Please make sure menu choice is an integer 1 - 4\n')

    if user_choice == 1:
        new_game()

    if user_choice == 4:
        exit()


main()