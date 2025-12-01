import fltk
import shapefile
import functions
# polygone -> survole -> indice -> departement dans le shapefilee -> info du département a cette indice

MARGE = 2
H = 1200
L = 1600

sf = shapefile.Reader("data/departement_shapefile/departements-20180101.shp")
fltk.cree_fenetre(L, H)
liste_points = functions.france(L, H, sf)

dico = {f'{i}': points for i,points in enumerate(liste_points)}
precedent = None


def rectangle(x1, y1, tag):
    """
    Affiche un rectangle 
    """
    x2 = x1 + 80
    y2 = y1 + 20
    fltk.rectangle(x1, y1, x2, y2, epaisseur = 1, remplissage = "white", tag = tag)


def texte(x1, y1, marge, info: list[str], tag):
    """
    Affiche le nom de la commune dans le rectangle
    """
    nom = info[0]
    x1 += marge
    y1 += marge + 2
    fltk.texte(x1,y1, chaine = nom, ancrage = "nw", taille = 8, tag = tag)


def milieu(points: list):
    """
    Calcule le milieu du département en fonction de sa liste de points
    On fait un vecteur entre 2 points opposés et on calcule le milieu du segment
    On fait la moyenne de tous les milieux trouvé

    points = [(x,y), (x,y)]
    """
    moyenne_x = 0
    moyenne_y = 0
    nbr_points = len(points)//2

    for i in range(nbr_points):
        a = points[i]
        b = points[-i-1]
        milieu_point = ((b[0] + a[0])/2, (b[1] + a[1])/2)

        moyenne_x += milieu_point[0]
        moyenne_y += milieu_point[1]

    x = moyenne_x / nbr_points
    y = moyenne_y / nbr_points

    return (x, y)




x2 = L - 10
y2 = H - 10
x1 = x2 - 80
y1 = y2 - 20

fltk.rectangle(x1, y1, x2, y2, remplissage = "white", tag = "avancer")
fltk.texte(x1 + 3, y1 - 3, chaine = "avancer", ancrage = "nw", taille = 15)

x2 = 90
y2 = H-10
x1 = 10
y1 = y2 -20
fltk.rectangle(x1, y1, x2, y2, remplissage = "white", tag = "reculer")
fltk.texte(x1 +3, y1 - 2, chaine = "reculer", ancrage = "nw", taille = 15)


def reculer():
    print('reculer')

def avancer():
    print('avancer')


while True:

    ev = fltk.donne_ev()

    if fltk.objet_survole():
        if type(fltk.objet_survole()) == int:
            if precedent is not None:
                fltk.efface("1")
            departement = fltk.objet_survole()
            print(departement)
            precedent = departement
            
            if departement is not None:
                x, y = milieu(dico[f"{departement-1}"])
                rectangle(x,y, tag = "1")
                texte(x, y, 2 ,[sf.record(departement)[1]], tag = "1")
            
            
        else:
            if fltk.type_ev(ev) == "ClicGauche":
                if fltk.est_objet_survole("reculer"):
                    reculer()
                    
                elif fltk.est_objet_survole("avancer"):
                    avancer()

        fltk.efface(precedent)
    elif fltk.type_ev(ev) == "Quitte":
        print("non")
        fltk.efface_tout()
        fltk.ferme_fenetre()
    fltk.mise_a_jour()

