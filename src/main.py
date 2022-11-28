from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color, x, y):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)
        self.x = -5
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.pos = self.canvas.coords(self.id)
        #print(self.pos)
        self.physics(racket)
            
    def physics(self, racket):
        if self.pos[0] <= racket.pos[2]:
            if self.pos[3] >= racket.pos[1]:
                if self.pos[1] <= racket.pos[3]:
                    self.x = 10
                    self.y = 5
            
        if self.pos[0] <= 0:
            global isDead
            isDead = True
            
class Racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 25, 75, fill=color)
        self.canvas.move(self.id, 50, 140)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.pos = self.canvas.coords(self.id)
        if frame > 60:
            self.move()
        
    def move(self):
        if self.pos[1] < mouse_y:
            self.y = 5
        if self.pos[1] > mouse_y:
            self.y = -5
        #print(mouse_y, self.pos[1], frame)

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

mouse_x = 0
mouse_y = 0

frame = 0

def motion(event):
    global mouse_x, mouse_y
    mouse_x, mouse_y = event.x, event.y

tk.bind('<Motion>', motion)

balllist = []
def makeBalls(lstx, lsty):
    e = 0
    for num in lstx:
        ball = Ball(canvas, 'red', num, 250)
        balllist.append(ball)
        e += 1
    print(e)

isDead = False

racket = Racket(canvas, 'blue')
ball = Ball(canvas, 'red', 500, 250)

makeBalls([600, 600, 600, 600, 600], 
          [250, 300, 400, 500, 600])

while 1:
    if isDead == False:
        racket.draw()
        ball.draw()
        for ball in balllist:
            ball.draw()
    tk.update_idletasks()
    tk.update()
    frame += 1
    time.sleep(0.01)