import shapefile
import fltk
import affichage 
import temperature as temp
import interaction
import couleurs
import constante


H = constante.H
L = constante.L

TAILLE_TXT_INFO = constante.TAILLE_TXT_INFO
TAILLE_TXT_B = constante.TAILLE_TXT_B




def main(sf, temps_json):

    fltk.cree_fenetre(L, H)
    depart_couleurs = temp.couleur_departement(couleurs.COULEUR, temps_json, sf)
    liste_points = affichage.france(L, H, sf)
    affichage.dessiner(liste_points, depart_couleurs)
    departement = None
    precedent = None
    
    affichage.titre(H,L)
    h_bouton = interaction.bouton_avancer(L, H, TAILLE_TXT_B)
    interaction.bouton_reculer(L, H, TAILLE_TXT_B)
    affichage.afficher_degrade(couleurs.COULEUR, L, H - h_bouton)
    affichage.afficher_degres(L, H - h_bouton)
    


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
                    interaction.affichageinfoavancé(H,L,departement, f"t_{departement}", sf, temps_json)
                
            if precedent is not None and departement != precedent:
                fltk.efface(f"t_{precedent}")
            precedent = departement
        else:
            if precedent is not None:
                fltk.efface(f"t_{precedent}")
                
        fltk.mise_a_jour()


    
if  __name__ == "__main__":
    sf = shapefile.Reader("data/departement_shapefile/departements-20180101.shp")
    temps_json = temp.carte_exemple("data/temperature/temperature-quotidienne-departementale.json")
    
    main(sf, temps_json)