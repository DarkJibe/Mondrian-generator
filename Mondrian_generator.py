import os, random, tkinter as tk
from functools import partial

def init_canvas():
    """
        (Ré)initialise le canvas et les variables
        Génère un nombre de lignes horizontales et verticales définie par [nb_lignes]
        Les coordonnées en x ou en y sont définient par un nombre aléatoire [rd]
        Génère une liste [liste_coord] qui contient toutes les coordonées x des lignes verticales
        Trie la liste [liste_coord]
        Appelle click_canvas() par un bind <Button-1>
    """
    global canvas, liste_coordX, liste_coordY, nb_blocs
    nb_blocs=0
    liste_coordX=[]
    liste_coordY=[]
    canvas = tk.Canvas(app, width=taille, height=taille, bg ='white')
    canvas.grid(row=1, column=0, columnspan=9, rowspan=4)
    for i in range(nb_lignes):
        rd=random.randint(0,taille)
        canvas.create_line(0,rd,taille,rd,fill='black')
        liste_coordY.append(rd)
    for i in range(nb_lignes):
        rd=random.randint(0,taille)
        canvas.create_line(rd,0,rd,taille,fill='black')
        liste_coordX.append(rd)
    liste_coordX.sort()
    liste_coordY.sort()

    canvas.bind('<Button-1>', click_canvas)


def arrange_blocs():
    global on_the_grid
    if on_the_grid: on_the_grid=False
    else: on_the_grid=True

def color_choice():
    global auto
    auto=True

def click_bt(col, eve):
    global  auto, cl
    auto=False
    cl=col

def click_canvas(eve):
    """
        Appelée par un bind <Button-1> sur [canvas]
        Crée un nombre de rectangles limités par [nb_max_blocs], de couleurs aléatoirement choisies dans [colors]
        Génère deux nombres aléatoire limités par la taille du canvas qui serviront à definir la taille des rectangles
        Si on veut les aligner :
            Ajoute la différence entre chaque élément de [liste_coord] et la coordonnée de clique à une liste [diff]
            Récupère l'index de la valeur minimale de [diff] et le stocke dans une variable [ind]
            Crée un rectangle ayant comme coordonnées d'abssyces liste_coord[ind] et liste_coord[ind+1]
            En cas de dépassement de l'index de la liste, ajoue d'un contion qui évite le problème
        Sinon :
            Crée un rectangle en fonction des coordonnées du clique de souris
        Incrémente le compteur du nombre de blocs.
    """
    global canvas, nb_blocs, cl
#-----------------------THIS IS WHERE THE MAGIC HAPPENS------------------------#
    if nb_blocs<nb_max_blocs:
        if auto: cl=random.sample(couleurs,1)
        if on_the_grid:
            diffX=[]
            diffY=[]
            for e in liste_coordX: diffX.append(abs(e-eve.x))
            for e in liste_coordY: diffY.append(abs(e-eve.y))
            indX=diffX.index(min(diffX))
            indY=diffY.index(min(diffY))
            try: canvas.create_rectangle(liste_coordX[indX],liste_coordY[indY],
                                         liste_coordX[indX+1],
                                         liste_coordY[indY+1],fill=cl)
            except IndexError: pass
        else:
            rect_x=random.randint(1,taille/4)
            rect_y=random.randint(1,taille/4)
            canvas.create_rectangle(eve.x,eve.y,
                                    eve.x+rect_x,eve.y+rect_y,fill=cl)
        nb_blocs+=1
#----------------------------END OF THE MAGIC----------------------------------#

def save_mondrian():
    global nbsave
    nbsave+=1
    name='mondrian'+str(nbsave)+'.ps'
    canvas.postscript(file=name)

taille = 700
nb_lignes = 20
nb_max_blocs = 50
couleurs = ['black', 'red', 'yellow', 'blue']
correc=['white']
on_the_grid=False
auto=True
nbsave=0

app = tk.Tk()
app.title("Mondrian")

new_game = tk.Button(app, text='New Mondrian', command=init_canvas, width=10)
new_game.grid(row=0, column=0, sticky=tk.W)

arrange = tk.Button(app, text='Arrange Blocks', command=arrange_blocs, width=10)
arrange.grid(row=0, column=1, sticky=tk.W)

choix = tk.Button(app, text='Couleur aleatoire', command=color_choice, width=12)
choix.grid(row=0, column=2, sticky=tk.W)

for i, color in enumerate(correc+couleurs):
#    b = tk.Button(app, text='', width=3, bg=color, activebackground=color) #Windaube way
    b = tk.Button(app, text='', width=1,bg=color, activebackground=color) #Nunux way
    b.grid(row=0, column=i+3)
    b.bind("<Button-1>",partial(click_bt,color))

save = tk.Button(app, text='Enregistrer', command=save_mondrian, width=10)
save.grid(row=0, column=8, sticky=tk.W)

init_canvas()

app.mainloop()

