import tkinter as tk

win = tk.Tk()


def executor():
    print(a.get(), b.get(), c.get())
    ka = float(a.get())
    kb = float(b.get())
    kc = float(c.get())
    d = kb**2 - 4*ka*kc
    if d<0:
        print('nema riesenie v R')
        vys.config(text='nema riesenie v R')
    elif d == 0:
        print('x = ', -kb/(2*ka))
        vys.config(text='x = ' + str(-kb/(2*ka)))
    else:
        print('x1 = ', (-kb + d ** 0.5) / (2 * ka))
        print('x2 = ', (-kb - d ** 0.5) / (2 * ka))
        vys.config(text='x1 = ' + str((-kb + d ** 0.5) / (2 * ka)) + '\n' + 'x2 = ' + str((-kb - d ** 0.5) / (2 * ka)))


button = tk.Button(win, text='Click me!', command=executor)
button.pack()

at = tk.Label(win, text='koeficient a:')
at.pack()
a = tk.Entry(win)
a.pack()

bt = tk.Label(win, text='koeficient b:')
bt.pack()
b = tk.Entry(win)
b.pack()

ct = tk.Label(win, text='koeficient c:')
ct.pack()
c = tk.Entry(win)
c.pack()

vys = tk.Label(win, text='vysledok')
vys.pack()

win.mainloop()

# TODO: vypis vysledky v gui, je jedno ako