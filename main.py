import shapefile
import fltk
import affichage 
import temperature as temp
import interaction
import couleurs


H = 1200
L = 1600
TAILLE_TXT_INFO = 20
TAILLE_TXT_B = 15



def main():
    sf = shapefile.Reader("data/departement_shapefile/departements-20180101.shp")
    temps_json = temp.carte_exemple()

    fltk.cree_fenetre(L, H)
    depart_couleurs = temp.couleur_departement(couleurs.COULEUR, temps_json, sf)
    liste_points = affichage.france(L, H, sf)
    affichage.dessiner(liste_points, depart_couleurs)
    departement = None
    precedent = None
    
    fltk.ligne(L-20, 0, L-20, 800)
    affichage.afficher_degrade(couleurs.COULEUR, L)
    affichage.afficher_degres(L)


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
    fltk.texte(x1 + 3, y1 - 2, chaine = "reculer", ancrage = "nw", taille = TAILLE_TXT_B)

    

    while True:

        ev = fltk.donne_ev()
        obj_s = fltk.objet_survole()

        if fltk.type_ev(ev) == "ClicGauche":
                if fltk.est_objet_survole("reculer"):
                    interaction.reculer()
                    
                elif fltk.est_objet_survole("avancer"):
                    interaction.avancer()

        elif fltk.type_ev(ev) == "Quitte":
            fltk.efface_tout()
            fltk.ferme_fenetre()

        if obj_s:
            tag = fltk.recuperer_tags(obj_s)
            if tag and tag[0].startswith("polygon_"):
                departement = int(tag[0].split("_")[1])
                if departement is not None:
                    x, y = interaction.milieu(liste_points[departement])
                    interaction.affichage_info(x, y, departement, f"t_{departement}", sf, temps_json)
                
            if precedent is not None and departement != precedent:
                fltk.efface(f"t_{precedent}")
            precedent = departement
        else:
            if precedent is not None:
                fltk.efface(f"t_{precedent}")
                
        fltk.mise_a_jour()


    
if  __name__ == "__main__":
    main()