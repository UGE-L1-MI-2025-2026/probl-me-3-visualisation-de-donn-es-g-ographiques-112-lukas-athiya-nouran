import math as m
import fltk
import shapefile
from tkinter import filedialog as fd


def conv_rad_degr(rad):
    return (rad*180)/m.pi

def conv_degr_rad(degre):
    return (degre*m.pi)/180

def fonct_mercator(latitude):
    return  m.log(m.tan((latitude / 2) + (m.pi / 4)))

def france():
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
    for i in range(len(sf.shapes())):
<<<<<<< HEAD
        shape = sf.shape(i)
        nbr_partie = len(shape.parts)

        if nbr_partie == 0:
            nouvelle_coordo = []
            for coord in shape.points:
                longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
                merc = fonct_mercator(latitude)
                x = (L/2) * (longitude - centre)*echh + 800
                y = H - (H/2) * merc*ech + 1600
                nouvelle_coordo.append((x,y))
            fltk.polygone(nouvelle_coordo, epaisseur = 1, tag = f"polygon_{i}")
        else:
            for debut in range(nbr_partie):
                for j in range(shape.points[debut], shape.points[max(0, min(debut+1, nbr_partie-1))]):
                    nouvelle_coordo = []
                    longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1]) #coordonnes en fonction de j
                    merc = fonct_mercator(latitude)
                    x = (L/2) * (longitude - centre)*echh + 800
                    y = H - (H/2) * merc*ech + 1600
                    nouvelle_coordo.append((x,y))
                fltk.polygone(nouvelle_coordo, epaisseur = 1, tag = f"polygon_{i}")
=======
        nouvelle_coordo = []
        for coord in sf.shape(i).points:
            longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
            merc = fonct_mercator(latitude)
            x = (L/2) * (longitude - centre)*echh + 800
            y = H - (H/2) * merc*ech + 1600
            nouvelle_coordo.append((x,y))
        for k in range(len(sf.shape(i).parts)): 
            if not k+1:   
                fltk.polygone(nouvelle_coordo[k:], epaisseur = 1)
            else:
                fltk.polygone(nouvelle_coordo[k:k+1], epaisseur = 1)
>>>>>>> 81aac663e9288e3637a29b6094181f5cfe5786d1
        print(i)
        total += nouvelle_coordo
    fltk.mise_a_jour()
    fltk.attend_ev()
    fltk.ferme_fenetre()

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
        print(nouvelle_coordo[1])
        nouvelle = []
        for i in range(len(nouvelle_coordo)-1):
            nouvelle.append(nouvelle_coordo[i]+nouvelle_coordo[i+1])
        #nouvelle = [(points[0],points[1]) for points in nouvelle if m.sqrt((points[2]-points[0])**2+(points[3]-points[1])**2) <= 10]  
        #fltk.polygone(nouvelle,epaisseur=1.5)
        print(nouvelle[1])
        for points in nouvelle:
            if m.sqrt((points[2]-points[0])**2+(points[3]-points[1])**2) <= 10:
                fltk.ligne(points[0],points[1],points[2],points[3],epaisseur=1.5)
    fltk.mise_a_jour()
    fltk.attend_ev()
    fltk.ferme_fenetre()  


def dessiner(lezip):
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
france()




liste = [0, 10, 20 ,30]
len_l = len(liste)

if len_l == 0:
    # on fait
    pass
else:
    for debut in range(len(liste)): # partie
        #nouvelle coord
        for j in range(liste[debut], liste[max(0, min(debut+1, len(liste)-1))]): # les points par rapport a la partie

            print( f"poly{debut}", i)
            # poly