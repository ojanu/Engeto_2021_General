""" Lekce #2 - Uvod do programovani, 2/2 Destinatio """

SEZNAM_MEST = ("Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava")
SEZNAM_CEN = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

print(ODDELOVAC)
print("Vitejte u nasi aplikace Destinatio!")
print(ODDELOVAC)
print(
    """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
)

print(ODDELOVAC)

# I. KROK:
# Update/doplnit zadani
SLEVY = ("Olomouc", "Ostrava")

# II. KROK:
# Spravne cislo lokality! 1 < x < 6
por_cislo = int(input("Vyberte cislo lokality: "))

if por_cislo < 1 or por_cislo > 6:
    print("Vami vybrane cislo neni v nabidce, ukoncuji")
    exit()
else:
    destinace = SEZNAM_MEST[por_cislo - 1]
    cena = SEZNAM_CEN[por_cislo - 1]
    print(f"DESTINACE: {destinace}")
    print(ODDELOVAC)

# III. KROK:
# Vyresime pouziti slevy --> ANO/NE
if destinace in SLEVY:
    cena_po_sleve = 0.75 * cena
else:
    cena_po_sleve = cena

# IV. KROK:
# jmeno + prijmeni obsahuje jen pismena
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")

if jmeno.isalpha() and prijmeni.isalpha():
    print(f"JMENO: {jmeno}, PRIJMENI: {prijmeni}")
    print(ODDELOVAC)
else:
    print("Jmeno a prijmeni musi obsahovat pouze pismena, ukoncuji")
    exit()

# V. KROK:
# aktualni rok - datum narozeni --> > 18
AKT_ROK = 2020
vek = int(input("ROK NAROZENI: "))

if (AKT_ROK - vek) >= 18:
    print(f"Pokracuji...")
    print(ODDELOVAC)
else:
    print("Nase sluzby mohou vyuzivat pouze osoby starsi 18 let, ukoncuji")
    exit()

# VI. KROK:
# Spravny email
email = input("EMAIL: ")
if "@" in email:
    print("Email v poradku, pokracuji...")
    print(ODDELOVAC)
else:
    print("Nepodporovany format emailu, ukoncuji")
    exit()

# VII. KROK:
# Heslo obsahuje jak cisla, tak pismena + delka?
heslo = input("HESLO: ")

if len(heslo) >= 8 and not heslo.isalpha() and not heslo.isnumeric():
    print("Heslo v poradku")
    print(ODDELOVAC)
    print("UZIVATEL: " + jmeno)
    print("DESTINACE: " + destinace)
    print("CENA(cil:" + destinace + "): " + str(cena_po_sleve))
    print(f"Jizdenku posleme na Vasi emailovou adresu: {email}")
else:
    print(
        """
            Tvoje heslo je spatne zadane:
            1. Musi obsahovat alespon 8 znaku,
            2. Musi obsahovat pismena,
            3. Musi obsahovat cislice
        """
    )

# Zmena
