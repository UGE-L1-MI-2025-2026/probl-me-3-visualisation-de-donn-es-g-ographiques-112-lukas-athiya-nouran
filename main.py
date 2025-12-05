import shapefile
import fltk
from couleurs import *
import math as m 
from test import *

sf = shapefile.Reader("data\departement_shapefile\departements-20180101.shp") #ouverture du fichier shapefile

seine_et_marne = sf.shape(47) # Récupération de l'entrée correspondant à la Seine-et-Marne
seine_et_marne.bbox # Les points extrémaux de la seine-et-marne

fltk.cree_fenetre(800, 800)

fltk.ligne(780, 0, 780, 800)

def afficher_degres():
    y = 0
    for i in range(0, 36, 5): 
        fltk.texte(760, y, str(i)+"°", taille=10)
        y += 100
    
afficher_degres()

def afficher_degrade():
    y = 0
    for c in couleurs:
        fltk.rectangle(780, y, 800, y+20, couleur=c, remplissage=c)
        y += 20

afficher_degrade()

def temp_to_couleur(temp, couleurs):
    if temp <= 0:
        return couleurs[0]
    elif temp >= 39:
        return couleurs[-1]
    indice = round(temp)
    return couleurs[indice]
    
def conv_rad_degr(rad):
    return (rad*180)/m.pi

def conv_degr_rad(degre):
    return (degre*m.pi)/180

def fonct_mercator(latitude):
    return  m.log(m.tan((latitude / 2) + (m.pi / 4)))

def france(H, L, ech, echh, couleurs, temps_json):
    sf = shapefile.Reader("data\departement_shapefile\departements-20180101.shp") #ouverture du fichier shapefile
    
    centre = 0
    for i in range(101):
        nouvelle_coordo = []
        for coord in sf.shape(i).points:
            longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
            merc = fonct_mercator(latitude)
            x = (L) * (longitude - centre)*echh + 300 
            y = H - (H/2) * merc*ech + 1000 
            nouvelle_coordo.append((x,y))

        code_shp = sf.record(i)[0]
        code_sans_lettre = code_shp[:2]
        if code_sans_lettre in temps_json:
            temp = temps_json[code_sans_lettre]
            couleur = temp_to_couleur(temp, couleurs)
        else:
            couleur = "#CCCCCC"
        
        nouvelle = []
        for i in range(len(nouvelle_coordo)-1):
            nouvelle.append(nouvelle_coordo[i]+nouvelle_coordo[i+1])
        nouvelle = [points for points in nouvelle if m.sqrt((points[2]-points[0])**2+(points[3]-points[1])**2) <= 10]  
        fltk.polygone(nouvelle, remplissage=couleur, epaisseur = 1.5)
        print(i)
    fltk.mise_a_jour()
    fltk.attend_ev()
    fltk.ferme_fenetre()

france(800, 800, 4, 3, couleurs, carte_exemple())

while True:
    ev = fltk.attend_ev()
    if fltk.type_ev(ev) == 'Quitte':
        fltk.ferme_fenetre()

    
