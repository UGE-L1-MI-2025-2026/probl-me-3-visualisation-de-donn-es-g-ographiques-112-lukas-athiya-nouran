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
    for i in range(len(sf.shapes())):
        shape = sf.shape(i)
        nbr_partie = len(shape.parts)

        if nbr_partie == 1: # regarde si le polygon est en une seule partie
            nouvelle_coordo = []
            for coord in shape.points:
                longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
                merc = fonct_mercator(latitude)
                x = (L/2) * (longitude - centre)*echh + 800
                y = H - (H/2) * merc*ech + 1600
                nouvelle_coordo.append((x,y))
            fltk.polygone(nouvelle_coordo, epaisseur = 1, tag = f"polygon_{i}")
            total.append(nouvelle_coordo)
        else:
            # s'il est en plusieurs parties on 
            # itère sur les parties
            for debut in range(nbr_partie-1):
                nouvelle_coordo = []
                # on fait une boucle avc
                # debut = le premier élément de parts (indexe du debut du polygon)
                # fin = l'élément suivant  
                for j in range(shape.parts[debut], shape.parts[max(0, min(debut+1, nbr_partie-1))]): 
                    
                    longitude, latitude = conv_degr_rad(shape.points[j][0]) , conv_degr_rad(shape.points[j][1]) 
                    merc = fonct_mercator(latitude)
                    x = (L/2) * (longitude - centre)*echh + 800
                    y = H - (H/2) * merc*ech + 1600
                    nouvelle_coordo.append((x,y))
                fltk.polygone(nouvelle_coordo, epaisseur = 1, tag = f"polygon_{i}")                
                total.append(nouvelle_coordo)
            
        print(i)
    return total

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





fltk.cree_fenetre(1600, 1200)
france(1600, 1200, shapefile.Reader("data/departement_shapefile/departements-20180101.shp") )
fltk.mise_a_jour()
fltk.attend_ev()

"""
liste = [0, 10, 20, 30]
len_l = len(liste)
total = []

if len_l == 0:
    # on fait
    pass
else:
    
    for debut in range(len(liste)-1): # partie
        coord = []
        for j in range(liste[debut], liste[max(0, min(debut+1, len(liste)-1))]): # les points par rapport a la partie
            
            print( f"poly{debut}", j)
            coord.append(j)
        #creer le polygone
        total.append(coord)

print(total)"""