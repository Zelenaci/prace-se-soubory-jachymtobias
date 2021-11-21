#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum:
# Autor:
############################################################################
from random import randint, choice

############################################################################


def menu():
    try:
        prvni_soubor = input("První soubor: ")
        druhy_soubor = input("Druhý soubor: ")
        file1 = open(prvni_soubor, "r")
        file2 = open(druhy_soubor, "w")
    except FileNotFoundError:
        print("soubor neexistuje")

    while True:
        print("""
        1 - Převeď soubor na malá písmena.
        2 - Náhodný text.
        """)
        volba = input("Chci číslo: ")
        if volba == "1":
            prevod_pismen(file1, file2)

        elif volba == "2":
            maxwords = int(input("Zadej počet slov: "))
            while maxwords < 1:
                print("Neplatné")
                maxwords = int(input("Zadej počet slov: "))
            print(gen_vet(maxwords))


def prevod_pismen(file1, file2):
    text = file1.read().lower()
    file2.write(text)

    file1.close()
    file2.close()
pocet={}



samohlasky = "aeiyou"
souhlasky = "qwrtpsdfghjklzxcvbnm"

def gen_slov(minchars=2, maxchars=10):
    vysledek = ""
    samohlasky = "aeiyou"
    souhlasky = "qwrtpsdfghjklzxcvbnm"
    pocet = randint(minchars, maxchars)
    zacatek = randint(0, 1)
    for i in range(pocet):
        if i % 2 == zacatek:
            vysledek = vysledek + choice(souhlasky)
        else:
            vysledek = vysledek + choice(samohlasky)
            if randint(1, 10) == 1:
                vysledek = vysledek + choice(souhlasky)
    return vysledek

def gen_vet(maxwords):
    vysledek = ""
    for i in range(maxwords):
        vysledek = vysledek + gen_slov() + " "
    return vysledek.capitalize()[0:-1] + "."

if __name__ == "__main__":
    menu()
