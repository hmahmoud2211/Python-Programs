from glob import glob
from tkinter import *
import random
# make next turn for the player
# to detrmine the x or o in which row and column
def next_turn(row, col):
    # to recall the player variable 
    global player
    # it check the this buttom is empty or not
    # and it check there is a win or not 
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        # check the player is the first one 
        if player == players[0]:
            # Put player 1 sympol in the botton
            game_btns[row][col]['text'] = player
            # to check if there is a win condtion or not 
            if check_winner() == False:
                # switch player
                player = players[1]
                # to show which player in the window 
                label.config(text=(players[1] + " turn"))
            # at the win condition of the first player 
            elif check_winner() == True:
                # show which player wins 
                label.config(text=(players[0] + " wins!"))
            # if there is a tie condition 
            elif check_winner() == 'tie':
                # show tie on the windows 
                label.config(text=("Tie, No Winner!"))
        # check the player is the second one 
        elif player == players[1]:
            # Put player 2 sympol in the button 
            game_btns[row][col]['text'] = player
            # to check if there is a win condtion or not
            if check_winner() == False:
                # switch player
                player = players[0]
                # to show which player in the window
                label.config(text=(players[0] + " turn"))
            # at the win condition of the second player
            elif check_winner() == True:
                label.config(text=(players[1] + " wins!"))
             # if there is a tie condition
            elif check_winner() == 'tie':
                # show tie on the windows
                label.config(text=("Tie, No Winner!"))

# check if there is a win or loose 
def check_winner():
    # check all 3 horizontal conditions
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg="cyan")
            game_btns[row][1].config(bg="cyan")
            game_btns[row][2].config(bg="cyan")
            return True

    # check all 3 vertical conditions
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg="cyan")
            game_btns[1][col].config(bg="cyan")
            game_btns[2][col].config(bg="cyan")
            return True

    # check diagonals conditions
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][2].config(bg="cyan")
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][0].config(bg="cyan")
        return True

    # if there are no empty spaces left
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='orange')

        return 'tie'
    # to continue the game if there is no tie or winning 
    else:
        return False

# check if there is empty cell to end or continue game 
def check_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

# to restart the game after the finish 
def start_new_game():
    # recall the player rondomly 
    global player
    player = random.choice(players)
    # make the player turn apear in the window
    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="red")


window = Tk()
window.title("X or O game")
# the list of the players 
players = ["x", "o"]
# to pick the player randomly 
player = random.choice(players)
# this is the buttom list
game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
# to show who is the player turn 
label = Label(text=(player + " turn"), font=('consolas', 40))
# to make the label apear in the window 
label.pack(side="top")
# to show the buttom apear to restart the game 
# the command recall the start new game function 
restart_btn = Button(text="play agian", font=(
    'consolas', 20), command=start_new_game)
# to show the botton in the window 
restart_btn.pack(side="top")
# to make a frame in the window to put in it the botton 
btns_frame = Frame(window)
# to show the frame in the window 
btns_frame.pack()
# the first loop to pass by the row
for row in range(3):
    # the second loop to pass by the column
    for col in range(3):
        # to call the row and column by there index 
        # because of this botton recall a function with parameter so we use lamda function because the comand dont put paremeter 
        game_btns[row][col] = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                                     command=lambda row=row, col=col: next_turn(row, col))
        # to make the botton grided 
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()
