'''
Chenchira Stevens
CNE330
6/21/2021
Python For Kids (Jason R. Briggs)
'''
from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball: # Adding the ball
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]#self.x = 0 (Making the ball bounce)
        self.y = -3 #self.y = -1 (speed up the ball)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_paddle(self, pos): # make the ball hit paddle (line 32, and 49)
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        #selfs.canvas.move(selfs.id, 0, -1)
        self.canvas.move(self.id, self.x, self.y) # Making the ball move
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos)  == True: # Make the ball hit paddle by make a function hit_paddle.
            self.y = -3
        if pos[0]<= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
#ball = Ball(canvas, 'pink')

class Paddle: # Adding the paddle
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2
paddle= Paddle(canvas, 'lightblue')
ball = Ball(canvas, paddle, 'orange')

while 1:
    if ball.hit_bottom == False: # Making the game finish
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

