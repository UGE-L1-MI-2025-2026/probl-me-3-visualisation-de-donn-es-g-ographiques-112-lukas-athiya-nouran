import fltk as f
import shapefile

# polygone -> survole -> indice -> departement dans le shapefilee -> info du département a cette indice

MARGE = 2

f.cree_fenetre(800, 600)



sf = shapefile.Reader("data/departement_shapefile/departements-20180101.shp")

def rectangle(x1, y1):
    """
    Affiche un rectangle 
    """
    x2 = x1 + 80
    y2 = y1 + 20
    f.rectangle(x1, y1, x2, y2, epaisseur = 1, remplissage = "white")


def texte(x1, y1, marge, info: list[str]):
    """
    Affiche le nom de la commune dans le rectangle
    """
    nom = info[0]
    x1 += marge
    y1 += marge + 2
    f.texte(x1,y1, chaine = nom, ancrage = "nw", taille = 8)


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



for i in range(101):
    points = [((20 * coord[0] + 300, 20 * coord[1] - (40*20) + 200)) for coord in sf.shape(i).points]
    x, y = milieu(points)
    rectangle(x,y)  
    texte(x, y, 2 ,[sf.record(i)[1]])




while True:
    ev = f.donne_ev()
    if f.type_ev(ev) == "Quitte":
        f.efface_tout()
        f.ferme_fenetre()
    
    if f.objet_survole():
        texte = sf.record(f.objet_survole())

    f.mise_a_jour()
