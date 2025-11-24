import shapefile
import fltk
import random

sf = shapefile.Reader("departements-20180101.shp") #ouverture du fichier shapefile


fltk.cree_fenetre(1920, 1080)

seine_et_marne = sf.shape(47) # Récupération de l'entrée correspondant à la Seine-et-Marne
seine_et_marne.bbox # Les points extrémaux de la seine-et-marne

def couleur(couleurs):
    random.choices(couleurs)

couleurs = ["green", "red", "orange", "blue", "purple"]

for i in range(0,110):
    try:
        for coord in sf.shape(i).points:
            fltk.polygone(points = [20*coord[0]+100, 20*coord[1]-(40*20)], remplissage= "red", epaisseur = 2)
        print(i)
    except:
        print("existe pas", i)

fltk.mise_a_jour()
fltk.attend_ev()
fltk.ferme_fenetre()