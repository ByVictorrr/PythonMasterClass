# Modify the circle function so that it allows the colour of the circle to be specified
# and defaults to red if a colour is not given.  You may want to review the previous lectures
# about named parameters and default values.


import math
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter # python 2
    
def parabola(page, size):
	for x in range(size):
		y = (x*x) / size
		plot(page, x, y)
		plot(page, -x, y)


def circle(page, radius, g, h, fill="red"):
	for x in range(g, (g+radius)*100):
		x/=100
		y = h + (math.sqrt(radius**2 -((x-g) **2)))
		plot(page, x, y, fill=fill)
		plot(page, x, 2*h-y,fill=fill)
		plot(page, 2*g-x, 2*h - y, fill=fill)
		print(locals())

def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin,-y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0,y_origin, 0, -y_origin, fill="black")


def plot(page, x, y, fill="red"):
    page.create_line(x,-y, x+1, -y+1, fill=fill)


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=620, height=480)
canvas.grid(row=0,column=0)


draw_axes(canvas)
parabola(canvas, 100)
parabola(canvas, 500)

circle(canvas, 100, 100, 100, fill="green")
circle(canvas, 100, -100, 100, fill="blue")
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, -100)




mainWindow.mainloop()

