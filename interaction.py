import fltk
import math as m
import constante


H = constante.H
L = constante.L

TAILLE_TXT_INFO = constante.TAILLE_TXT_INFO
TAILLE_TXT_B = constante.TAILLE_TXT_B



def affichage_info(x1:float, y1:float, departement: int, tag:str, sf, temps_json):
    """
    Permet d'afficher le nom et la température du département
    """
    nom = sf.record(departement)[1]
    try: 
        t_min, t_max = str(temps_json[sf.record(departement)[0]])
    except:
        print("Pas de donnée sur le département:", nom)
        t_min, t_max = "???"
    
    len_chaine = max(len(nom), len(t_max)+9, len(t_min)+9) # 9 = taille de la chaine temp
    
    rect_x2, rect_y2, marge_x, marge_y = taille_info(len_chaine, nbr_ligne = 3)
    
    fltk.rectangle(x1, y1, x1+rect_x2, y1+rect_y2, epaisseur = 1, remplissage = "white", tag = tag)
    texte(x1+marge_x, y1+marge_y, [t_max, t_min, nom], tag = tag)



# # TODO ? prendre en parametre un dico avec comme clé qui correspond 
# les coordonne de base et supplementaire pour calcule les coef
def taille_info(longueur_txt:int, taille_txt: int = TAILLE_TXT_INFO, nbr_ligne = 1):
    """
    Définie la taille du rectangle et la marge en fonction 
    de la longueur du texte et de sa taille

    """
    #coord supplementaire / taille_texte
    coef_l_x = 0.75 * taille_txt  # longueur rect pr une lettre en majuscule
    coef_txt_y = 1.875 # hauteur rectangle
    coef_marge_x = 0.25 # 2/8
    coef_marge_y = 0.5  # 4/8

    rect_x2 = coef_l_x * longueur_txt # longueur du rectangle
    rect_y2 = coef_txt_y * taille_txt * nbr_ligne #la hauteur du rectangle
    marge_x = coef_marge_x * taille_txt # marge du texte x
    marge_y = coef_marge_y * taille_txt # marge du texte y

    
    return rect_x2, rect_y2, marge_x, marge_y


def texte(x1, y1, texte: list, tag, taille_txt = TAILLE_TXT_INFO):
    """
    Affiche le nom de la commune dans le rectangle avec sa temperature maximal
    """
    #x1 += marge 
    #y1 += marge + 2
    t_max ,t_min, nom = texte
    chaine = nom + "\n" + f"t_max: {t_max}°C\nt_min: {t_min}°C"
    

    fltk.texte(x1, y1, chaine = chaine, ancrage = "nw", taille = taille_txt, tag = tag)


def milieu(depart_points: list):
    """
    Calcule le milieu du département en fonction de sa liste de points
    On fait un vecteur entre 2 points opposés et on calcule le milieu du segment
    On fait la moyenne de tous les milieux trouvé

    depart_points = [[(x,y), (x,y)], # partie 1
                     [(x,y), (x,y)], # partie 2
                     [...]
                    ]
    """
    moyenne_x = 0
    moyenne_y = 0
    nbr_points = 0

    for partie in depart_points:

        nbr_points_partie = m.floor((len(partie)//2))
        nbr_points += nbr_points_partie
        
        for i in range(nbr_points_partie):
            a = partie[i]
            b = partie[-i-1]
            milieu_point = ((b[0] + a[0])/2, (b[1] + a[1])/2)

            moyenne_x += milieu_point[0]
            moyenne_y += milieu_point[1]

    x = moyenne_x / nbr_points
    y = moyenne_y / nbr_points

    return (x, y)

# TODO on peut appeler reculer avancer tt les 1 seconde pour faire une animation
# TODO on peut afficher la date -> Nouran

def reculer(temps_json, liste_points):
    """
    Doit reafficher le dessin avec les temperatures de l'annee precedente si possible
    """
    
    print('reculer')


def avancer():
    """
    Doit reafficher le dessin avec les temperatures de l'annee suivante si possible
    """
    print('avancer')



def bouton_reculer(l, h, taille_txt, marge = 5):
    """
    Créer le bouton reculer en bas a gauche de la fenêtre
    """
    chaine = "reculer"
    rect_x2, rect_y2, marge_x, marge_y = taille_info(len(chaine), taille_txt)
    x1 = (20/1200)*l    # coef entre coord/la longueur de l'image 20/1200 -> a mettre dans taille info
    y1 = h - rect_y2 - marge 

    fltk.rectangle(x1, y1, x1+rect_x2, y1+rect_y2, remplissage = "white", tag = "reculer")
    fltk.texte(x1+marge_x, y1+marge_y,  chaine = chaine, ancrage = "nw", taille = taille_txt)



def bouton_avancer(l, h, taille_txt, marge = 5):
    """
    Créer le bouton avancer en bas a droite de la fenêtre
    """
    chaine = "avancer"
    rect_x2, rect_y2, marge_x, marge_y = taille_info(len(chaine), taille_txt)
    x1 = l - rect_x2 - marge 
    y1 = h - rect_y2 - marge
    x2 = x1 + rect_x2
    y2 = y1 + rect_y2

    fltk.rectangle(x1, y1, x2, y2, remplissage = "white", tag = "avancer")
    fltk.texte(x1 + marge_x, y1 + marge_y, chaine = chaine, ancrage = "nw", taille = taille_txt)
    
    return rect_x2 - marge


def affichageinfoavancé(H,L,departement: int, tag:str, sf, temps_json):
    """
    Permet d'afficher le nom et la température du département
    """
    x2 = L - 10
    y2 = H - 10
    x1 = x2 - 80
    y1 = y2 - 20

    nom = sf.record(departement)[1]
    try: 
        temperature = str(temps_json[sf.record(departement)[0]])
    except:
        print("Pas de donnée sur le département:", nom)
        temperature = "???"
    len_chaine = max(len(nom), len(temperature)+9) # taille de la chaine temp
    
    rect_x2, rect_y2, marge_x, marge_y = taille_info(len_chaine)
    fltk.rectangle(x1, y1, x2, y2, remplissage = "white", tag = tag)
    fltk.texte(x1/2, y1 - 3, [temperature, nom], ancrage = "center", tag=tag)

"""x2 = L - 10
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
"""

"""
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
                affichage_info(x, y, departement, tag = f"t_{departement}")
                #texte(x, y, 2, [sf.record(departement)[1]], tag = f"t_{departement}")

        if precedent is not None and departement != precedent:
            fltk.efface(f"t_{precedent}")
        precedent = departement

    else:
        if precedent is not None:
            fltk.efface(f"t_{precedent}")
            
    fltk.mise_a_jour()

"""