import shapefile
import fltk
from couleurs import *
import math as m 
from temperature import *

fltk.cree_fenetre(1000, 900)

def afficher_degres():
    y = 0
    for i in range(0, 36, 5): 
        fltk.texte(960, y, str(i)+"°", taille=10)
        y += 100
    
afficher_degres()

def afficher_degrade():
    y = 0
    for c in COULEUR:
        fltk.rectangle(980, y, 1000, y+20, couleur=c, remplissage=c)
        y += 20

afficher_degrade()

def temp_to_couleur(temp, couleurs):
    if temp <= 0:
        return couleurs[0]
    if temp >= 39:
        return couleurs[-1]
    indice = round(temp)
    return couleurs[indice]
    
def conv_rad_degr(rad):
    return (rad*180)/m.pi

def conv_degr_rad(degre):
    return (degre*m.pi)/180

def fonct_mercator(latitude):
    return m.log(m.tan((latitude / 2) + (m.pi / 4)))

def france(H, L, ech, echh, couleurs, temps_json):
    identifiants = {}
    sf = shapefile.Reader("data\departement_shapefile\departements-20180101.shp") #ouverture du fichier shapefile
    
    centre = 0
    for i in range(102):
        parties = list(sf.shape(i).parts) + [len(sf.shape(i).points)]
        # print(f"parts: {sf.shape(i).parts}, len_points: {len(sf.shape(i).points)}, parties: {parties}")
        texte_dom_tom = []
        for j in range(len(parties)-1):
            debut = parties[j]
            fin = parties[j+1]

            coordonnee = []
            for coord in sf.shape(i).points[debut:fin]:
                longitude, latitude = conv_degr_rad(coord[0]) , conv_degr_rad(coord[1])
                merc = fonct_mercator(latitude)
                x = (L) * (longitude - centre)*echh + 400 
                y = H - (H/2) * merc*ech + 1050
                coordonnee.append((x,y))
            
            dom_tom = ('La Réunion', 'Martinique', 'Guadeloupe', 'Guyane', 'Mayotte')
            nom_shp = sf.record(i).nom
            
            if nom_shp in dom_tom:
                ecart = dom_tom.index(nom_shp)
                minx = min([x for x, _ in coordonnee])
                miny = min([y for _, y in coordonnee])
                echelle = 0.2 if nom_shp == 'Guyane' else 1
                coordonnee = [((x-minx)*echelle+10, (y-miny)*echelle+450+50*ecart) for x, y in coordonnee]
                
                minx = min([x for x, _ in coordonnee])
                maxy = max([y for _, y in coordonnee])
                if nom_shp not in texte_dom_tom:
                    fltk.texte(minx, maxy+5, nom_shp, taille=10)
                    texte_dom_tom.append(nom_shp)

            code_shp = sf.record(i).code_insee
            code_sans_lettre = code_shp[:2]
            if code_sans_lettre in temps_json:
                temp = temps_json[code_sans_lettre]
                couleur = temp_to_couleur(temp, couleurs)
            else:
                couleur = "#CCCCCC"
            
            id = fltk.polygone(coordonnee, couleur="#767676", remplissage=couleur, epaisseur = 0.5)
            identifiants[id] = i
        fltk.mise_a_jour()
    return identifiants

identifiants = france(800, 800, 4, 3, COULEUR, carte_exemple())
#print(identifiants)

while True:
    ev = fltk.attend_ev()
    if fltk.type_ev(ev) == "ClicGauche":
        print([sf.record(identifiants[id]).nom for id in fltk.liste_objets_survoles()])
    if fltk.type_ev(ev) == 'Quitte':
        fltk.ferme_fenetre()

    
