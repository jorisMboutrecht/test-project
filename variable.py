producten = [
    ["ps5", 500],
    ["xbox", 400],
    ["pc", 2000]
]

aantal_producten_verkocht = [
    ["ps5", 10],
    ["xbox", 2],
    ["pc", 20]
]

totaal_omzet = 0



for p in producten:
    for a in aantal_producten_verkocht:
        if p[0] == a[0]:
            print(f"{p[0]} worden verkocht voor €{p[1]} en er zijn {a[1]} verkocht")
            totaal_omzet += p[1]*a[1]
print(f"totale omzet: €{totaal_omzet}")