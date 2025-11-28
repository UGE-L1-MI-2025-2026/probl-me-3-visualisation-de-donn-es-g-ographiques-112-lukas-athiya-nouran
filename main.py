import shapefile
import fltk
import random

sf = shapefile.Reader("departements-20180101.shp") #ouverture du fichier shapefile

seine_et_marne = sf.shape(47) # Récupération de l'entrée correspondant à la Seine-et-Marne
seine_et_marne.bbox # Les points extrémaux de la seine-et-marne

fltk.cree_fenetre(800, 800)

fltk.ligne(780, 0, 780, 800)

def afficher_degres():
    y = 0
    for i in range(0, 36, 5): 
        fltk.texte(760, y, str(i)+"°", taille=10)
        y += 100
    

couleurs = ["#000062", "#200040", "#3F013E", "#B000B0", "#FC02BD","#D13800", "#FF8000", "#FFFF00"]
def afficher_degrade():
    y = 0
    for c in couleurs:
        fltk.rectangle(780, y, 800, y+100, remplissage=c)
        y += 100


for i in range(0 , 110):
    # try:
    #     for coord in sf.shape(i).points:
    #         fltk.polygone(points = [(20 * coord[0] + 100, 20 * coord[1] - (40*20) + 100)], remplissage = "red", epaisseur = 1)

    # except:
    #     print("existe pas", i)
    # fltk.mise_a_jour()
    try:
        points = [((20 * coord[0] + 300, 20 * coord[1] - (40*20) + 200)) for coord in sf.shape(i).points]
        fltk.polygone(points, epaisseur = 1)
    except:
        print("existe pas", i)
    fltk.mise_a_jour()


if __name__ == "main":
    afficher_degres()
    afficher_degrade()
    while True:
        ev = fltk.attend_ev()
        if fltk.type_ev(ev) == 'Quitte':
            fltk.ferme_fenetre()

    
