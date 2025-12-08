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
            depa_couleurs.append(temp_to_couleur(temp, couleurs))
        else:
            depa_couleurs.append("#CCCCCC")
    return depa_couleurs

def moyenne_departement_annee(annee):
    temp_dep = {}
    with open("data/temperature/temperature-quotidienne-departementale.json", "r") as file:
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


moyenne_2018 = moyenne_departement_annee("2018")
moyenne_2019 = moyenne_departement_annee("2019")
moyenne_2020 = moyenne_departement_annee("2020")
moyenne_2021 = moyenne_departement_annee("2021")
moyenne_2022 = moyenne_departement_annee("2022")
moyenne_2023 = moyenne_departement_annee("2023")
moyenne_2024 = moyenne_departement_annee("2024")
moyenne_2025 = moyenne_departement_annee("2025")


# la meme carte que l'exemple, date : 01/07/2018
def carte_exemple():
    temps_json = {}
    with open("data/temperature/temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2018" and dep["date_obs"][5:7] == "07" and dep["date_obs"][8:10] == "01":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2018 : ", temps_json)
    return temps_json


#carte_exemple()

def temp_annee(annee):
    temps_json = {}
    with open("data/temperature/temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == annee:
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    return temps_json

annee2018 = temp_annee("2018")
annee2019 = temp_annee("2019")
annee2020 = temp_annee("2020")
annee2021 = temp_annee("2021")
annee2022 = temp_annee("2022")
annee2023 = temp_annee("2023")
annee2024 = temp_annee("2024")
annee2025 = temp_annee("2025")