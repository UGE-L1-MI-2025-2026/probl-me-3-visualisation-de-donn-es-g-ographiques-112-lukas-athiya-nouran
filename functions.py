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

def france(L, H, sf):
    ech = 4
    echh = 3
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
        print(fltk.polygone(nouvelle_coordo, epaisseur = 1))

        total.append(nouvelle_coordo)
    print("Fini")
    return total



def dessiner(lezip):
    H = 1200
    L = 1600
    HH = 600
    LL = 800
    ech = 4
    echh = 3
    sf = shapefile.Reader(lezip) #ouverture du fichier shapefile
    fltk.cree_fenetre(L, H)
    centre = 0
    for i in range(101):
        nouvelle_coordo = []
        for coord in sf.shape(i).points:
            longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
            merc = fonct_mercator(latitude)
            x = (L/2) * (longitude - centre)*echh + 800
            y = H - (H/2) * merc*ech + 1600
            nouvelle_coordo.append((x,y))
        fltk.polygone(nouvelle_coordo, epaisseur = 1)
        print(i)
    fltk.mise_a_jour()
    fltk.attend_ev()
    fltk.ferme_fenetre()
#filename = fd.askopenfilename()
#dessiner(f"{filename}/land-polygons-complete-4326/land_polygons.shp")

