# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:16:26 2022

@author: SAMIR
"""

import math
import ipaddress 

def identite():
    nom = input("Veuillez introduire votre nom: ")
    prenom = input("Veuillez entroduire votre prénom: ")
    
    print("Vous êtes Mr/Mme {} {}".format(nom,prenom))
    

##### FONCTION QUI DEFINIT L'AGE #####
def age():
    '''
    FONTION AGE
    '''
    while True:
        try:
            age = int(input("Veuillez introduire votre age: "))
            break
        except ValueError:
            print("Veuillez introduire un entier SVP!!")
        
    
    print("Vous aurez 100 ans en  {}".format(2022-age+100))

##### FONCTION QUI DEFINIT LE CONE #####
def cone():
    '''
    FONTION CONE
    '''
    while True:
        try:
            rayon = float(input("introduire le rayon: "))
            hauteur = float(input("Introduire la hauteur: "))
            break
        except ValueError:
            print("Impossible de saisir une chaine de caractère. Réessayez")
            
    volume = math.pi * (rayon**2) * (hauteur/3)
    print("Le volume du cône droit est: ", volume)

##### FONCTION QUI DEFINIT SI PAIR OU IMPAIR #####
def ispair():
    
    while True:
        try: 
            nombre = int(input("Introduire votre nombre: "))
            break
        except:
            print("Veuillez introduire un entier SVP!!")
        
    if nombre%2 == 0:
        print("Votre nombre est pair")
    else:
        print("votre nombre est impair")
        
        
def fibonacci():
    n = int(input("Introduire le rang: "))
    fibo = [0]*(n)
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2,n):
        fibo[i] = fibo[i-1] + fibo[i-2]

    print(fibo)
    

def pgcd_ppcm():
    nombre_1 = int(input("Introduire le nombre 1: "))
    nombre_2 = int(input("Introduire le nombre 2: "))
    print("Le ppcm de {} et {} est: {}".format(nombre_1, nombre_2, math.lcm(nombre_1, nombre_2)))
    print("Le pgcd de {} et {} est: {}".format(nombre_1, nombre_2, math.gcd(nombre_1, nombre_2))) 


def element_communs(liste1, liste2):
    liste_finale = []
    
    for i in liste1:
        for j in liste2:
            if i == j:
                if i not in liste_finale:
                    liste_finale.append(i)
                
    return liste_finale


def Palindrome():
    mot = input("Ecrire votre mot: ")
    if str(mot) == str(mot)[::-1] :
        print("La chaine de caractère saisie est un palyndrome")
    else:
        print("La chaine de caractère saisie n'est pas un palyndrome")
    

def doublon(liste):
    resultaListe = []
    for element in liste:
        if element not in liste:
            resultaListe.append(element)

    return resultaListe



def isadressIP(adresse):
    if ipaddress.ip_address(adresse) in ipaddress.ip_network('192.168.0.0/24'):
        print("C'est une bonne adresse IP")
        

