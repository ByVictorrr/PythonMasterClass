try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
    
def parablola(x):
    y = x*x
    return y

for x in range(-100, 100):
    y = parablola(x)
    print(y)
