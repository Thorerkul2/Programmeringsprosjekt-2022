from tkinter import *
import random
import time

isInEditor = False
def loadLevel(filename):
    global level, levelr, levelname
    levelname = filename
    level = open(filename, "a")
    levelr = open(filename, "r")

class Ball:
    def __init__(self, canvas, color, x, y):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)
        self.x = -5
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        
        #self.sprite = canvas.create_image(200, 470, image=PhotoImage(file='/Users/thomasholmesland/Documents/Thor/Programmering/Skoleprosjekt 2022/src/assets/art/ball.png'))

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.pos = self.canvas.coords(self.id)
        self.physics(racket)
        #print(self.pos[0], self.pos[1])
            
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
        self.canvas.move(self.id, 10, 140)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.pos = self.canvas.coords(self.id)
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.pos = self.canvas.coords(self.id)
        if frame > 10:
            self.move()
        
    def move(self):
        if self.pos[1] < mouse_y - 37:
            self.y = 10
        if self.pos[1] > mouse_y - 37:
            self.y = -10
        #print(mouse_y, self.pos[1], frame)

class BallSpawner:
    def __init__(self):
        self.levela = level
        self.isInEditor = isInEditor
        #print(levelr.read())

        if isInEditor:
            canvas.bind_all('<KeyPress-Up>', self.writePos)

        self.i = 0

    def start(self):
        self.levelt = levelr.read()
        self.levelt = self.levelt.split('-')

    def update(self):
        self.levelr = open(levelname, "r")
        if isInEditor == False:
            self.read()

    def read(self):
        if self.i < len(self.levelt) - 1:
            self.i += 1

        if int(self.levelt[self.i]) > 0:
            global balllist
            ball = Ball(canvas, 'red', 500, int(self.levelt[self.i])*40 - 10)
            balllist.append(ball)

    def write(self):
        level.write("0-")

    def write1(self, evt):
        level.write("1-")

    def write1(self, evt):
        level.write("2-")

    def write1(self, evt):
        level.write("3-")

    def write1(self, evt):
        level.write("4-")

    def write1(self, evt):
        level.write("5-")

    def write1(self, evt):
        level.write("6-")

    def write1(self, evt):
        level.write("7-")

    def write1(self, evt):
        level.write("8-")

    def write1(self, evt):
        level.write("9-")

class GameManager:
    def __init__(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass


isRunning = True
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
    for i, num in enumerate(lstx):
        ball = Ball(canvas, 'red', num, lsty[i])
        balllist.append(ball)

def on_closing():
    isRunning = False
    gamemanager.stop()
    level.close()
    levelr.close()
    tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_closing)

loadLevel("level1.txt")
isDead = False
ballspawner = BallSpawner()

gamemanager = GameManager()


racket = Racket(canvas, 'blue')
#ball = Ball(canvas, 'red', 500, 250)

#makeBalls([600, 700, 800, 900, 1000], 
#          [300, 250, 200, 150, 100])


ballspawner.start()
gamemanager.start()
while isRunning:
    #print(len(balllist))
    ballspawner.update()
    if isDead == False:
        racket.draw()
        #ball.draw()
        for ball in balllist:
            ball.draw()
    tk.update_idletasks()
    tk.update()
    frame += 1
    time.sleep(0.01)
