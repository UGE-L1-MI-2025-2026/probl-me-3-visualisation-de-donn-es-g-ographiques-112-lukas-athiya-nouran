import shapefile
import fltk


sf = shapefile.Reader("departements-20180101.shp") #ouverture du fichier shapefile


fltk.cree_fenetre(1920, 1080)

seine_et_marne = sf.shape(47) # Récupération de l'entrée correspondant à la Seine-et-Marne
seine_et_marne.bbox # Les points extrémaux de la seine-et-marne



for i in range(101):
    for coord in sf.shape(i).points:
        fltk.polygone(points = [20*coord[0]+100, 20*coord[1]-(40*20)], epaisseur = 1)
    print(i)
    
fltk.mise_a_jour()
fltk.attend_ev()
fltk.ferme_fenetre()
