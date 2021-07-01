# Pozdrav klienta
print('=' * 100)
print('''Welcome to the DESTINATIO,
place where people plan their trips''')
print('=' * 100)

# Nabídni mu destinaci
print('We can offer you the following destinations:')
print('-' * 100)
print('''
1 - Prague | 1000
2 - Wien | 1100
3 - Brno | 2000
4 - Svitavy | 1500
5 - Zlin | 2300
6 - Ostrava | 3400
''')
print('-' * 100)

# Získej vstup uživatele o destinaci
selection = int(input('Please enter the destination number to select: '))
selection_index = selection - 1

# Přiřaď proměnným příslušná data
DESTINATIONS = ['Prague', 'Wien', 'Brno', 'Svitavy', 'Zlin', 'Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]
DISCOUNT_25 = ['Svitavy', 'Ostrava']

# Zkontroluj, zde byl vložen vhodný vstup
if selection > 0 and selection < 7:
    print(f"The select is {DESTINATIONS[selection_index]} and is correct, continue...")
else:
    print("The select is NOT correct, ending...")
    exit()

# Získej data z proměnných podle vstupu uživatele
destination = DESTINATIONS[selection_index]
price = PRICES[selection_index]

# Spočítej cenu a zkontroluj, zda je vhodný aplikovat slevu pro zvolenou destinaci
if destination in DISCOUNT_25:
    price = int(price * 0.75)
    print(f"Lucky you! You have just earned 25% discount for your destination - {destination}. The price is {price}")
    input('Press enter to continue')

else:
    print("You have no discount for your destination")

# Začni registraci
print('=' * 100)
print("REGISTRATION:")
print('-' * 100)
print("In order to complete your reservations, please share few details about yourself with us.")
print('-' * 100)
# Získej vstup uživatele o jeho osobních datech
name = input('NAME: ')
print('=' * 40)
surname = input('SURNAME: ')
print('=' * 40)
birth_year = int(input('YEAR of BIRTH: '))
print('=' * 40)
email = input('EMAIL: ')
print('=' * 40)
password = input('PASSWORD (min. 8 char.): ')
print('=' * 100)

# Zkotroluj, jestli je uživatel starší než 15 let
CURRENT_YEAR = 2021
age = CURRENT_YEAR - birth_year
if age >= 15:
    print(f"You are {age} old and you can order the ticket, continue...")
else:
    print(f"You are {age} old and you can NOT order the ticket, ending...")
    exit()

# Zkontroluj, jestli email obsahuje zavináč - @
if "@" not in email:
    print("The email must contain @, ending...")
    exit()

# Zkontroluj, jestli heslo
# - má aspoň 8 znaků
if len(password) < 8:
    print("Password must have min. 8 characters, ending..")
    exit()

# Poděkuj uživateli použitím jeho jména a informuj jej/jí o provedení rezervace
print(f"Thank you {name}")
print(f"We have made your reservation to {destination}")
print(f"The total price is {price}")
