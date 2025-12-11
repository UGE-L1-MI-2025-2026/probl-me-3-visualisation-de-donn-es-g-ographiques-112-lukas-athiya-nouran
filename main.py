import shapefile
import fltk
import affichage 
import temperature as temp
import interaction
import couleurs
import constante
import time
import map2

H = constante.H
L = constante.L

TAILLE_TXT_INFO = constante.TAILLE_TXT_INFO
TAILLE_TXT_B = constante.TAILLE_TXT_B




def main(f_depar, f_temp):

    borne = temp.borne_annee(f_temp)
    annee = str(borne[0])
    departement = None
    precedent = None
    tmax = 0
    animat = False

    sf = shapefile.Reader(f_depar)
    t_json = temp.carte_exemple(annee, f_temp)
    fltk.cree_fenetre(L, H)


    depart_couleurs = temp.couleur_departement(t_json, sf, tmax)
    l_polygon = affichage.france(L, H, sf)
    affichage.dessiner(l_polygon, depart_couleurs)
    affichage.titre(H,L)

    h_bouton = interaction.bouton_avancer(L, H, TAILLE_TXT_B)
    interaction.bouton_reculer(L, H, TAILLE_TXT_B)
    interaction.bouton_animation(L, H, TAILLE_TXT_B, animat)
    interaction.change_temp(L, H, TAILLE_TXT_B, tmax = tmax)
    affichage.afficher_degrade(couleurs.COULEUR, L, H - h_bouton-10)
    affichage.afficher_degres(L, H - h_bouton-10)
    affichage.datedynamique(H,L,annee) 

    while True:

        ev = fltk.donne_ev()
        obj_s = fltk.objet_survole()
        if fltk.type_ev(ev) == "ClicGauche":
                
                if fltk.est_objet_survole("reculer"):
                    result = interaction.reculer(f_temp, sf, annee, tmax, borne[0])
                    if len(result)==3:
                        l_polygon, t_json, annee = result
                    else:
                        annee = result
                    affichage.datedynamique(H,L,annee)
                elif fltk.est_objet_survole("avancer"):
                    result = interaction.avancer(f_temp, sf, annee, tmax, borne[1])
                    if len(result)==3:
                        l_polygon, t_json, annee = result
                    else:
                        annee = result
                    affichage.datedynamique(H,L,annee)
                elif fltk.est_objet_survole("temp"):
                    tmax = interaction.change_temp(L, H, TAILLE_TXT_B, tmax=tmax)
                    depart_couleurs = temp.couleur_departement(t_json, sf, tmax)
                    affichage.dessiner(l_polygon, depart_couleurs)
                    
                elif fltk.est_objet_survole("animation"):
                    animat = not(animat)
                    interaction.bouton_animation(L, H, TAILLE_TXT_B, animat)
                    
                    
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
        
        if animat:
            
            result = interaction.avancer(f_temp, sf, annee, tmax)
            l_polygon, t_json, annee = result
            annee = borne[0] + (int(annee) - borne[0]) % (borne[1] - borne[0])
            affichage.datedynamique(H,L,annee)
            # ajouter la date
            fltk.mise_a_jour()
            time.sleep(1)
            

        fltk.mise_a_jour()


    
if  __name__ == "__main__":
    fichier_depart = "data/departement_shapefile/departements-20180101.shp"
    fichier_temp = "data/temperature/temperature-quotidienne-departementale.json"

    affichage.menu()

    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
    
        if tev == "ClicGauche":
            if fltk.est_objet_survole("france"):
                fltk.ferme_fenetre()
                main(fichier_depart, fichier_temp)
            elif fltk.est_objet_survole("bonus"):
                fltk.ferme_fenetre()
                map2.bonus()
            else:
                pass

        elif tev == 'Quitte': 
            break

        else: 
            pass
        fltk.mise_a_jour()
    fltk.ferme_fenetre()


