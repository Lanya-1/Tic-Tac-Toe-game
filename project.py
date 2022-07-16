# Tic Tac Toe game with two levels

import random
import sys
import copy
from termcolor import colored


player_position =[]
cpu_position = []
the_board = {1: ' ', 2: ' ', 3: ' ',    #the board of the game
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}



def main():


# info to show from the beginning
    print(colored('''
    Welcome to Tic Tac Toe game

    You play with (X)

    This is the game board

    1 | 2 | 3
   ---+---+---
    4 | 5 | 6
   ---+---+---
    7 | 8 | 9

    Two levels available (easy & hard)
    ''', "green"))

# insure the user to type a vaild level
    while True :
        level = input("Choose a vaild level : ")
        if level == "easy" or level == "hard":
            break

    global player_position
    global cpu_position

    while True:
        try:
            a = int(input("Enter your placement (1-9) : "))   # ask the user for a number to place X on it

            while a in player_position or a in cpu_position :       # prevent the user to choose a taken place
                print("Position taken! Enter a correct Position")
                a = int(input("Enter your placement (1-9) : "))

            while a not in [1,2,3,4,5,6,7,8,9] :             # insure the user for an input from 1 to 9
                print("Enter a position from 1 to 9")
                a = int(input("Enter your placement (1-9) : "))


            # call the implemented functions for that input
            place_piece(the_board , a , "user")
            result = check_winner()
            if result == colored("Congratulations YOU WON 🏆!" , "green") or result == colored("YOU LOST! Sorry :( " , "red") or result ==colored("Tie Game!" , "yellow"):
                printboard(the_board)
                print(result)
                sys.exit()
            else:
                pass

            # check if the user chose easy or hard based on that call one of the function
            if level == "easy":
                b = comp_move2()
            if level == "hard":
                b = comp_move()


            # again call the implemented functions
            place_piece(the_board , b , "cpu")
            result = check_winner()
            if result == colored("Congratulations YOU WON 🏆!" , "green") or result == colored("YOU LOST! Sorry :( " , "red") or result ==colored("Tie Game!" , "yellow"):
                printboard(the_board)
                print(result)
                sys.exit()
            else:
                pass

            printboard(the_board)     # finally print the board by using printboard function

        except ValueError :
            pass





# to print the board
def printboard(board):
    print(' {} | {} | {} '.format(board[1], board[2], board[3]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[4], board[5], board[6]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[7], board[8], board[9]))



def place_piece(board , pos , player):   # takes three parameters
    global player_position
    global cpu_position

    symbol = " "             # based on player parameter chose X or O
    if player == "user":
        symbol =  "X"
        player_position.append(pos)    #append the givin position to player_position list which we want to track on

    if player == "cpu":
        symbol = "O"
        cpu_position.append(pos)       #append the givin position to cpu_position list which we want to track on

    board[pos] = symbol          # change the given position's value to the symbol on the board




def check_winner():
    global player_position
    global cpu_position
#  winning condition
    top_row = [1,2,3]
    mid_row = [4,5,6]
    low_row = [7,8,9]
    top_col = [1,4,7]
    mid_col = [2,5,8]
    low_col = [3,6,9]
    cross1 =  [1,5,9]
    cross2  = [7,5,3]

# append them to to one list
    conditions = []
    conditions.append(top_row)
    conditions.append(mid_row)
    conditions.append(low_row)
    conditions.append(top_col)
    conditions.append(mid_col)
    conditions.append(low_col)
    conditions.append(cross1)
    conditions.append(cross2)

# loop through conditions list and check if all the content  of that list exist in player_postion or cpu_position list
    for list in conditions:
        # if the user win
        if  set(list).issubset(player_position):
            return colored("Congratulations YOU WON 🏆!" , "green")
        if  set(list).issubset(player_position) and (len(player_position) + len(cpu_position) == 9) :
            return colored("Congratulations YOU WON 🏆!" , "green")

        # if the computer wins
        if  set(list).issubset(cpu_position):
            return colored("YOU LOST! Sorry :( " , "red")
        if  set(list).issubset(cpu_position) and (len(player_position) + len(cpu_position) == 9):
            return colored("YOU LOST! Sorry :( " , "red")


        # check if there is no space left
        if len(player_position) + len(cpu_position) == 9  :
            return colored("Tie Game!" , "yellow")


# return true if one of  the these coditions were true
def is_winner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))



# tell the computer how to move
# this one is for the hard level cause it tries to take the center first
def comp_move():
    possibleMoves = [key for key in the_board if the_board[key] == " "] # Create a list of possible moves
    move = 0

    #Check for possible winning move to take or to block opponents winning move

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = the_board.copy()
            boardCopy[i] = let
            if is_winner(boardCopy, let):
                move = i
                return move

    # try to take the center
    if 5 in possibleMoves:
        move = 5
        return move



    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = random.choice(cornersOpen)
        return move



    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = random.choice(edgesOpen)

    return move



#same thing but for easy level
def comp_move2():
    possibleMoves = [key for key in the_board if the_board[key] == " "]
    move = 0


    #Check for possible winning move to take or to block opponents winning move
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = the_board.copy()
            boardCopy[i] = let
            if is_winner(boardCopy, let):
                move = i
                return move


    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = random.choice(cornersOpen)
        return move


    if 5 in possibleMoves:
        move = 5
        return move



    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = random.choice(edgesOpen)

    return move






if __name__ == "__main__":
    main()

