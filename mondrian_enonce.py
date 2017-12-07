import tkinter as tk
import random

taille = 300
nb_lignes = 15
nb_max_blocs = 10
nb_blocs=0
couleurs = {1: 'black', 2: 'red', 3:'yellow', 4:'blue'}
on_the_grid=False


app = tk.Tk()
app.title("Mondrian")

new_game = tk.Button(app, text='New Mondrian', command=init_canvas, width=10)
new_game.grid(row=0, column=0, sticky=tk.W)

arrange = tk.Button(app, text='Arrange Blocks', command=arrange_blocs, width=10)
arrange.grid(row=0, column=1, sticky=tk.E)

canvas = tk.Canvas(app, width=taille, height=taille, bg ='white')
canvas.grid(row=1, column=0)

canvas.bind('<Button-1>', click_canvas)


app.mainloop()

