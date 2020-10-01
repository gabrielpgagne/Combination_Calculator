from math import factorial as fc

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

def combinations(n=0, r=0):
    return (fc(n)/(fc(r)*fc(n-r)))

def getNR():
    try:
        d1 = n1.get()
        d2 = r1.get()
        tk.Label(root, text=f'C(n,r) = {combinations(int(d1),int(d2))}').grid(row=2, column=1)
    except TypeError:
        pass

def enter(*kargs):
    getNR()

root = tk.Tk()
root.title('Combinations calculator')
frame = tk.Frame(root)
frame.grid(row=0, column=0)

nLab = tk.Label(root, text='n')
rLab = tk.Label(root, text='r')
n1 = tk.Entry(root)
r1 = tk.Entry(root)
r1.bind('<Return>', enter)

nLab.grid(row=0, column=0)
rLab.grid(row=1, column=0)
n1.grid(row=0, column=1)
r1.grid(row=1, column=1)

okButton = tk.Button(root, text='Ok', command=getNR)
okButton.bind('<Return>', enter)
okButton.grid(row=2, column=0)

root.mainloop()

