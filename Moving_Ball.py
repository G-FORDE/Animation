from tkinter import *


tk = Tk()

#create the canvas
canvas = Canvas(tk)
canvas.pack(fill=BOTH, expand=1)

#create the ball
ball = canvas.create_oval(20, 20, 50, 50, fill="blue")

#create coordinate points where to move the ball
def animation(x_move, y_move):
    canvas.move(ball, x_move, y_move)
    canvas.update()

    #speed of the ball
    canvas.after(100)

    #create the animation
    tk.after_idle(animation, x_move, y_move)

#controle the direction
animation(1, 1)


tk.mainloop()