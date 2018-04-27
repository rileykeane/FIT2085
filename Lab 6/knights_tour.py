import tour


def game_menu():
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

    return user_choice


def read_move():
    valid_move = False
    row = None
    col = None

    while valid_move is False:
        user_move = input('\nEnter a position for the knight in the format row, column: ')
        try:
            user_move = user_move.split(',')
            row = int(user_move[0])
            col = int(user_move[1])
            valid_move = True
        except ValueError:
            print("Move is not valid! Please make sure row and column are integers and fit within the size of the tour.")
        except IndexError:
            print("Move is not valid! Please make sure input is in the form row, column.")

    return row, col


def position(the_tour):
    first_move = False
    allowed_move = False

    try:
        moves = tour.next_moves(the_tour)
        print("Allowed moves\n" + tour.next_moves_str(moves))
    except Exception:
        print('Enter the initial position for the knight')
        first_move = True

    while not allowed_move:

        if first_move:
            row, col = read_move()
            try:
                tour.new_position(the_tour, row, col)
                allowed_move = True
            except IndexError:
                print('Position must be within size of the tour, try again.')
        else:
            row, col = read_move()
            if tour.check_position(the_tour, row, col):
                try:
                    tour.new_position(the_tour, row, col)
                    allowed_move = True
                except IndexError:
                    print('Position must be within size of the tour, try again.')
            else:
                print('Position must be an allowed move, try again')


def main():
    the_tour = tour.initialise_tour(8)

    print("\nWelcome to the Knights Tour!\n"
          "This aim of this game is to have the knight travel around the whole board and land on each spot exactly once"
          "\nThe position of the Knight is given by 'K' and all the spots visited by the knight are given by '*'. Aim"
          "\nto turn every '0' on the board to a '*' and you will win!\n\nLets get started...")

    print('\nLets choose an initial position for the knight\n'
          'Select position from the menu below\n')

    quit_game = False
    while not quit_game:
        user_choice = game_menu()

        # MENU CHOICE - Position
        if user_choice == 1:
            tour.print_tour(the_tour)
            position(the_tour)

        # MENU CHOICE - Undo
        if user_choice == 2:
            try:
                tour.undo_move(the_tour)
                tour.print_tour(the_tour)
            except Exception:
                print('The tour must have made at least one move to undo.\n')

        # MENU CHOICE - Start Over
        if user_choice == 3:
            the_tour = tour.initialise_tour(8)

        # MENU CHOICE - Exit
        if user_choice == 4:
            quit_game = True


main()
