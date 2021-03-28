# Parametric Assignment by Angelina Wu

import simplegui
import math, time


dots_list = []
t0 = time.time()
t = t0


shift = [400,300]

w = (0.9*math.cos(8*t)+1)*(0.1*math.cos(24*t)+1)*(0.1*math.cos(200*t)+0.9)

def fun(t):
    x = 50*(math.sin(t)+1)*(math.cos(t))*w
    y = 50*(math.sin(t))*(math.sin(t)+1)*w
    return x,y
   

class Dot:
    def __init__(self, position):
        self.pos = position
        
        
    def draw(self, canvas, col):
        x = self.pos[0] + shift[0]
        y = -self.pos[1] + shift[1]
        canvas.draw_circle([x,y], 5, 1, col, col)

# Handler to draw on canvas
def draw(canvas):
    for dot in dots_list:
        dot.draw(canvas, "#ACDEF8")
    dot = Dot(fun(time.time()))
    dots_list.append(dot)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Parametric demo", 800, 600)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
