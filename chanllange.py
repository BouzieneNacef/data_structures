
# proba
def calcul(n):
    if n <2 or n>365:
        return "le nombre doit entre 2 et 365"
    proba = 1.0
    for i in range(1,n):
        proba*=(365 - i)/365
        probabiliter =1-proba
        return probabiliter
    nombre_eleve= int(input("entret nb eleve"))
    proba_anni=calcul(nombre_eleve)
    print("la proba ",nombre_eleve, "les eleve aient leur anniversaire",proba_anni )

calcul(32)
