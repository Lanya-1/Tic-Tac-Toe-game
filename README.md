# Tic Tac Toe game
## Video Demo:  https://youtu.be/vjVhMnU3Fq0
### Description: It is a Tic Tac Toe game
The program consists of 7 functions (main, printboard(), place_piece(), check_winner(), is_winner(), comp_move(), comp_move2())

The design of the program is similar of problem sets that it has a main function that include other functions inside it and called at the end of program

Also, the user goes first and play with (X)

Here is what each function:

       * We have a boarder which is dictionary

       1- Printboard(): it basically prints the board of the game



       2- place_piece(): it takes three parameters (board) we put the game board in it

           (pos) take an integer, (player) which is (user) or (cpu)

           If we write (user) then the function will put (O) in the given position of the gameboard

           If we write (player) then the function will put (X) in the given position of the gameboard

           by changing the board’s value to X or O to the given position

           also, this function will append the given position to player_position or cpu_position list baced

           On what the given (player) argument is




       3 - check_winner (): it has a conditions list which contains all the winning conditions

            It loops through each one of them, if  player_position list match exactly one of them then it will

            Return (Congratulations YOU WON 🏆!) With green colour by help of termcolor module

            elif cpu_position list match one of them then it returns (YOU LOST! Sorry :( ) in red colour

            elif the combination of the length of both player_position & cpu_position list was equal to 9

            Which means no one wins then it returns Tie Game! With yellow colour




       4 - is_winner(): the function takes two parameters (board & letter) so it checks if the same letter    exists if so, the it returns True





       5 - comp_move(): the function first creates a list of possible moves which are empty places

         and return a move which will be a number depend on those:

         first check for possible winning move to take or to block opponents winning move

         then it checks if the centre is taken or not if not then it goes there

         then check for the corners if empty then it chooses one of the comers randomly

         then check for the edges if empty then it chooses one of the comers randomly




      6 – comp_move2(): it does the same thing as comp_move() function the only difference is it doesn't check for centre to move it there it checks for the
          coneres then centre



      7 – main ():

        First it prints the information for the game

        then choosing a level and it handles invalid level and ask the user again

        after that it asks the user for a number to place (X) there and it handles value error and if the

        user tried to put (X) on a taken place or if the input was not between 1 to 9and ask the user again

        Then it calls place_piece() to that input >>> (place_piece(the_board , a, "user") and it call check_winner() to check if it was a win move





        after that if the user chose the easy level the in calls the comp_move2() because it is eerier

        but if it was hard level then it calls comp_move() because it is harder >>>

        (place_piece(the_board , b, "cpu"), check_winner() to check if it was a win move


        Finally, it prints the gameboard


so that was project.py
and in test_project.py it tests the functions with pytest
