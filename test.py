import shapefile
import json

sf = shapefile.Reader("data\departement_shapefile\departements-20180101.shp") #ouverture du fichier shapefile

"""
def annee_j():
    code_json = []
    temps_json = {}
    date_lst = []
    departement_lst = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
        code = dep["code_insee_departement"]
        temp = dep["tmax"]

        temps_json[code] = temp
        code_json.append(code)

        date = dep["date_obs"]#[:4]
        date_lst.append(date)

        departement_lst[date] = dep["departement"]

    print(departement_lst)

    print("{departement : temperature} -> ", temps_json)
    code_json = list(set(code_json))
    code_json.sort()
    print("code_insee_json : ", code_json)

annee_j() """

def moyenne_departement_annee(annee):
    temp_dep = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
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
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2018" and dep["date_obs"][5:7] == "07" and dep["date_obs"][8:10] == "01":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2018 : ", temps_json)
    return temps_json

carte_exemple()

def annee_2018():
    temps_json = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2018":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2018 : ", temps_json)
    return temps_json
annee_2018()

def annee_2019():
    temps_json = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2019":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2019 : ", temps_json)
    return temps_json
annee_2019()

def annee_2020():
    temps_json = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2020":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2020 : ", temps_json)
    return temps_json
annee_2020()

def annee_2021():
    temps_json = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2021":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2021 : ", temps_json)
    return temps_json
annee_2021()

def annee_2022():
    temps_json = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2022":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2022 : ", temps_json)
    return temps_json
annee_2022()

def annee_2023():
    temps_json = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2023":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2023 : ", temps_json)
    return temps_json
annee_2023()

def annee_2024():
    temps_json = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2024":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2024 : ", temps_json)
    return temps_json
annee_2024()

def annee_2025():
    temps_json = {}
    with open("temperature-quotidienne-departementale.json", "r") as file:
        donnee = json.load(file)
    for dep in donnee:
       if dep["date_obs"][:4] == "2025":
           code = dep["code_insee_departement"]
           temp = dep["tmax"]

           temps_json[code] = temp
        
    #print("ANNEE 2025 : ", temps_json)
    return temps_json
annee_2025()

