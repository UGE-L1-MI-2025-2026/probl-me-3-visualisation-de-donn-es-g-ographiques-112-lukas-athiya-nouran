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




def main(f_depar, f_temp):

    annee = "2018"
    departement = None
    precedent = None
    tmax = 0
    animat = False
    sf = shapefile.Reader(f_depar)
    t_json = temp.carte_exemple(annee, f_temp)
    depart_couleurs = temp.couleur_departement(t_json, sf, tmax)
    fltk.cree_fenetre(L, H)
    l_polygon = affichage.france(L, H, sf)
    affichage.dessiner(l_polygon, depart_couleurs)
    affichage.titre(H,L)

    h_bouton = interaction.bouton_avancer(L, H, TAILLE_TXT_B)
    interaction.bouton_reculer(L, H, TAILLE_TXT_B)
    interaction.bouton_temp(L, H, TAILLE_TXT_B, tmax = tmax)
    affichage.afficher_degrade(couleurs.COULEUR, L, H - h_bouton)
    affichage.afficher_degres(L, H - h_bouton)
    

    while True:

        ev = fltk.donne_ev()
        obj_s = fltk.objet_survole()

        if fltk.type_ev(ev) == "ClicGauche":
                if fltk.est_objet_survole("reculer"):
                    l_polygon, t_json, annee = interaction.reculer(f_temp, sf, l_polygon, annee, tmax)
                    
                elif fltk.est_objet_survole("avancer"):
                    l_polygon, t_json, annee = interaction.avancer(f_temp, sf, l_polygon ,annee, tmax)

                elif fltk.est_objet_survole("temp"):
                    tmax = interaction.bouton_temp(L, H, TAILLE_TXT_B, tmax=tmax)

                elif fltk.est_objet_survole("animation"):
                    animat = not(animat)
                    animat, l_polygon, t_json, annee = interaction.animation(animat, f_temp, sf, 
                                                                     annee, tmax, borne = 2025)
                    
        elif fltk.type_ev(ev) == "Quitte":
            fltk.efface_tout()
            fltk.ferme_fenetre()

        if obj_s:
            tag = fltk.recuperer_tags(obj_s)
            if tag and tag[0].startswith("polygon_"):
                departement = int(tag[0].split("_")[1])
                if departement is not None:
                    x, y = interaction.milieu(l_polygon[departement])
                    interaction.affichage_info(x, y, departement, f"t_{departement}",
                                                sf, t_json, tmax)
                
            if precedent is not None and departement != precedent:
                fltk.efface(f"t_{precedent}")
            precedent = departement
        else:
            if precedent is not None:
                fltk.efface(f"t_{precedent}")
                
        fltk.mise_a_jour()


    
if  __name__ == "__main__":
    fichier_depart = "data/departement_shapefile/departements-20180101.shp"
    fichier_temp = "data/temperature/temperature-quotidienne-departementale.json"


    main(fichier_depart, fichier_temp)