import shapefile
import fltk
import random

sf = shapefile.Reader("departements-20180101.shp") #ouverture du fichier shapefile

seine_et_marne = sf.shape(47) # Récupération de l'entrée correspondant à la Seine-et-Marne
seine_et_marne.bbox # Les points extrémaux de la seine-et-marne

fltk.cree_fenetre(800, 800)

couleurs = ["green", "red", "orange", "blue", "purple"]

def couleur(couleurs):
    random.choices(couleurs)

for i in range(0 , 110):
    # try:
    #     for coord in sf.shape(i).points:
    #         fltk.polygone(points = [(20 * coord[0] + 100, 20 * coord[1] - (40*20) + 100)], remplissage = "red", epaisseur = 1)

    # except:
    #     print("existe pas", i)
    
    try:
        points = [((20 * coord[0] + 300, 20 * coord[1] - (40*20) + 200)) for coord in sf.shape(i).points]
        fltk.polygone(points, epaisseur = 1)
    except:
        print("existe pas", i)
    fltk.mise_a_jour()

    
while True:
    ev = fltk.attend_ev()
    if fltk.type_ev(ev) == 'Quitte':
        fltk.ferme_fenetre()
