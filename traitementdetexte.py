
f_out= open('files/exo61_td7.txt','w')
i=0
while(i<10000):
    f_out.write(str(i)+'\n')
    i +=1
f_out.close()

tab=[]
f_in = open('files/exo61_td7.txt','r')
li = f_in.readline()
while(''!=li):
    tab.append(int(li))
    li= f_in.readline()
print(tab)
f_in.close()




import tkinter as tk

HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 8 
hauteur_case = HEIGHT // 8


#changement de couleur
WHITE = "white"
BLACK = "black"

def changement_color(color):
    if color == WHITE:
        return BLACK
    elif color == BLACK:
        return WHITE
racine = tk.Tk() #création de la fenêtre racine
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH)
canvas.grid()
for i in range(8):
    for j in range(8):
        (i+j) % 2 == 0
        color= "white"
        canvas.create_rectangle((i*largeur_case,j*hauteur_case),
                ((i+1)*largeur_case,(j+1)*hauteur_case), fill=color, outline="black")
racine.mainloop() # lancement de la boucle principale


