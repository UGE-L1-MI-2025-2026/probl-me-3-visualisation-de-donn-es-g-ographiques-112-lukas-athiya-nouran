import math as m
import fltk
import shapefile


def conv_rad_degr(rad):
    return (rad*180)/m.pi


def conv_degr_rad(degre):
    return (degre*m.pi)/180


def fonct_mercator(latitude):
    return  m.log(m.tan((latitude / 2) + (m.pi / 4)))


def france(L, H, sf):
    L *= 1.5
    H *= 1.5
    ech = 4
    echh = 3
    centre = 0
    total = []
    for i in range(len(sf.shapes())):
        shape = sf.shape(i)
        nbr_partie = len(shape.parts)
        # s'il est en plusieurs parties on 
        # itère sur les parties
        partie = []
        for k in range(nbr_partie):
            nouvelle_coordo = []
            # on fait une boucle avc
            # debut = le premier élément de parts (indexe du debut du polygon)
            debut = shape.parts[k]
            # fin = l'élément suivant s'il existe 
            if k+1 < len(shape.parts):
                fin = shape.parts[k+1]
            # sinon on prend la longueur de la liste des points
            else:
                fin = len(shape.points)

            for j in range(debut, fin):
                longitude, latitude = conv_degr_rad(shape.points[j][0]) , conv_degr_rad(shape.points[j][1]) 
                merc = fonct_mercator(latitude)
                x = (L/2) * (longitude - centre)*echh + (400/1600)*L
                y = H - (H/2) * merc*ech + (1400/1200)*H
                nouvelle_coordo.append((x,y))
            partie.append(nouvelle_coordo)
        total.append(partie)
    return total



def dessiner(france_points: list, couleur: list):
    for i, points_dep in enumerate(france_points):
        if len(points_dep) == 1:
            fltk.polygone(points_dep, remplissage = couleur[i], epaisseur = 1, tag = f"polygon_{i}")
        else:
            for partie in points_dep:
                fltk.polygone(partie, remplissage= couleur[i], epaisseur = 1, tag = f"polygon_{i}")

def afficher_degres(L,H):
    y = 0
    for i in range(0, 40, 5): 
        fltk.texte(L-40, y, str(i)+"°", taille=10)
        y += H/8


def afficher_degrade(couleurs, L,H):
    y = 0
    for c in couleurs:
        fltk.rectangle(L-20, y, L, y+H/40, couleur=c, remplissage=c)
        y += H/40


def france2():
    H = 1200
    L = 1600
    HH = 600
    LL = 800
    ech = 4
    echh = 3
    sf = shapefile.Reader("departements-20140306-100m.shp") #ouverture du fichier shapefile
    fltk.cree_fenetre(L, H)
    centre = 0
    total = []
    for i in range(101):
        nouvelle_coordo = []
        for coord in sf.shape(i).points:
            longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
            merc = fonct_mercator(latitude)
            x = (L/2) * (longitude - centre)*echh + 800
            y = H - (H/2) * merc*ech + 1600
            nouvelle_coordo.append((x,y))
        nouvelle = []
        for i in range(len(nouvelle_coordo)-1):
            nouvelle.append(nouvelle_coordo[i]+nouvelle_coordo[i+1])
        nouvelle = [points for points in nouvelle if m.sqrt((points[2]-points[0])**2+(points[3]-points[1])**2) <= 10]  
        fltk.polygone(nouvelle,epaisseur=1.5)
        #for points in nouvelle:
           # if m.sqrt((points[2]-points[0])**2+(points[3]-points[1])**2) <= 10:
             #   fltk.ligne(points[0],points[1],points[2],points[3],epaisseur=1.5)
    fltk.mise_a_jour()
    fltk.attend_ev()
    fltk.ferme_fenetre()  


def dessiner2(lezip):
    H = 1200
    L = 1600
    HH = 600
    LL = 800
    ech = 4
    echh = 3
    sf = shapefile.Reader(lezip) #ouverture du fichier shapefile
    print(sf.records())
    fltk.cree_fenetre(L, H)
    centre = 0
    for i in range(0,813000,1000):
        nouvelle_coordo = []
        for coord in sf.shape(i).points:
            longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
            merc = fonct_mercator(latitude)
            x = (L/2) * (longitude - centre)*echh + 800
            y = H - (H/2) * merc*ech + 1600
            nouvelle_coordo.append((x,y))
        fltk.polygone(nouvelle_coordo, epaisseur = 1)
        print(f"{i*100/826872} %")
        fltk.mise_a_jour()
    fltk.attend_ev()
    fltk.ferme_fenetre()

def titre(H,L):
    fltk.texte(L/2,20, "Carte des variations de température en France", taille=20,ancrage='center')


################## teste de la methode sur une liste ########################
"""
points = [
    # Partie 1
    [(1.0, 44.0),
    (1.1, 44.1),
    (1.2, 44.0),

    # Partie 2
    (1.5, 44.2),
    (1.6, 44.3),
    (1.7, 44.2)]
]

liste = [0, 2, 4]
len_l = len(liste)
total = []

for i in range(1):
    partie = []
    for k in range(len_l):
        coord = []
        debut = liste[k]
        if k+1 < len(liste): # sil existe on prend l'indice
            fin = liste[k+1]
        else:
            fin = len(points[i]) #sinon on prend la fin de la liste
        print("debut",debut,"fin", fin)
        for j in range(debut, fin):
            print("j",j)
            coord.append(points[i][j])
        partie.append(coord)
    total.append(partie)

print(total)
"""
