from tkinter import *
import random 
# Some constents require for the game 
GAMEW = 700 
GAMEH = 700
SPEED = 50 
SPACE_SIZE = 50 
Snake_body = 3
SNAKE_COLOR = "#00FF00"#green
FOOD_COLOR ="#FF0000"#red
BG ="#000000"#black

class Snake :
     
    def __init__(self):
         self.body_size = Snake_body
         self.coordinates = []
         self.squares = []
         for i in range (0 , Snake_body):
             self.coordinates.append([0 , 0])

         for x, y in self.coordinates:
            square = canvas.create_rectangle(x , y , x + SPACE_SIZE , y + SPACE_SIZE ,fill = SNAKE_COLOR , tag = "snake")
            self.squares.append(square)


class Food:
    
    def __init__(self):
        # create the food at a certian x and y 
        x = random.randint(0 , (GAMEW/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0 , (GAMEH/SPACE_SIZE)-1) * SPACE_SIZE


        self.corrdinates =[x,y]

        canvas.create_oval(x , y , x+ SPACE_SIZE , y +SPACE_SIZE , fill = FOOD_COLOR , tag = "food")



def next_turn():
    pass

def change_direction(new_dirction):
    pass

def check_collisions():
    pass 

def game_over():
    pass

#create the window 
window = Tk()
window.title("Snake Game")
window.resizable(False , False)

score = 0
direction = "down"

label = Label(window, text = "Score:{}".format(score),font=('consolas',40))
label.pack()
canvas = Canvas (window, bg = BG , height=GAMEH,width=GAMEW )
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x =int((screen_width/2) - (window_width/2))
y =int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")#Centre the game screen 

#Call the snake class
snake = Snake()
#Call the food class
food = Food()

window.mainloop()