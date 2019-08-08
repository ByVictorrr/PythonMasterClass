try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

#print(tkinter.TkVersion)
#print(tkinter.TclVersion)

# open a window
# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("hello worlR")
mainWindow.geometry("680x480+8+200")


label = tkinter.Label(mainWindow, text="hello world")
label.grid(row=0,column=0)


leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)


# frames help group stuff together
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')


button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

#configure the colums
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)


mainWindow.mainloop()