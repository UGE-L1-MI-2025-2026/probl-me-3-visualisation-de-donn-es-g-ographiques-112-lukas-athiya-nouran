import json
import couleurs

def temp_to_couleur(temp, couleurs = couleurs.COULEUR):
    if temp <= -15:
        return couleurs[0]
    elif temp >= 39:
        return couleurs[-1]
    indice = round(temp) + 15
    if indice >= len(couleurs):
        indice = len(couleurs) - 1

    return couleurs[indice]


def couleur_departement(temps_json, sf, tmax: int = 0 ):
    #tmax permet de choisir entre 
    # les temperature minimales (1) et maximales (0)
    depa_couleurs = []

    for i in range(len(sf.shapes())):
        code_shp = sf.record(i).code_insee
        code_sans_lettre = code_shp[:2]
        if code_sans_lettre in temps_json:
            temp = temps_json[code_sans_lettre][tmax]
            depa_couleurs.append(temp_to_couleur(temp))
        else:
            depa_couleurs.append("#CCCCCC")
    return depa_couleurs


# la meme carte que l'exemple, date : 01/07/2018
def carte_exemple(annee, path: str):
    temps_json = {}
    with open(path , "r") as file:
        donnee = json.load(file)

    for mesure in donnee:
       if mesure["date_obs"][:4] == annee:
           code = mesure["code_insee_departement"]

           if code not in temps_json:
               temps_json[code] = mesure["tmax"], mesure["tmin"]
           else:
               if mesure["tmax"] is not None and temps_json[code][0] < mesure["tmax"]:
                   temps_json[code] = (mesure["tmax"], temps_json[code][1])

               if mesure["tmin"] is not None and temps_json[code][1] > mesure["tmin"]:
                   temps_json[code] = (temps_json[code][0], mesure["tmin"])
        
    return temps_json


def borne_annee(path):
    """
    Trouve et renvoit les bornes de temperature du fichier
    """
    with open(path, "r") as f:
        donnee = json.load(f)
    max = float("-inf")
    min = float("+inf")
    for dep in donnee:

        if int(dep["date_obs"][:4]) > max:
            max = int(dep["date_obs"][:4])

        if int(dep["date_obs"][:4]) < min:
            min = int(dep["date_obs"][:4])
    return int(min), int(max)
