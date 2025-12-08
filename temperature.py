import json


def temp_to_couleur(temp, couleurs):
    if temp <= 0:
        return couleurs[0]
    elif temp >= 39:
        return couleurs[-1]
    indice = round(temp)
    return couleurs[indice]


def couleur_departement(couleurs, temps_json, sf):
    depa_couleurs = []

    for i in range(len(sf.shapes())):
        code_shp = sf.record(i)[0]
        code_sans_lettre = code_shp[:2]
        if code_sans_lettre in temps_json:
            temp = temps_json[code_sans_lettre]
            depa_couleurs.append(temp_to_couleur(temp, couleurs)) # a changer ya tmin et tmax mtn
        else:
            depa_couleurs.append("#CCCCCC")
    return depa_couleurs



def moyenne_departement_annee(annee, path):
    temp_dep = {}

    with open(path, "r") as file:
        donnee = json.load(file)

    for dep in donnee:
        if dep["date_obs"][:4] == annee:
            code = dep["code_insee_departement"]
            temp = dep["tmax"]

            if temp is None:
                continue
            if code not in temp_dep:
                temp_dep[code] = []

            temp_dep[code].append(temp)
    
    moyennes = {}
    for code in temp_dep:
        liste_temps = temp_dep[code]
        moyennes[code] = sum(liste_temps) / len(liste_temps)
    return moyennes


def moyenne_dep_annees():
    m_t_2018_2025 = []
    path = "data/temperature/temperature-quotidienne-departementale.json"

    for i in range (18, 26):
        m_t_2018_2025.append(moyenne_departement_annee(f"20{i}", path))

    return m_t_2018_2025


# la meme carte que l'exemple, date : 01/07/2018
def carte_exemple(path: str):
    temps_json = {}
    with open(path , "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2018" and dep["date_obs"][5:7] == "07" and dep["date_obs"][8:10] == "01":
           code = dep["code_insee_departement"]
           temp = dep["tmax"], dep["tmin"]
           

           temps_json[code] = temp
        
    #print("ANNEE 2018 : ", temps_json)
    return temps_json


#carte_exemple()

def temp_annee(annee, path):
    temps_json = {}
    with open(path, "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == annee:
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    return temps_json

def temps_annees():

    t_2018_2025 = []
    path = "data/temperature/temperature-quotidienne-departementale.json"

    for i in range (18, 26):
        t_2018_2025.append(temp_annee(f"20{i}", path))
    
    return t_2018_2025