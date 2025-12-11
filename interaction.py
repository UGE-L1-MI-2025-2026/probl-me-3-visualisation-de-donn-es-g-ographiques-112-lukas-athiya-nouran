import fltk
import math as m
import constante
import temperature as temp
import affichage



H = constante.H
L = constante.L

TAILLE_TXT_INFO = constante.TAILLE_TXT_INFO
TAILLE_TXT_B = constante.TAILLE_TXT_B



def affichage_info(x1:float, y1:float, departement: int, tag:str, sf, temps_json, tmax: int = 0):
    """
    Permet d'afficher le nom et la température du département 
    """
    info = sf.record(departement)
    nom = info[1]
    try: 
        temp = str(temps_json[info[0][:2]][tmax])
    except:
        print("Pas de donnée sur le département:", nom)
        temp  = "???"
    
    len_chaine = max(len(nom), len(temp)+9) # 9 = taille de la chaine temp
    
    rect_x2, rect_y2, marge_x, marge_y = taille_info(len_chaine, nbr_ligne = 2)
    
    fltk.rectangle(x1, y1, x1+rect_x2, y1+rect_y2, epaisseur = 1, remplissage = "white", tag = tag)
    texte(x1+marge_x, y1+marge_y, [temp, nom], tag, tmax)



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
    rect_y2 = coef_txt_y * taille_txt * nbr_ligne # la hauteur du rectangle
    marge_x = coef_marge_x * taille_txt # marge du texte x
    marge_y = coef_marge_y * taille_txt # marge du texte y

    
    return rect_x2, rect_y2, marge_x, marge_y



def texte(x1, y1, texte: list, tag: str, tmax: int, taille_txt = TAILLE_TXT_INFO):
    """
    Affiche le nom de la commune dans le rectangle avec sa temperature maximal
    """
    temp, nom = texte
    chaine = nom + "\n"
    if tmax == 0:
        chaine += f"t_max: {temp}°C"
    else:
        chaine+= f"t_min: {temp}°C"

    fltk.texte(x1, y1, chaine = chaine, ancrage = "nw", taille = taille_txt, tag = tag)



def milieu(depart_points: list):
    """
    Calcule le milieu du département en fonction de sa liste de points
    On fait un vecteur entre 2 points opposés et on calcule le milieu du vecteur
    On fait la moyenne de tous les milieux trouvé

    depart_points = [[(x,y), (x,y)], # partie 1
                     [(x,y), (x,y)], # partie 2
                     [...]
                    ]
    """
    moyenne_x = 0
    moyenne_y = 0
    nbr_vecteurs = 0

    for partie in depart_points:
        
        nbr_vecteurs_partie = m.floor((len(partie)//2)) 
        nbr_vecteurs += nbr_vecteurs_partie
        
        for i in range(nbr_vecteurs_partie):
            a = partie[i]
            b = partie[-i-1]
            milieu_point = ((b[0] + a[0])/2, (b[1] + a[1])/2)

            moyenne_x += milieu_point[0]
            moyenne_y += milieu_point[1]

    x = moyenne_x / nbr_vecteurs
    y = moyenne_y / nbr_vecteurs

    return (x, y)



def reculer(f_temp, sf, annee, tmax, borne = 2018):
    """
    Doit reafficher le dessin avec les temperatures de l'annee precedente si possible
    """

    n_annee = int(annee) - 1
    
    if n_annee < borne:
        print("Vous ne pouvez pas reculer d'avantage dans le temps")
        return annee
    else:
        n_annee = str(n_annee)
        temps_json = temp.carte_exemple(n_annee, f_temp)
        depart_couleurs = temp.couleur_departement(temps_json, sf, tmax)

        affichage.effacer_dep(sf)
        liste_points = affichage.france(L, H, sf)
        affichage.dessiner(liste_points, depart_couleurs)

    return liste_points, temps_json, n_annee



def avancer(f_temp, sf, annee, tmax, borne = 2025):
    """
    Doit reafficher le dessin avec les temperatures de l'annee suivante si possible
    """
    n_annee = int(annee) + 1
    
    if n_annee > borne:
        print("Vous ne pouvez pas avancer d'avantage dans le temps")
        return str(annee)
    
    else:
        n_annee = str(n_annee)
        temps_json = temp.carte_exemple(n_annee, f_temp)
        depart_couleurs = temp.couleur_departement(temps_json, sf, tmax)

        affichage.effacer_dep(sf)
        liste_points = affichage.france(L, H, sf)
        affichage.dessiner(liste_points, depart_couleurs)

        return liste_points, temps_json, n_annee




def bouton_reculer(l, h, taille_txt, marge = 5):
    """
    Créer le bouton reculer en bas a gauche de la fenêtre
    """
    chaine = "reculer"
    rect_x2, rect_y2, marge_x, marge_y = taille_info(len(chaine), taille_txt)
    x1 = (20/1200)*l    # coef entre coord/la longueur de l'image 20/1200 -> a mettre dans taille info
    y1 = h - rect_y2 - marge 

    fltk.rectangle(x1, y1, x1+rect_x2, y1+rect_y2, remplissage = "white", tag = "reculer")
    fltk.texte(x1+marge_x, y1+marge_y - marge,  chaine = chaine, ancrage = "nw", taille = taille_txt)



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
    fltk.texte(x1 + marge_x, y1 + marge_y-marge, chaine = chaine, ancrage = "nw", taille = taille_txt)
    
    return rect_x2 - marge



def bouton_animation(l, h, taille_txt, boole ,marge = 5):
    """
    Créer le bouton pour arreter ou lancer l'animation 
    """
    try:
        fltk.efface("animation")
    except:
        pass

    if boole:
        chaine = "Stopper l'animation"
    else:
        chaine = "Animation"

    rect_x2, rect_y2, marge_x, marge_y = taille_info(len(chaine), taille_txt)
    x1 = (20/1200)*l   
    y1 = h - rect_y2 - marge - 80

    fltk.rectangle(x1, y1, x1+rect_x2, y1+rect_y2, remplissage = "white", tag = "animation")
    fltk.texte(x1+marge_x, y1+marge_y - marge,  chaine = chaine,
                ancrage = "nw", taille = taille_txt, tag = "animation")



def change_temp(l, h, taille_txt, marge = 5, tmax: int = 0):
    """
    Créer un bouton et permet de changer entre les températures minimales et maximales
    """
    chaine = "Afficher température " 
    maxi = "maximale"
    mini = "minimale"
    long = len(chaine) + len(mini)
    rect_x2, rect_y2, marge_x, marge_y = taille_info(long, taille_txt)
    x1 = (20/1200)*l  
    y1 = h - rect_y2 - marge - 40
    fltk.rectangle(x1, y1, x1 + rect_x2, y1 + rect_y2 , 
                   remplissage = "white", tag = "temp")
    
    if tmax == 0:
        try:
            fltk.efface("t_1")
        except:
            pass
        chaine += maxi
        fltk.texte(x1+marge_x, y1 + marge_y - marge,  chaine = chaine,
                   ancrage = "nw", taille = taille_txt, tag = "t_0")
        return 1
    else:
        try:
            fltk.efface("t_0")
        except:
            pass
        chaine += mini
        fltk.texte(x1 + marge_x, y1 + marge_y - marge, chaine = chaine, 
                   ancrage = "nw", taille = taille_txt, tag = "t_1")
        
        return 0
    

