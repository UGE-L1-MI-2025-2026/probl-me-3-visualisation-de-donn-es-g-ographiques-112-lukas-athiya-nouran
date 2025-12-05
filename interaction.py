import fltk
import shapefile
import functions
import math as m
# polygone -> survole -> indice -> departement dans le shapefilee -> info du département a cette indice

#MARGE = 2
H = 1200
L = 1600
TAILLE_TXT_INFO = 15
TAILLE_TXT_B = 15


sf = shapefile.Reader("data/departement_shapefile/departements-20180101.shp")
fltk.cree_fenetre(L, H)
liste_points = functions.france(L, H, sf)
precedent = None


def affichage_info(x1, y1, departement: int, tag):
    rect_x2, rect_y2, marge_x, marge_y = taille_info()

    rectangle(x1, y1, x1+rect_x2, y1+rect_y2, tag = tag)
    texte(x1+marge_x, y1+marge_y, [f"?°C", sf.record(departement)[1]], tag = tag)

# TODO faire la meme pour les boutons avancer, reculer

def taille_info(taille_txt: int = TAILLE_TXT_INFO, texte = None):
    """
    Définie la taille du rectangle en fonction de la longueur du texte

    texte = [temp: int, nom du département: str]
    """
    #coord supplementaire / taille_texte
    coef_txt_x = 10
    coef_txt_y = 2.5
    coef_marge_x = 0.25
    coef_marge_y = 0.5

    rect_x2 = coef_txt_x * taille_txt # TODO ajuster la longueur en fonction de la taille de la chaine
    rect_y2 = coef_txt_y * taille_txt
    marge_x = coef_marge_x * taille_txt
    marge_y = coef_marge_y * taille_txt

    
    return rect_x2, rect_y2, marge_x, marge_y


def rectangle(x1, y1, x2, y2, tag):
    """
    Affiche un rectangle 
    """
    #x2 = x1 + 80 
    #y2 = y1 + 20 
    fltk.rectangle(x1, y1, x2, y2, epaisseur = 1, remplissage = "white", tag = tag)


def texte(x1, y1, texte: list, tag, taille_txt = TAILLE_TXT_INFO):
    """
    Affiche le nom de la commune dans le rectangle
    """
    # TODO ajouter une ligne (y*2) pour la temp
    temperature, nom = texte[0], texte[1]
    
    #x1 += marge 
    #y1 += marge + 2
    fltk.texte(x1, y1, chaine = nom, ancrage = "nw", taille = taille_txt, tag = tag)


def milieu(points: list):
    """
    Calcule le milieu du département en fonction de sa liste de points
    On fait un vecteur entre 2 points opposés et on calcule le milieu du segment
    On fait la moyenne de tous les milieux trouvé

    points = [(x,y), (x,y)]
    """
    moyenne_x = 0
    moyenne_y = 0
    nbr_points = m.floor((len(points)//2))

    for i in range(nbr_points):
        a = points[i]
        b = points[-i-1]
        milieu_point = ((b[0] + a[0])/2, (b[1] + a[1])/2)

        moyenne_x += milieu_point[0]
        moyenne_y += milieu_point[1]

    x = moyenne_x / nbr_points
    y = moyenne_y / nbr_points

    return (x, y)


def reculer():
    print('reculer')


def avancer():
    print('avancer')




x2 = L - 10
y2 = H - 10
x1 = x2 - 80
y1 = y2 - 20

fltk.rectangle(x1, y1, x2, y2, remplissage = "white", tag = "avancer")
fltk.texte(x1 + 3, y1 - 3, chaine = "avancer", ancrage = "nw", taille = TAILLE_TXT_B)

x2 = 90
y2 = H-10
x1 = 10
y1 = y2 -20
fltk.rectangle(x1, y1, x2, y2, remplissage = "white", tag = "reculer")
fltk.texte(x1 +3, y1 - 2, chaine = "reculer", ancrage = "nw", taille = TAILLE_TXT_B)



while True:

    ev = fltk.donne_ev()
    obj_s = fltk.objet_survole()

    if fltk.type_ev(ev) == "ClicGauche":
            if fltk.est_objet_survole("reculer"):
                reculer()
                
            elif fltk.est_objet_survole("avancer"):
                avancer()

    elif fltk.type_ev(ev) == "Quitte":
        fltk.efface_tout()
        fltk.ferme_fenetre()

    if obj_s:
        tag = fltk.recuperer_tags(obj_s)
        if tag and tag[0].startswith("polygon_"):
            departement = int(tag[0].split("_")[1])
            if departement is not None:
                x, y = milieu(liste_points[departement])
                affichage_info(x, y, departement, f"t_{departement}")
                #rectangle(x, y, tag = f"t_{departement}")
                #texte(x, y, 2, [sf.record(departement)[1]], tag = f"t_{departement}")

        if precedent is not None and departement != precedent:
            fltk.efface(f"t_{precedent}")
        precedent = departement

    else:
        if precedent is not None:
            fltk.efface(f"t_{precedent}")
            
    fltk.mise_a_jour()

