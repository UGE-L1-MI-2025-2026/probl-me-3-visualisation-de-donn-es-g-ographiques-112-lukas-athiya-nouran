import math as m
import fltk



def conv_rad_degr(rad):
    return (rad*180)/m.pi


def conv_degr_rad(degre):
    return (degre*m.pi)/180


def fonct_mercator(latitude):
    return  m.log(m.tan((latitude / 2) + (m.pi / 4)))


def france(L, H, sf):
    '''
    fonction permettant de dessiner l'objet sf (dessine la france)
    
    '''
    L *= 1.5
    H *= 1.5
    ech = 4
    echh = 3
    centre = 0
    total = []
    for i in range(len(sf.shapes())):
        shape = sf.shape(i)
        nbr_partie = len(shape.parts)
        partie = []
        texte_dom_tom = []
        for k in range(nbr_partie):
            nouvelle_coordo = []
            # on fait une boucle avc
            # debut = le premier élément de parts (indexe du debut du polygon)
            debut = shape.parts[k]
            # fin = l'élément suivant s'il existe 
            if k+1 < len(shape.parts):
                fin = shape.parts[k+1]
            # sinon on prend la longueur de la liste des points
            else:
                fin = len(shape.points)

            for j in range(debut, fin):
                longitude, latitude = conv_degr_rad(shape.points[j][0]) , conv_degr_rad(shape.points[j][1]) 
                merc = fonct_mercator(latitude)
                x = (L/2) * (longitude - centre)*echh + (400/1600)*L
                y = H - (H/2) * merc*ech + (1400/1200)*H
                nouvelle_coordo.append((x,y))

            dom_tom = ('La Réunion', 'Martinique', 'Guadeloupe', 'Guyane', 'Mayotte')
            nom_shp = sf.record(i).nom
            
            if nom_shp in dom_tom:
                ecart = dom_tom.index(nom_shp)
                minx = min([x for x, _ in nouvelle_coordo])
                miny = min([y for _, y in nouvelle_coordo])
                echelle = 0.2 if nom_shp == 'Guyane' else 1
                nouvelle_coordo = [((x-minx)*echelle+10, (y-miny)*echelle+250+50*ecart) for x, y in nouvelle_coordo]
                
                minx = min([x for x, _ in nouvelle_coordo])
                maxy = max([y for _, y in nouvelle_coordo])
                if nom_shp not in texte_dom_tom:
                    fltk.texte(minx, maxy+5, nom_shp, taille=10)
                    texte_dom_tom.append(nom_shp)

            partie.append(nouvelle_coordo)
        total.append(partie)
    return total



def dessiner(france_points: list, couleur: list):
    for i, points_dep in enumerate(france_points):
        if len(points_dep) == 1:
            fltk.polygone(points_dep, remplissage = couleur[i], epaisseur = 1, tag = f"polygon_{i}")
        else:
            for partie in points_dep:
                fltk.polygone(partie, remplissage= couleur[i], epaisseur = 1, tag = f"polygon_{i}")



def afficher_degres(l, h):
    y = 0
    for i in range(-15, 40, 5):
        fltk.texte(l-42, y, str(i)+"°", taille=10)
        y += h/10




def afficher_degrade(couleurs, l,h):
    y = 0
    for c in couleurs:
        fltk.rectangle(l-20, y, l, y+h/50, couleur=c, remplissage=c)
        y += h/50




def effacer_dep(sf):
    """
    Permet d'effacer tous les departements 
    """
    for i in range(len(sf.shapes())):
        fltk.efface(f"polygon_{i}")



def titre(H,L):
    '''
    Afficher le titre de la Carte

    '''
    fltk.texte(L/2,20, "Carte des variations de température en France", taille=20, ancrage='center')



def datedynamique(H,L,date): 
    '''
    afficher dynamiquement la date en annee de l'affichage
    '''
    fltk.efface("tag1")  
    fltk.texte(L/2,60, f"en {date}", taille=20, ancrage='center',tag="tag1")

def menu(l= 800, h = 600):

    fltk.cree_fenetre(l, h)
    fltk.texte(l/2, 50, "Menu", taille=80, ancrage='center')
    fltk.texte(l/2 - 100, 350, "France", taille=20, ancrage='center', tag = "france")
    fltk.texte(l/2 + 100, 350, "Bonus", taille=20, ancrage='center', tag = "bonus")
    fltk.rectangle(l/2 - 170, 300, l/2 - 20, 400, tag = "france")
    fltk.rectangle(l/2 + 30 , 300, l/2+180, 400, tag = "bonus")