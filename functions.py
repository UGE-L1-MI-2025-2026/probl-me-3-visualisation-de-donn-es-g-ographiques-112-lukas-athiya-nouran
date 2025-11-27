import shapefile
import fltk
import math as m

H = 600
L = 800

sf = shapefile.Reader("departements-20180101.shp") #ouverture du fichier shapefile

fltk.cree_fenetre(1920, 1080)



def conv_rad_degr(rad):
    return (rad*180)/m.pi

def conv_degr_rad(degre):
    return (degre*m.pi)/180

def fonct_mercator(latitude):
    return  m.log(m.tan((latitude / 2) + (m.pi / 4)))

        

for i in range(101):
    nouvelle_coordo = []
    for coord in sf.shape(i).points:
        longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
        
        x = n * (longitude - centre)        # cest quoi n ?
        y = n * fonct_mercator(latitude)
        nouvelle_coordo.append((x,y))
    fltk.polygone(nouvelle_coordo, epaisseur = 2)
    print(i)







fltk.mise_a_jour()
fltk.attend_ev()
fltk.ferme_fenetre()