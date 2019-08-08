try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

#print(tkinter.TkVersion)
#print(tkinter.TclVersion)

# open a window
# tkinter._test()

mainWindow = tkinter.Tk()

# setup
mainWindow.title("hello worlR")
mainWindow.geometry("680x480+0+400")

label = tkinter.Label(mainWindow, text="hello world")
label.pack(side='top')


leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left',anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.pack(side='top')


# frames help group stuff together
rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right',anchor='n', fill=tkinter.Y, expand=True)


button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")
button1.pack(side="top" )
button2.pack(side="top")
button3.pack(side="top")

# run
mainWindow.mainloop()
