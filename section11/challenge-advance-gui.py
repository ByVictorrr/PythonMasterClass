# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# init main window
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("680x480-8-200")


# init rows and columns
mainWindow.columnconfigure(0, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=100)


# entryBox
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nw')


#
buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=1, column=0, sticky='nw')

const_sticky="nw"
const_height=1
const_width=1

calc_str = {"C":[0,0], #[row, column]
            "CE":[0,1],
            '7':[1,0],
            '8':[1,1],
            '9':[1,2],
            '+':[1,3],
            '4':[2,0],
            "5":[2,1],
            "6":[2,2],
            "-":[2,3],
            '1':[3,0],
            '2':[3,1],
            '3':[3,2],
            '*':[3,3],
            '0':[4,0],
            '=':[4,1],
            '/':[4,2]
            }
btns = []

for symbol in calc_str:
    btn = tkinter.Button(buttonFrame, text=symbol, height=const_height, width=const_width)
    btn.grid(row=calc_str[symbol][0],column=calc_str[symbol][1], sticky=const_sticky)
    btns.append(btn)
    
   
    btn = tkinter.Button(buttonFrame, text=symbol, height=const_height, width=const_width)
    btn.grid(row=calc_str[symbol][0],column=calc_str[symbol][1], sticky=const_sticky)
    btns.append(btn)
    

# run program
mainWindow.mainloop()

