#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:31:17 2020

@author: lordof20th
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:59:25 2019

@authors: Julien Morelle & Louis Lacoste
"""
from random import randint

# Initialisation, Endphase et Banqueroute
def initialisation(n, strat): # Création de la liste des joueurs, et le dictionnaire de leurs caractéristiques
    LJ=[]
    for i in range(n+1):
        if i == n:
            LJ.append("Croupier")
        else:
            LJ.append("Joueur "+str(i))
    J = {}
    for i in LJ:
        if i == 'Croupier':
            J[i] = [0, stratCroupier, [], 0, 200]  # [mise, stratégie, main, valeur main, capital]    
        else:
            J[i] = [0, strat, [], 0, 200]  # [mise, stratégie, main, valeur main, capital]
    return LJ,J


def endphase(LJ, J):
    vmain_croupier = J["Croupier"][3]
    for i in LJ:
        #print(" End Phase : "+str(LJ))
        infosJoueurs = J[i]
        # On récupère les valeurs
        capital = infosJoueurs[4]
        mise = infosJoueurs[0]
        main = infosJoueurs[2]
        vmain = infosJoueurs[3]

        if i == "Croupier":
            capital = 200
        else:
            if vmain == 21 and len(main) == 2:
                capital += int(3 * mise)
            elif vmain_croupier > 21:
                if vmain <= 21:
                    capital += 2*mise
                else:
                    capital += mise
            elif vmain_croupier <= 21:
                if vmain_croupier==vmain:
                    capital += mise
                elif (vmain<vmain_croupier and vmain<=21):
                    capital+= 2*mise

        # On vide main et mise
        main = []
        mise = 0
        vmain = valeurMain(main)

        # On set toutes les valeurs modifiées
        infosJoueurs[4] = capital
        infosJoueurs[0] = mise
        infosJoueurs[2] = main
        infosJoueurs[3] = vmain

def testBanqueroute(LJ, J):
    print("Voici la liste des Joueurs : " +str(LJ))
    for i in LJ:
        if i != "Croupier":
            print("On teste si le joueur " + i + " fait banqueroute")
            infosJoueurs = J[i]
            # On récupère les valeurs
            capital = infosJoueurs[4]
            if capital <= 2:  # Si on a moins de 2 jetons alors on ne mise plus
                del J[i]  # On retire le joueur de la partie
                print(LJ[LJ.index(i)] + " ne peut plus jouer, il quitte la table !")
                del LJ[LJ.index(i)]  # On retire le nom du joueur de la partie


def bankruptTest2(nom, J, LJ):
    if J[nom][4] == 2 or J[nom][4] == 1 or J[nom][4] == 0:
        # Le joueur ne peut plus jouer, il faut le retirer des listes
        del J[nom]  # On supprime ses données
        LJ.remove(nom)  # On le retire de la liste des joueurs


#Mélange
def melange(n):
    """ Fonction générant un mélange de plusieurs paquets de cartes
    sous la forme d'une liste """
    P = n*52*[0]
    conv = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']
    dic = {'AH': n, '2H': n, '3H': n, '4H': n, '5H': n, '6H': n, '7H': n, '8H': n, '9H': n, '10H': n, 'JH': n, 'QH': n, 'KH': n, 'AS': n, '2S': n, '3S': n, '4S': n, '5S': n, '6S': n, '7S': n, '8S': n, '9S': n, '10S': n, 'JS': n, 'QS': n, 'KS': n, 'AD': n, '2D': n, '3D': n, '4D': n, '5D': n, '6D': n, '7D': n, '8D': n, '9D': n, '10D': n, 'JD': n, 'QD': n, 'KD': n, 'AC': n, '2C': n, '3C': n, '4C': n, '5C': n, '6C': n, '7C': n, '8C': n, '9C': n, '10C': n, 'JC': n, 'QC': n, 'KC': n}
    for i in range((n*52)):         # on affecte à chaque valeur de la liste P un nom de carte
        while P[i] == 0:            # tant que le iéme terme de la liste n'a pas de nom on va continuer a essayer de lui en trouver                                             une disponible
            r = randint(0, 51)      # on tire aléatoirement une carte parmis les 52 d'un paquet
            if dic[conv[r]] != 0:   # si la carte est encore disponible dans le paquet, on la place dans la liste
                P[i] = conv[r]
                dic[conv[r]] -= 1   # dic[conv[r]] = dic[conv[r]] -1 (on diminue de 1 la valeur de l'index de la carte tirée (une carte de moins est disponible)
    return P

# Distribution
def testJouable(LJ, J, P):
    if len(P) > 52 and len(LJ) >= 2:  # verif qu'on peut jouer
        return True
    else:
        return False

def distrib(LJ,J,P,n):  # LJ : Liste du nom index des joueurs | J : dictionnaire avec en index les { noms index des joueurs : [Main du joueur] }
        for c in range(n):
            for i in LJ:
                J[i][2].append(P.pop()) # On ajoute une carte dans la liste de carte du joueur i


def tirerUneCarte(P):
    return P.pop()


def valeurMain(main):
    S = 0
    count = 0
    for i in main:
        if i[0] == 'K' or i[0] == 'Q' or i[0] == 'J' or i[0] == '1':
            S += 10
        elif i[0] == 'A':
            S += 11
            count += 1
        else:
            S += int(i[0])
    while S > 21 and count > 0:
        S -= 10
        count -= 1
    return S


# Stratégies
def stratAlea(phase, infosJoueurs, P, valUpCard):
    # avec phase qui correspond à la phase de jeu
    """ mise entre 2 et 100 euros aléatoirement
    Soit il tire | soit il double
    Si il tire, il a une chance sur deux d'arrêter de tirer """
    # On récupère les valeurs
    capital = infosJoueurs[4]
    mise = infosJoueurs[0]
    main = infosJoueurs[2]

    if phase == 1:  # Mise de départ
        mise = randint(2, capital)
        capital -= mise
    elif phase == 2:
        if capital >= mise:
            choix = randint(1, 3)
            if choix == 1:  # Double
                main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                capital -= mise
                mise = 2*mise
            elif choix == 2: # Hit
                rejouer = True
                while valeurMain(main) < 21 and rejouer:
                    if randint(1, 2) == 1:
                        rejouer = True
                    main.append(tirerUneCarte(P)) # On ajoute une carte à la main

        else: # On ne peut pas doubler
            choix = randint(2, 3)
            if choix == 2: # Hit
                    rejouer = True
                    while valeurMain(main) < 21 and rejouer:
                        if randint(1, 2) == 1:
                            rejouer = True
                        main.append(tirerUneCarte(P)) # On ajoute une carte à la main

    # On attribue les nouvelles valeurs
    infosJoueurs[2] = main
    infosJoueurs[0] = mise
    infosJoueurs[4] = capital
    infosJoueurs[3] = valeurMain(main)

def stratBasique(phase, infosJoueurs, P, valUpCard):
    # avec phase qui correspond à la phase de jeu
    # On récupère les valeurs dont la carte du croupier (cartecroup)
    cartecroup= valUpCard
    capital = infosJoueurs[4]
    mise = infosJoueurs[0]
    main = infosJoueurs[2]

    if phase == 1:  # Mise de départ
        mise = capital//20
        capital -= mise
    elif phase == 2:
        jouer = True
        while jouer == True :
            if valeurMain(main) <=8 or (valeurMain(main) == 9 and (cartecroup>=7 or cartecroup==2)) or (valeurMain(main)==10 and cartecroup>=10) or (valeurMain(main)== 12 and (cartecroup==2 or cartecroup==3)) or ((valeurMain(main)>= 12 and valeurMain(main)<=16) and cartecroup>=7):
                main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                # il va hit
            elif valeurMain(main) >= 17 or ((valeurMain(main)>= 13 and valeurMain(main) <= 16) and cartecroup <=6) or (valeurMain(main) == 12 and (cartecroup>=4 and cartecroup <=6)):
                jouer = False
                # il va stand
            else:
                main.append(tirerUneCarte(P)) # On ajoute une carte à la main
                capital -= mise
                mise = 2*mise
                jouer= False
                # il va double

    # On attribue les nouvelles valeurs
    infosJoueurs[2] = main
    infosJoueurs[0] = mise
    infosJoueurs[4] = capital
    infosJoueurs[3] = valeurMain(main)

def principale(nbreJoueurs, nbrePCartes, stratChoisie):
    tour = 0
    listeJoueurs, infoJoueurs = initialisation(nbreJoueurs, stratChoisie)
    P = melange(nbrePCartes)
    upCardCroupier = []
    while testJouable(listeJoueurs, infoJoueurs, P):
        tour += 1
        phase = 0
        """ Première phase de mise """
        phase = 1
        for i in listeJoueurs:
            strat = infoJoueurs[i][1]
            strat(phase, infoJoueurs[i], P, 0)

        """ Distribution des mains """
        distrib(listeJoueurs, infoJoueurs, P, 2)
        upCardCroupier.append(infoJoueurs["Croupier"][2][1])
        valUpCard = valeurMain(upCardCroupier)
        """ Deuxième phase de mise """
        phase = 2
        for i in listeJoueurs:
            strat = infoJoueurs[i][1]
            strat(phase, infoJoueurs[i], P, valUpCard)
        endphase(listeJoueurs, infoJoueurs)
        for i in listeJoueurs:
            bankruptTest2(i, infoJoueurs, listeJoueurs)
        for i in listeJoueurs:
            bankruptTest2(i, infoJoueurs, listeJoueurs)
        upCardCroupier = []
    return tour


def test(N):
    n=0
    for i in range(1,N+1):
        if i % 1000 == 0:
            print("Essai n°" + str(i))
        try:
            principale(2,10,stratBasique)
        except:
            n+=1
    return str(n/N*100) + " % d'erreurs"


def test2(N):
    s=0
    for i in range(N):
        s+=principale(1, 100, stratBasique)
    s=s/N
    return s


def test3(N):
    s=0
    for i in range(N):
        s+=principale(1, 100, stratAlea)
    s=s/N
    return s


def testc(N):
    return (test2(N),test3(N))