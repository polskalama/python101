# ! /usr/bin/env python3
# -*- coding: utf-8 -*-
import time

# deklarujemy i inicjalizujemy zmienne
current_year = time.localtime()
aktRok = int(time.strftime('%Y', current_year))
print(aktRok)
pythonRok = 1989
# obliczamy wiek Pythona
wiekPythona = aktRok - pythonRok

# pobieramy dane
imie = input('Jak się nazywasz? ')
wiek = int(input('Ile masz lat? '))

# wyświetlamy komunikaty
print("Witaj", imie)
print("Mów mi Python, mam", wiekPythona, "lat.")

# instrukcja warunkowa
if wiek > wiekPythona:
    print('Jesteś starszy ode mnie.')
else:
    print('Jesteś młodszy ode mnie.')
