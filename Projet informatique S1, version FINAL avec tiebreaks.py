##########################################################################################
#  Auteurs : Léo Lemaire, Nirojan Salvanathan, Maé Bretin                   Janvier 2025 #
#                                                                                        #
#                                    Jeu de Rolit                                        #
##########################################################################################

#-------------Imports--------------
import fltk
import json

#-------------Constantes-----------
LARG = 1340 #Largeur de la fenêtre
HAUT = 755 #Hauteur de la fenêtre
TAILLE = 8 #Nombre de lignes et de colonnes de la grille
TAILLE_CEL = 80 #Taille d'une cellule en pixels
X_OFFSET = 600 # décallage gauche - min 30 pour afficher les références
Y_OFFSET = 50 # décallage droite - min 30

#-------------Fonctions------------

#-------Fonctions graphiques-------

def show_grid_with_marks(nb_cel, taille_cel, x_offset, y_offset):
    """
    Affiche une grille carrée avec des marques de repérage.
    :param nb_cel: (int) nombre de colonnes et nombre de cellules par ligne
    :param taille_cel: (int) taille d'une cellule en pixels
    :param x_offset: (int) décalage, en pixels, par rapport au bord gauche de la fenêtre
    :param y_offset: (int) décalage, en pixels, par rapport au bord supérieur de la fenêtre
    :return: None
    """
    liste_lettres = ['A','B','C','D','E','F','G','H']
    x, y = 10, 10 #position du coin
    #----Affichage des légendes
    fltk.ligne(x_offset - 30, y_offset - 30, x_offset, y_offset, couleur = 'black')
    for i in range(nb_cel):
        fltk.texte(x_offset + taille_cel/3 + i * taille_cel, y_offset - 24, i, taille = 16, couleur = 'black')
        fltk.texte(x_offset - 20 , y_offset + taille_cel/3 + i * taille_cel, liste_lettres[i], taille = 16, couleur = 'black')
    for i in range(nb_cel + 1):
        #----Affichage des lignes
        fltk.ligne(x_offset + i*taille_cel, y_offset, x_offset + i*taille_cel, y_offset + nb_cel*taille_cel, couleur = 'grey', epaisseur = 3)
        fltk.ligne(x_offset, y_offset + i*taille_cel, x_offset + nb_cel*taille_cel, y_offset + i*taille_cel, couleur = 'grey', epaisseur = 3)

def pix_vers_cel(x, y, taille, taille_cel, x_offset, y_offset) :
    """
    Calcule les références de la cellule dans laquelle le point (x, y) se situe.
    Les bords Ouest et Nord appartiennent à la cellule.
    """
    col = (x - x_offset)//taille_cel
    li = (y - y_offset)//taille_cel
    return li, col

def centre_pixel(li, col, taille_cel, x_offset, y_offset) :
    """
    Calcule les coordonnées en pixels du centre de la cellule référencée (li, col).
    """
    x = x_offset + (col + 0.5) * taille_cel
    y = y_offset + (li + 0.5) * taille_cel
    return x, y

def actualisation(grille):
    """
    Récupère la grille et affiche les boules correspondandes sur la fenêtre fltk
    """
    
    fltk.efface('cercle')
    xcentre=0
    ycentre=0
    li=-1
    col=-1
    for ligne in grille:
        li+=1
        for elt in ligne:
            col+=1
            xcentre, ycentre = centre_pixel(li, col, TAILLE_CEL, X_OFFSET, Y_OFFSET)
            if elt == "R":
                fltk.cercle(xcentre, ycentre, TAILLE_CEL*0.4, remplissage ='red', epaisseur = 1, tag = 'cercle')
            elif elt == "V":
                fltk.cercle(xcentre, ycentre, TAILLE_CEL*0.4, remplissage ='green', epaisseur = 1, tag = 'cercle')
            elif elt == "J":
                fltk.cercle(xcentre, ycentre, TAILLE_CEL*0.4, remplissage ='yellow', epaisseur = 1, tag = 'cercle')
            elif elt == "B":
                fltk.cercle(xcentre, ycentre, TAILLE_CEL*0.4, remplissage ='blue', epaisseur = 1, tag = 'cercle')
        col = -1
                
def couleur_joueur(joueur):
    if joueur == "R":
        return 'red'
    elif joueur == "J":
        return 'yellow'
    elif joueur == "V":
        return 'green'
    elif joueur == "B":
        return 'blue'
    else:
        return None

def current_player(joueur_actif, liste_noms_joueurs):
    fltk.efface('noms_joueurs_fltk')
    fltk.efface('cercle_actif')
    fltk.cercle(275, 75, TAILLE_CEL*0.45, remplissage =joueur_actif, epaisseur = 1, tag = 'cercle_actif')
    if joueur_actif == 'red':
        fltk.texte(320, 60, f'{liste_noms_joueurs[0]}', couleur = 'black', taille = 23, tag = 'noms_joueurs_fltk')
    if joueur_actif == 'yellow':
        fltk.texte(320, 60, f'{liste_noms_joueurs[2]}', couleur = 'black', taille = 23, tag = 'noms_joueurs_fltk')
    if joueur_actif == 'green':
        fltk.texte(320, 60, f'{liste_noms_joueurs[1]}', couleur = 'black', taille = 23, tag = 'noms_joueurs_fltk')
    if joueur_actif == 'blue':
        fltk.texte(320, 60, f'{liste_noms_joueurs[3]}', couleur = 'black', taille = 23, tag = 'noms_joueurs_fltk')
    
def next_player(joueur_suivant, liste_noms_joueurs):
    fltk.efface('cercle_suivant')
    fltk.cercle(275, 175, TAILLE_CEL*0.45, remplissage =joueur_suivant, epaisseur = 1, tag = 'cercle_suivant')
    if joueur_suivant == 'red':
        fltk.texte(320, 160, f'{liste_noms_joueurs[0]}', couleur = 'black', taille = 23, tag = 'noms_joueurs_fltk')
    if joueur_suivant == 'yellow':
        fltk.texte(320, 160, f'{liste_noms_joueurs[2]}', couleur = 'black', taille = 23, tag = 'noms_joueurs_fltk')
    if joueur_suivant == 'green':
        fltk.texte(320, 160, f'{liste_noms_joueurs[1]}', couleur = 'black', taille = 23, tag = 'noms_joueurs_fltk')
    if joueur_suivant == 'blue':
        fltk.texte(320, 160, f'{liste_noms_joueurs[3]}', couleur = 'black', taille = 23, tag = 'noms_joueurs_fltk')
    
def score_rouge(rouge, grille):
    score=0
    for ligne in grille:
        for elt in ligne:
            if elt == rouge:
                score+=1
    if score>9:
        fltk.texte(60, 512, str(score), couleur = 'white', taille=20, tag = 'score_joueur')   
    else:    
        fltk.texte(68, 512, str(score), couleur = 'white', taille=20, tag = 'score_joueur')
    return score

def score_vert(vert, grille):
    score=0
    for ligne in grille:
        for elt in ligne:
            if elt == vert:
                score+=1
    
    if score>9:
        fltk.texte(160, 512, str(score), couleur = 'white', taille=20, tag = 'score_joueur')
    else:
        fltk.texte(168, 512, str(score), couleur = 'white', taille=20, tag = 'score_joueur')
    return score

def score_jaune(jaune, grille):
    score=0
    for ligne in grille:
        for elt in ligne:
            if elt == jaune:
                score+=1
    if score>9:
        fltk.texte(260, 512, str(score), couleur = 'black', taille=20, tag = 'score_joueur')
    else:
        fltk.texte(268, 512, str(score), couleur = 'black', taille=20, tag = 'score_joueur')
    return score
    
def score_bleu(bleu, grille):
    score=0
    for ligne in grille:
        for elt in ligne:
            if elt == bleu:
                score+=1
    if score>9:
        fltk.texte(360, 512, str(score), couleur = 'white', taille=20, tag = 'score_joueur')
    else:
        fltk.texte(368, 512, str(score), couleur = 'white', taille=20, tag = 'score_joueur')
    return score    


def score_joueurs(liste_joueurs, grille):
    fltk.efface('score_joueur')
    liste_score=[]
    for i in range(len(liste_joueurs)):
        if liste_joueurs[i]=="R":
            liste_score.append(score_rouge(liste_joueurs[i], grille))
        elif liste_joueurs[i]=="V":
            liste_score.append(score_vert(liste_joueurs[i], grille))
        elif liste_joueurs[i]=="J":
            liste_score.append(score_jaune(liste_joueurs[i], grille))
        elif liste_joueurs[i]=="B":
            liste_score.append(score_bleu(liste_joueurs[i], grille))
    return liste_score
    
    
def score_total_rouge(rouge, score_init, grille):
    score=0
    for ligne in grille:
        for elt in ligne:
            if elt == rouge:
                score+=1
    if score>9:
        fltk.texte(60, 662, str(score+score_init), couleur = 'white', taille=20, tag = 'score_total')   
    else:    
        fltk.texte(68, 662, str(score+score_init), couleur = 'white', taille=20, tag = 'score_total')
    return score+score_init

def score_total_vert(vert, score_init, grille):
    score=0
    for ligne in grille:
        for elt in ligne:
            if elt == vert:
                score+=1
    
    if score>9:
        fltk.texte(160, 662, str(score+score_init), couleur = 'white', taille=20, tag = 'score_total')
    else:
        fltk.texte(168, 662, str(score+score_init), couleur = 'white', taille=20, tag = 'score_total')
    return score+score_init

def score_total_jaune(jaune, score_init, grille):
    score=0
    for ligne in grille:
        for elt in ligne:
            if elt == jaune:
                score+=1
    if score>9:
        fltk.texte(260, 662, str(score+score_init), couleur = 'black', taille=20, tag = 'score_total')
    else:
        fltk.texte(268, 662, str(score+score_init), couleur = 'black', taille=20, tag = 'score_total')
    return score+score_init
    
def score_total_bleu(bleu, score_init, grille):
    score=0
    for ligne in grille:
        for elt in ligne:
            if elt == bleu:
                score+=1
    if score>9:
        fltk.texte(360, 662, str(score+score_init), couleur = 'white', taille=20, tag = 'score_total')
    else:
        fltk.texte(368, 662, str(score+score_init), couleur = 'white', taille=20, tag = 'score_total')
    return score+score_init    


def score_total_joueurs(liste_joueurs, liste_score_init, grille):
    fltk.efface('score_total')
    liste_score=[]
    for i in range(len(liste_joueurs)):
        if liste_joueurs[i]=="R":
            liste_score.append(score_total_rouge(liste_joueurs[i], liste_score_init[i], grille))
        elif liste_joueurs[i]=="V":
            liste_score.append(score_total_vert(liste_joueurs[i], liste_score_init[i], grille))
        elif liste_joueurs[i]=="J":
            liste_score.append(score_total_jaune(liste_joueurs[i], liste_score_init[i],  grille))
        elif liste_joueurs[i]=="B":
            liste_score.append(score_total_bleu(liste_joueurs[i], liste_score_init[i], grille))
    return liste_score

def manches_rouge(score):
    fltk.texte(68, 662, str(score), couleur = 'white', taille=20, tag = 'score_manches')

def manches_vert(score):
    fltk.texte(168, 662, str(score), couleur = 'white', taille=20, tag = 'score_manches')

def manches_jaune(score):
    fltk.texte(268, 662, str(score), couleur = 'black', taille=20, tag = 'score_manches')

def manches_bleu(score):
    fltk.texte(368, 662, str(score), couleur = 'white', taille=20, tag = 'score_manches')

def manches_joueurs(rouge, vert, jaune, bleu):
    fltk.efface('score_manches')
    manches_rouge(rouge)
    manches_vert(vert)
    manches_jaune(jaune)
    manches_bleu(bleu)
    
def mettre_nom(noms, cara):
    noms = noms + cara
    fltk.texte (405, 260, noms, couleur = 'black', tag = 'nom')
    return noms

def noms_joueurs():
    fltk.image (670, 377, 'fond_blanc.gif', ancrage = 'center', tag ='noms_joueurs')
    fltk.ligne (400, 300, 940, 300, couleur = 'black', epaisseur = '4', tag = 'noms_joueurs')
    fltk.rectangle (750, 450, 1190, 602, couleur = 'black', remplissage = 'white', epaisseur = 7, tag = 'rectangle_2')
    fltk.rectangle (150, 450, 590, 602, couleur = 'black', remplissage = 'white', epaisseur = 7, tag = 'rectangle_2')
    fltk.texte (895, 510, 'CONFIRMER', couleur = 'black', taille = 20, tag = 'continuer_2')
    fltk.texte (300, 510, 'ANNULER', couleur = 'black', taille = 20, tag = 'continuer_2')
    fltk.texte (150, 100, 'VEUILLEZ ENTREZ VOTRE NOM.', couleur = 'black', taille = 20)
    #fltk.repere(50)
    noms = ''
    shift = False
    while True:
        ev = fltk.attend_ev()
        type_ev = fltk.type_ev(ev)

        # Action dépendant du type d'événement reçu :

        if type_ev == 'Touche':  # on indique la touche pressée
            if fltk.touche(ev) == 'BackSpace':
                fltk.efface('nom')
                length = len(noms)
                length = length - 1
                noms = noms[:length]
                fltk.texte (405, 260, noms, couleur = 'black', tag = 'nom')
            elif fltk.touche(ev) == 'space':
                noms = noms + ' '
            elif fltk.touche(ev) == 'Shift_L':
                shift = not(shift)
            elif fltk.touche(ev) == 'Shift_R':
                shift = not(shift)
            elif fltk.touche(ev) == 'ampersand':
                cara = '&'
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'eacute':
                cara = 'é'
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'quotedbl':
                cara = '"'
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'apostrophe':
                cara = "'"
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'parenleft':
                cara = "("
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'minus':
                cara = "-"
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'egrave':
                cara = "è"
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'underscore':
                cara = "_"
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'ccedilla':
                cara = "ç"
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'agrave':
                cara = "à"
                noms = mettre_nom(noms, cara)
            elif fltk.touche(ev) == 'parenright':
                cara = ")"
                noms = mettre_nom(noms, cara)
            else:
                fltk.efface('nom')
                if shift == True:
                    maj = fltk.touche(ev)
                    maj.upper()
                    noms = mettre_nom(noms, maj)
                if shift == False:
                    noms = mettre_nom(noms, fltk.touche(ev))
                    
        elif type_ev == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if x > 150 and x < 590 and y > 450 and y < 602:
                return None
            if x > 750 and x < 1190 and y > 450 and y < 602:
                return noms
        elif type_ev == 'Quitte':  # on sort de la boucle
            break

        else:
            pass

##-------Fonctions liste-----------


def init_grille(taille):
    grille = []
    for i in range(taille):
        grille.append(["."] * taille)
    return grille

def affiche_grille(grille):
    for ligne in grille:
        for element in ligne:
            print(element, end=" ")
        print()


def verif (li, col, grille):
    fltk.efface('occupe')
    if grille[li][col] != ".":
        fltk.texte(75, 325, "Cette case est déjà occupée!", couleur = 'black', taille = 20, tag = 'occupe')
        return False
    return True

def complete(grille):
    for ligne in grille:
        for element in ligne:
            if element == ".":
                return False
    return True

def detection (li, col, grille):
    """
    Récupère les coordonner d'un case et vérifie si l'on peut la poser selon les règles du jeus
    """
    
    resultat= False
    verif_haut = True
    verif_bas = True
    verif_gauche = True
    verif_droite = True
    if li==0 :
        verif_haut = False
    if li==7 :
        verif_bas = False
    if col==0 :
        verif_gauche = False
    if col==7 :
        verif_droite = False   
    if verif_haut :
        if grille[li-1][col] != ".": #haut
            resultat = True
    if verif_haut and verif_gauche :
        if grille[li-1][col-1] != ".": #haut gauche
            resultat = True
    if verif_haut and verif_droite :
        if grille[li-1][col+1] != ".": #haut droite
            resultat = True
    if verif_bas :
        if grille[li+1][col] != ".": #bas
            resultat = True
    if verif_bas and verif_gauche :
        if grille[li+1][col-1] != ".": #bas gauche
            resultat = True
    if verif_bas and verif_droite :
        if grille[li+1][col+1] != ".": #bas droite
            resultat = True
    if verif_gauche :
        if grille[li][col-1] != ".": #gauche
            resultat = True
    if verif_droite :
        if grille[li][col+1] != ".": #droite
            resultat = True
    return resultat

def capture_horizontale_droite(li, col, grille, joueur) :
    m = 1
    z = False 
    Test = False
    while Test == False :
        if col+m != 8:
            if grille[li][col+m] == joueur:
                Test = True
                m+=1
                z = True
            else:
                Test = False
                m+=1
        else:
            Test = True
    n=1
    fini2 = False
    if z == True:
        if col + n != 8:
            while grille[li][col+n] != joueur:
                while fini2 == False:
                    if col+n==8 :
                        return grille
        
                    if grille[li][col+n] != "." :
                        grille[li][col+n] = joueur
                    n+=1
                    if grille[li][col+n] == joueur :
                        fini2 = True

def capture_horizontale_gauche(li, col, grille, joueur) :
    m = 1
    z = False 
    Test = False
    while Test == False :
        if col-m != -1:
            if grille[li][col-m] == joueur:
                Test = True
                m+=1
                z = True
            else:
                Test = False
                m+=1
        else:
            Test = True
    n=1
    fini2 = False
    if z == True:
        if col - n != -1:
            while grille[li][col-n] != joueur:
                while fini2 == False:
                    if col-n==-1 :
                        return grille
        
                    if grille[li][col-n] != "." :
                        grille[li][col-n] = joueur
                    n+=1
                    if grille[li][col-n] == joueur :
                        fini2 = True
                        
                        
#regarde les cases qui peut être capturer à la vertical de bas en haut 
def capture_verticale_haut(li, col, grille, joueur) :
    m = 1
    z = False 
    Test = False
    while Test == False :
        if li-m != -1:
            if grille[li-m][col] == joueur:
                Test = True
                m+=1
                z = True
            else:
                Test = False
                m+=1
        else:
            Test = True
    n=1
    fini2 = False
    if z == True: 
        if li - n != -1:
            while grille[li-n][col] != joueur:
                while fini2 == False:
                    if li-n==-1 :
                        return grille
        
                    if grille[li-n][col] != "." :
                        grille[li-n][col] = joueur
                    n+=1
                    if grille[li-n][col] == joueur :
                        fini2 = True
                        
#regarde les cases qui peut être capturer à la vertical de haut en bas                     
def capture_verticale_bas(li, col, grille, joueur) :
    m = 1
    z = False 
    Test = False
    while Test == False :
        if li+m != 8:
            if grille[li+m][col] == joueur:
                Test = True
                m+=1
                z = True
            else:
                Test = False
                m+=1
        else:
            Test = True
    n=1
    fini2 = False
    if z == True: 
        if li + n != 8:
            while grille[li+n][col] != joueur:
                while fini2 == False:
                    if li+n==-1 :
                        return grille
        
                    if grille[li+n][col] != "." :
                        grille[li+n][col] = joueur
                    n+=1
                    if grille[li+n][col] == joueur :
                        fini2 = True
                        

#regarde les cases qui peut être capturer sur la diagonale de bas en haut à droite
def capture_diagonale_haut_droite(li, col, grille, joueur) :
    m = 1
    z = False 
    Test = False
    arreter = False
    while Test == False :
        if li-m == -1 :
            arreter = True
        if col+m == 8 :
            arreter = True
        if arreter == False :
            if grille[li-m][col+m] == joueur:
                Test = True
                m+=1
                z = True
            else:
                Test = False
                m+=1
        else:
            Test = True
    n=1
    fini2 = False
    if z == True: 
        if li-n != -1 or col+n != 8:
            while grille[li-n][col+n] != joueur:
                while fini2 == False:
                    if li-n==-1 or col+n ==8 :
                        return grille
        
                    if grille[li-n][col+n] != "." :
                        grille[li-n][col+n] = joueur
                    n+=1
                    if grille[li-n][col+n] == joueur :
                        fini2 = True
                        
#regarde les cases qui peut être capturer sur la diagonale de bas en haut à gauche 
def capture_diagonale_haut_gauche(li, col, grille, joueur) :
    m = 1
    z = False 
    Test = False
    arreter = False
    while Test == False :
        if li-m == -1 :
            arreter = True
        if col-m == -1 :
            arreter = True
        if arreter == False :
            if grille[li-m][col-m] == joueur:
                Test = True
                m+=1
                z = True
            else:
                Test = False
                m+=1
        else:
            Test = True
    n=1
    fini2 = False
    if z == True: 
        if li-n != -1 or col-n != -1:
            while grille[li-n][col-n] != joueur:
                while fini2 == False:
                    if li-n==-1 or col-n ==-1 :
                        return grille
        
                    if grille[li-n][col-n] != "." :
                        grille[li-n][col-n] = joueur
                    n+=1
                    if grille[li-n][col-n] == joueur :
                        fini2 = True
                        
#regarde les cases qui peut être capturer sur la diagonale de haut en bas à droite
def capture_diagonale_bas_droite(li, col, grille, joueur) :
    m = 1
    z = False 
    Test = False
    arreter = False
    while Test == False :
        if li+m == 8 :
            arreter = True
        if col+m == 8 :
            arreter = True
        if arreter == False :
            if grille[li+m][col+m] == joueur:
                Test = True
                m+=1
                z = True
            else:
                Test = False
                m+=1
        else:
            Test = True
    n=1
    fini2 = False
    if z == True: 
        if li-n != 8 or col+n != 8:
            while grille[li+n][col+n] != joueur:
                while fini2 == False:
                    if li+n==8 or col+n ==8 :
                        return grille
        
                    if grille[li+n][col+n] != "." :
                        grille[li+n][col+n] = joueur
                    n+=1
                    if grille[li+n][col+n] == joueur :
                        fini2 = True
#regarde les cases qui peut être capturer sur la diagonale de haut en bas à gauche 
def capture_diagonale_bas_gauche(li, col, grille, joueur) :
    m = 1
    z = False 
    Test = False
    arreter = False
    while Test == False :
        if li+m == 8 :
            arreter = True
        if col-m == -1 :
            arreter : True
        if arreter == False :    
            if grille[li+m][col-m] == joueur:
                Test = True
                m+=1
                z = True
            else:
                Test = False
                m+=1
        else:
            Test = True
    n=1
    fini2 = False
    if z == True: 
        if li-n != 8 or col-n != -1:
            while grille[li+n][col-n] != joueur:
                while fini2 == False:
                    if li+n==8 or col-n ==-1 :
                        return grille
        
                    if grille[li+n][col-n] != "." :
                        grille[li+n][col-n] = joueur
                    n+=1
                    if grille[li+n][col-n] == joueur :
                        fini2 = True
                        
#capture les cases                     
def capture(li, col, grille, joueur):
    capture_horizontale_droite(li, col, grille, joueur)
    capture_horizontale_gauche(li, col, grille, joueur)
    capture_verticale_bas(li, col, grille, joueur)
    capture_verticale_haut(li, col, grille, joueur)
    capture_diagonale_haut_droite(li, col, grille, joueur)
    capture_diagonale_haut_gauche(li, col, grille, joueur)
    capture_diagonale_bas_droite(li, col, grille, joueur)
    capture_diagonale_bas_gauche(li, col, grille, joueur)

def score(grille, joueur):
    score_joueur=0
    ligne=0
    for i in range(8) :
        for elt in grille[ligne]:
            if elt==joueur :
                score_joueur+=1
        ligne+=1
    return score_joueur

#affiche le nom du gagnant
def gagnant(lst_score, lst_joueurs, manche, tiebreaks):
    maximum=lst_score[0]
    indice_maximum=0
    for i in range(len(lst_score)):
        if lst_score[i]>maximum:
            maximum=lst_score[i]
            indice_maximum=i
        elif lst_score[i]==maximum:
            if manche == True:
                if tiebreaks[indice_maximum] < tiebreaks[i] :
                    maximum=lst_score[i]
                    indice_maximum=i
                
                
    return lst_joueurs[indice_maximum]

#---Programme principal---------

if __name__ == "__main__":
    grille = init_grille(8)
    grille[3][3]= "B"
    grille[3][4]= "R"
    grille[4][3]= "V"
    grille[4][4]= "J"

    systeme_points=''
    nombre_joueur = 0
    manche_choisie = 0
    points_manches_rouge=0
    points_manches_vert=0
    points_manches_jaune=0
    points_manches_bleu=0
    tiebreaks=[0, 0, 0, 0]
    liste_score=[]
    reprendre = False
    liste_joueurs=["R", "V", "J", "B"]


    fltk.cree_fenetre(LARG,HAUT)

    page_acceuil = True
    while page_acceuil:
        quitter = False
        fltk.efface_tout()
        acceuil_identifiant = fltk.image (670, 377, 'rolit_acceuil.gif', ancrage = 'center', tag ='im')
        #fltk.repere(50)
        ev = fltk.attend_ev()
        type_ev = fltk.type_ev(ev)
        if type_ev == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if x > 560 and x < 770 and y > 500 and y < 540:
                lecteur = open('sav.txt')
                etat_restaure = json.load(lecteur)
                lecteur.close()
                if etat_restaure != {}:
                    print('ya')
                    page_reprendre = True
                    fltk.efface_tout()
                    fltk.texte(677, 300, 'VOULEZ-VOUS REPRENDRE LA PARTIE PRECEDENTE ?', taille = 23, ancrage = 'center', tag = 'reprendre')
                    fltk.rectangle (750, 450, 1190, 602, couleur = 'black', remplissage = 'white', epaisseur = 7, tag = 'rectangle_2')
                    fltk.rectangle (150, 450, 590, 602, couleur = 'black', remplissage = 'white', epaisseur = 7, tag = 'rectangle_2')
                    fltk.texte (940, 510, 'OUI', couleur = 'black', taille = 20, tag = 'continuer_2')
                    fltk.texte (330, 510, 'NON', couleur = 'black', taille = 20, tag = 'continuer_2')
                    while page_reprendre == True:
                        ev = fltk.attend_ev()
                        type_ev = fltk.type_ev(ev)
                        if type_ev == "ClicGauche" :
                            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                            if x > 150 and x < 590 and y > 450 and y < 602:
                                page_reprendre = False
                                reprendre = False
                            if x > 750 and x < 1190 and y > 450 and y < 602:
                                page_reprendre = False
                                reprendre = True
                                demarrer = True
                if reprendre == False:
                    fltk.efface_tout()
                    fltk.rectangle (0,0 ,1340, 755, couleur = 'white', remplissage = 'white')
                    parametre_identifiant = fltk.image (670, 377, 'parametres_partie_2.gif', ancrage = 'center', tag ='im')
                    fltk.image(25,25, 'fleche_retour.gif', ancrage = 'center', tag = 'im')
                    #fltk.repere(50)
                    ecran_parametre = True
                    demarrer = False
                    while ecran_parametre == True:
                        ev = fltk.attend_ev()
                        type_ev = fltk.type_ev(ev)
                        if type_ev == "ClicGauche" :
                            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                            if x > 0 and x < 50 and y > 0 and y < 50:
                                ecran_parametre = False
                                manche_choisie = 0
                                nombre_joueur = 0
                            elif x > 0 and x < 365 and y > 660 and y < 745:
                                continuer_3 = True
                                while continuer_3:
                                    fltk.image(670, 377, 'regle_jeu.gif', ancrage = 'center', tag ='regle')
                                    ev = fltk.attend_ev()
                                    type_ev = fltk.type_ev(ev)
                                    if type_ev == "ClicGauche" :
                                        x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                                        if x > 15 and x < 230 and y > 30 and y < 80:
                                            fltk.efface('regle')
                                            continuer_3 = False
                            
                            if x > 390 and x < 450 and y > 205 and y < 255:
                                fltk.efface('carre_1')
                                nombre_joueur = 2
                                fltk.rectangle(385, 195, 460, 265, couleur = 'green', tag = 'carre_1', epaisseur = 5 )
                            if x > 490 and x < 540 and y > 205 and y < 255:
                                fltk.efface('carre_1')
                                nombre_joueur = 3
                                fltk.rectangle(480, 195, 555, 265, couleur = 'green', tag = 'carre_1', epaisseur = 5 )
                            if x > 585 and x < 640 and y > 205 and y < 255:
                                fltk.efface('carre_1')
                                nombre_joueur = 4
                                fltk.rectangle(575, 195, 650, 265, couleur = 'green', tag = 'carre_1', epaisseur = 5 )
                            if x > 645 and x < 695 and y > 310 and y < 360:
                                fltk.efface('carre_2')
                                manche_choisie = 1
                                fltk.rectangle(635, 305, 705, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                            if x > 740 and x < 790 and y > 310 and y < 360:
                                fltk.efface('carre_2')
                                manche_choisie = 2
                                fltk.rectangle(732, 305, 800, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                            if x > 840 and x < 890 and y > 310 and y < 360:
                                fltk.efface('carre_2')
                                manche_choisie = 3
                                fltk.rectangle(830, 305, 895, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                            if x > 935 and x < 985 and y > 310 and y < 360:
                                fltk.efface('carre_2')
                                manche_choisie = 4
                                fltk.rectangle(925, 305, 995, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                            if x > 1030 and x < 1080 and y > 310 and y < 360:
                                fltk.efface('carre_2')
                                manche_choisie = 5
                                fltk.rectangle(1022, 305, 1090, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                            if x > 410 and x < 565 and y > 398 and y < 480:
                                fltk.efface('rectangle')
                                systeme_points = 'total'
                                fltk.rectangle(405, 390, 575, 490, couleur = 'green', tag = 'rectangle', epaisseur = 5 )
                            if x > 610 and x < 754 and y > 398 and y < 480:
                                fltk.efface('rectangle')
                                systeme_points = 'manches'
                                fltk.rectangle(605, 390, 768, 490, couleur = 'green', tag = 'rectangle', epaisseur = 5 )
                            if x > 460 and x < 893 and y > 570 and y < 720:
                                if manche_choisie != 0 and nombre_joueur != 0:
                                    demarrer = True
                                    ecran_parametre = False
                                else:
                                    fltk.texte(950, 650, "Il faut choisir un nombre de joueurs et de manche", couleur = 'black', taille = 10)
                                    demarrer = False
                            if demarrer == True:
                                liste_noms_joueurs = []
                                for i in range (nombre_joueur):
                                    if demarrer == True:
                                        liste_noms_joueurs.append(noms_joueurs())
                                        if liste_noms_joueurs[i] == None:
                                            demarrer = False
                                    
                                        
                if demarrer == True:
                    if reprendre == True:
                        systeme_points = etat_restaure["systeme_points"]
                    fltk.efface_tout()
                    #fltk.repere(50)
                    fltk.rectangle (0,0 ,1340, 755, couleur = 'white', remplissage = 'white')
                    fltk.image(25,25, 'engrenage.gif', ancrage = 'center') 
                    show_grid_with_marks(TAILLE, TAILLE_CEL, X_OFFSET, Y_OFFSET)
                    fltk.texte(55, 65, "JOUEUR ACTIF :", couleur = 'black', taille=15)
                    fltk.texte(55, 165, "JOUEUR SUIVANT :", couleur = 'black', taille=15)
                    #score
                    fltk.texte(185, 455, "SCORES", couleur = 'black', taille=15)
                    fltk.cercle(75, 525, TAILLE_CEL*0.45, remplissage ='red', epaisseur = 1, tag = 'cercle_score')
                    fltk.cercle(175, 525, TAILLE_CEL*0.45, remplissage ='green', epaisseur = 1, tag = 'cercle_score')
                    fltk.cercle(275, 525, TAILLE_CEL*0.45, remplissage ='yellow', epaisseur = 1, tag = 'cercle_score')
                    fltk.cercle(375, 525, TAILLE_CEL*0.45, remplissage ='blue', epaisseur = 1, tag = 'cercle_score')
                    #total
                    if systeme_points=='total':
                        fltk.cercle(75, 675, TAILLE_CEL*0.45, remplissage ='red', epaisseur = 1, tag = 'cercle_total')
                        fltk.cercle(175, 675, TAILLE_CEL*0.45, remplissage ='green', epaisseur = 1, tag = 'cercle_total')
                        fltk.cercle(275, 675, TAILLE_CEL*0.45, remplissage ='yellow', epaisseur = 1, tag = 'cercle_total')
                        fltk.cercle(375, 675, TAILLE_CEL*0.45, remplissage ='blue', epaisseur = 1, tag = 'cercle_total')
                        fltk.texte(140, 605, "SCORES TOTAUX", couleur = 'black', taille=15)
                    elif systeme_points=='manches':
                        fltk.cercle(75, 675, TAILLE_CEL*0.45, remplissage ='red', epaisseur = 1, tag = 'cercle_manches')
                        fltk.cercle(175, 675, TAILLE_CEL*0.45, remplissage ='green', epaisseur = 1, tag = 'cercle_manches')
                        fltk.cercle(275, 675, TAILLE_CEL*0.45, remplissage ='yellow', epaisseur = 1, tag = 'cercle_manches')
                        fltk.cercle(375, 675, TAILLE_CEL*0.45, remplissage ='blue', epaisseur = 1, tag = 'cercle_manches')
                        fltk.texte(108, 605, "MANCHES REMPORTÉES", couleur = 'black', taille=15)
                        
                    if reprendre == False:
                        compte = 0
                        n=0
                        score_manche=[0, 0, 0, 0]
                        score_total=[0, 0, 0, 0]
                        liste_score_totaux=[]
                        tiebreaks=[0, 0, 0, 0]
                        manches_totaux=[0, 0, 0, 0]
                        points_manches_rouge=0
                        points_manches_vert=0
                        points_manches_jaune=0
                        points_manches_bleu=0
                        manche = 0
                    if reprendre == True:
                        compte = 1
                        n = etat_restaure["n"]
                        score_manche = etat_restaure["score_manche"]
                        score_total = etat_restaure["score_total"]
                        liste_score_totaux =etat_restaure["liste_score_totaux"]
                        manches_totaux=etat_restaure["manches_totaux"]
                        points_manches_rouge=etat_restaure["points_manches_rouge"]
                        points_manches_vert=etat_restaure["points_manches_vert"]
                        points_manches_jaune=etat_restaure["points_manches_jaune"]
                        points_manches_bleu=etat_restaure["points_manches_bleu"]
                        manche = etat_restaure["manche"]
                        manche_choisie = etat_restaure["nb_manches"]
                        nombre_joueur = etat_restaure["nb_joueurs"]
                        liste_noms_joueurs = etat_restaure["noms_j"]
                    while manche < manche_choisie:
                        
                        grille = init_grille(8)
                        grille[3][3]= "B"
                        grille[3][4]= "R"
                        grille[4][3]= "V"
                        grille[4][4]= "J"
                        #affiche_grille(grille)
                        arreter=False
                        
                        Ini_xc, Ini_yc = centre_pixel(3, 3, TAILLE_CEL, X_OFFSET, Y_OFFSET)
                        yes = fltk.cercle(Ini_xc, Ini_yc, TAILLE_CEL*0.4, remplissage ='blue', epaisseur = 1, tag = 'cercle')
                        Ini_xc, Ini_yc = centre_pixel(3, 4, TAILLE_CEL, X_OFFSET, Y_OFFSET)
                        yes_1 = fltk.cercle(Ini_xc, Ini_yc, TAILLE_CEL*0.4, remplissage ='red', epaisseur = 1, tag = 'cercle')
                        Ini_xc, Ini_yc = centre_pixel(4, 3, TAILLE_CEL, X_OFFSET, Y_OFFSET)
                        yes_2 = fltk.cercle(Ini_xc, Ini_yc, TAILLE_CEL*0.4, remplissage ='green', epaisseur = 1, tag = 'cercle')
                        Ini_xc, Ini_yc = centre_pixel(4, 4, TAILLE_CEL, X_OFFSET, Y_OFFSET)
                        yes_3 = fltk.cercle(Ini_xc, Ini_yc, TAILLE_CEL*0.4, remplissage ='yellow', epaisseur = 1, tag = 'cercle')
                        score_rouge(liste_joueurs, grille)
                        score_vert(liste_joueurs, grille)
                        score_jaune(liste_joueurs, grille)
                        score_bleu(liste_joueurs, grille)
                        
                        if reprendre == True and compte == 1:
                            grille = etat_restaure["grille"]
                            score_rouge(liste_joueurs, grille)
                            score_vert(liste_joueurs, grille)
                            score_jaune(liste_joueurs, grille)
                            score_bleu(liste_joueurs, grille)
                            actualisation(grille)
                            compte = 0
                        
                        
                        page_jeu = True
                        while page_jeu :
                            if x > 0 and x < 50 and y > 0 and y < 50:
                                page_parametre_check = True
                                while page_parametre_check:
                                    
                                    fltk.rectangle (0,0,1340, 20, couleur = 'white', remplissage = 'white', tag = 'rectangle_2')
                                    parametre_identifiant = fltk.image (670, 377, 'parametres_partie_2.gif', ancrage = 'center', tag ='para_2')
                                    #fltk.repere(50)
                                    fltk.rectangle (460, 570, 900, 722, couleur = 'black', remplissage = 'white', epaisseur = 10, tag = 'rectangle_2')
                                    fltk.rectangle (950, 608, 1300, 684, couleur = 'black', remplissage = 'white', epaisseur = 7, tag = 'rectangle_2')
                                    fltk.texte (600, 635, 'CONTINUER', couleur = 'black', taille = 20, tag = 'continuer_2')
                                    fltk.texte (1060, 630, 'QUITTER', couleur = 'black', taille = 20, tag = 'continuer_2')
                                    if manche_choisie == 1:
                                        fltk.rectangle(635, 305, 705, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                                    elif manche_choisie == 2:
                                        fltk.rectangle(732, 305, 800, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )    
                                    elif manche_choisie == 3:
                                        fltk.rectangle(830, 305, 895, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                                    elif manche_choisie == 4:
                                        fltk.rectangle(925, 305, 995, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                                    elif manche_choisie == 5:
                                        fltk.rectangle(1022, 305, 1090, 370, couleur = 'green', tag = 'carre_2', epaisseur = 5 )
                                    if nombre_joueur == 2:
                                        fltk.rectangle(385, 195, 460, 265, couleur = 'green', tag = 'carre_1', epaisseur = 5 )
                                    elif nombre_joueur == 3:
                                        fltk.rectangle(480, 195, 555, 265, couleur = 'green', tag = 'carre_1', epaisseur = 5 )
                                    elif nombre_joueur == 4:
                                        fltk.rectangle(575, 195, 650, 265, couleur = 'green', tag = 'carre_1', epaisseur = 5 )
                                    if systeme_points == 'total':
                                        fltk.rectangle(405, 390, 575, 490, couleur = 'green', tag = 'rectangle', epaisseur = 5 )    
                                    elif systeme_points == 'manches':
                                        fltk.rectangle(605, 390, 768, 490, couleur = 'green', tag = 'rectangle', epaisseur = 5 )
                                    
                                    ev = fltk.attend_ev()
                                    type_ev = fltk.type_ev(ev)
                                    if type_ev == "ClicGauche" :
                                        x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                                        if x > 950 and x < 1300 and y > 570 and y < 900:
                                            fltk.image (670, 377, 'save_confirmer.gif', ancrage = 'center', tag = 'save')
                                            fltk.image(25,25, 'fleche_retour.gif', ancrage = 'center', tag = 'fleche')
                                            #fltk.repere(50)
                                            page_quitter = True
                                            while page_quitter == True:
                                                ev = fltk.attend_ev()
                                                type_ev = fltk.type_ev(ev)
                                                if type_ev == "ClicGauche" :
                                                    x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                                                    if x > 0 and x < 50 and y > 0 and y < 50:
                                                        page_quitter = False
                                                        fltk.efface('save')
                                                        fltk.efface('fleche')
                                                    elif x > 505 and x < 835 and y > 566 and y < 640:
                                                        page_quitter = False
                                                        fltk.efface('save')
                                                        fltk.efface('fleche')
                                                    elif x > 269 and x < 600 and y > 450 and y < 535:
                                                        score_manche_joueurs = [points_manches_rouge, points_manches_vert, points_manches_jaune, points_manches_bleu]
                                                        etat_jeu = {"systeme_points" : systeme_points, "nb_joueurs" : nombre_joueur,"nb_manches" : manche_choisie , "score_manche" : score_manche_joueurs ,"n":n, "score_total" : score_total, "liste_score_totaux": liste_score_totaux, "manches_totaux": manches_totaux, "points_manches_rouge": points_manches_rouge, "points_manches_vert": points_manches_vert,"points_manches_jaune": points_manches_jaune,"points_manches_bleu":points_manches_bleu, "manche":manche , "noms_j" : liste_noms_joueurs, "grille" : grille}                                                                                 
                                                        ecrivain = open('sav.txt', 'w')
                                                        contenu = json.dump(etat_jeu, ecrivain)
                                                        ecrivain.close()
                                                        fltk.efface_tout()
                                                        page_parametre_check = False
                                                        page_jeu = False
                                                        page_quitter = False
                                                        demarrer = False
                                                        quitter = True
                                                        n=0
                                                        grille = init_grille(8)
                                                        grille[3][3]= "B"
                                                        grille[3][4]= "R"
                                                        grille[4][3]= "V"
                                                        grille[4][4]= "J"
                                                        systeme_points=''
                                                        nombre_joueur = 0
                                                        manche_choisie = 0
                                                        points_manches_rouge=0
                                                        points_manches_vert=0
                                                        points_manches_jaune=0
                                                        points_manches_bleu=0
                                                        liste_score=[]
                                                        liste_joueurs=["R", "V", "J", "B"]
                                                        fltk.efface_tout()
                                                    elif x > 740 and x < 1170 and y > 450 and y < 535:
                                                        etat_jeu = {}
                                                        ecrivain = open('sav.txt', 'w')
                                                        contenu = json.dump(etat_jeu, ecrivain)
                                                        ecrivain.close()
                                                        fltk.efface_tout()
                                                        page_parametre_check = False
                                                        page_jeu = False
                                                        page_quitter = False
                                                        demarrer = False
                                                        quitter = True
                                                        n=0
                                                        grille = init_grille(8)
                                                        grille[3][3]= "B"
                                                        grille[3][4]= "R"
                                                        grille[4][3]= "V"
                                                        grille[4][4]= "J"
                                                        systeme_points=''
                                                        nombre_joueur = 0
                                                        manche_choisie = 0
                                                        points_manches_rouge=0
                                                        points_manches_vert=0
                                                        points_manches_jaune=0
                                                        points_manches_bleu=0
                                                        liste_score=[]
                                                        tiebreaks=[0, 0, 0, 0]
                                                        liste_joueurs=["R", "V", "J", "B"]
                                                        fltk.efface_tout()
                                        if x > 0 and x < 365 and y > 660 and y < 745:
                                            page_regle_2 = True
                                            while page_regle_2:
                                                fltk.image(670, 377, 'regle_jeu.gif', ancrage = 'center', tag ='regle')
                                                ev = fltk.attend_ev()
                                                type_ev = fltk.type_ev(ev)
                                                if type_ev == "ClicGauche" :
                                                    x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                                                    if x > 15 and x < 230 and y > 30 and y < 80:
                                                        fltk.efface('regle')
                                                        page_regle_2 = False
                                        if x > 460 and x < 900 and y > 570 and y < 722:
                                            fltk.efface('para_2')
                                            fltk.efface('continuer_2')
                                            fltk.efface('rectangle_2')
                                            fltk.efface('carre_1')
                                            fltk.efface('carre_2')
                                            fltk.efface('rectangle')
                                            page_parametre_check = False
                            if page_jeu == False:
                                pass
                            else:
                                joueur_actif=0
                                joueur_suivant=0
                                couleur_active=''
                                if n==nombre_joueur:
                                    n=0
                                joueur_actif = liste_joueurs[n]
                                if n+1==nombre_joueur:
                                    joueur_suivant=liste_joueurs[0]
                                else:
                                    joueur_suivant = liste_joueurs[n+1]
                                            
                                couleur_active = couleur_joueur(joueur_actif)
                                current_player(couleur_joueur(joueur_actif), liste_noms_joueurs)
                                next_player(couleur_joueur(joueur_suivant), liste_noms_joueurs)
                                
                                score_manche = score_joueurs(liste_joueurs, grille)
                                
                                if systeme_points=='total':
                                    liste_score_totaux = score_total_joueurs(liste_joueurs, score_total, grille)
                                if systeme_points=='manches':
                                    manches_joueurs (points_manches_rouge, points_manches_vert, points_manches_jaune, points_manches_bleu)
                                if arreter==True:
                                    if systeme_points=='manches':   
                                        lst_score_manches=[]
                                        for joueur in liste_joueurs :
                                            lst_score_manches.append(score(grille, joueur))  
                                        winner=gagnant(lst_score_manches, liste_joueurs, False, tiebreaks)
                                        if winner=="R":
                                            points_manches_rouge += 1
                                        elif winner=="V":
                                            points_manches_vert += 1
                                        elif winner=="J":
                                            points_manches_jaune += 1
                                        elif winner=="B":
                                            points_manches_bleu += 1
                                        manches_joueurs(points_manches_rouge, points_manches_vert, points_manches_jaune, points_manches_bleu)   
                                    break
                                ev = fltk.attend_ev()
                                type_ev = fltk.type_ev(ev)
                                if type_ev == "Quitte":
                                    fltk.ferme_fenetre()
                                elif type_ev == "ClicGauche" :
                                    x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                                    li, col = pix_vers_cel(x, y, TAILLE, TAILLE_CEL, X_OFFSET, Y_OFFSET)
                                    xc, yc = centre_pixel(li, col, TAILLE_CEL, X_OFFSET, Y_OFFSET)
                                    if li < 8 and li >-1 and col < 8 and col > -1:
                                        verification = verif(li, col, grille)
                                        if verification == True:
                                            if detection(li, col, grille) == True :
                                                grille[li][col] = joueur_actif
                                                capture(li, col, grille, joueur_actif)
                                                actualisation(grille)
                                                n+=1
                                                if complete(grille)==True :
                                                    lst_scores_manche=[]
                                                    nm=0
                                                    score_temp=0
                                                    while nm != len(liste_joueurs):
                                                        score_temp=score(grille, liste_joueurs[nm])
                                                        lst_scores_manche.append(score_temp)
                                                        tiebreaks[nm]+=score_temp
                                                        nm+=1
                                                    gagnant_manche=''
                                                    gagnant_manche=gagnant(lst_scores_manche, liste_joueurs, False, tiebreaks)
                                                    if gagnant_manche == "R":
                                                        fltk.cercle(100, 340, TAILLE_CEL*0.45, remplissage ='red', epaisseur = 1, tag = 'next_manche')
                                                    elif gagnant_manche == "V":
                                                        fltk.cercle(100, 340, TAILLE_CEL*0.45, remplissage ='green', epaisseur = 1, tag = 'next_manche')
                                                    elif gagnant_manche == "J":
                                                        fltk.cercle(100, 340, TAILLE_CEL*0.45, remplissage ='yellow', epaisseur = 1, tag = 'next_manche')
                                                    elif gagnant_manche == "B":
                                                        fltk.cercle(100, 340, TAILLE_CEL*0.45, remplissage ='blue', epaisseur = 1, tag = 'next_manche')
                                                    fltk.texte(175, 325, "remporte la manche!", couleur = 'black', taille = 20, tag = 'next_manche')
                                                    fltk.rectangle(1050, 695, 1335, 750, couleur = 'orange', remplissage='orange', epaisseur ='2', tag='next_manche')
                                                    fltk.texte(1190, 725, "SUIVANT", couleur = 'white', taille = 20, ancrage = 'center', tag = 'next_manche')
                                                    manche_suivante=True
                                                    while manche_suivante:
                                                        ev = fltk.attend_ev()
                                                        type_ev = fltk.type_ev(ev)
                                                        if type_ev == "ClicGauche" :
                                                            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                                                            if x > 1050 and x < 1335 and y > 695 and y < 750: #manche suivante
                                                                fltk.efface('next_manche')
                                                                manche_suivante = False
                                                                arreter=True
                                                                reprendre = False
                                
                                if type_ev == "Quitte":
                                    break
                        if systeme_points=='total':
                            score_total[0]+=score_manche[0]
                            score_total[1]+=score_manche[1]
                            score_total[2]+=score_manche[2]
                            score_total[3]+=score_manche[3]
                        
                        fltk.efface('cercle')
                        
                        
                        manche+=1
                    gagnant_final=''
                    if systeme_points=='total':
                        gagnant_final=gagnant(liste_score_totaux, liste_joueurs, False, tiebreaks)
                    elif systeme_points=='manches':
                        liste_manches_finale=[]
                        liste_manches_finale.append(points_manches_rouge)
                        liste_manches_finale.append(points_manches_vert)
                        liste_manches_finale.append(points_manches_jaune)
                        liste_manches_finale.append(points_manches_bleu)
                        gagnant_final=gagnant(liste_manches_finale, liste_joueurs, True, tiebreaks)
                        
                    if quitter == False:    
                        ecran_de_victoire = True
                        while ecran_de_victoire :
                            fltk.image(670, 377, 'BRAVO.gif', ancrage = 'center', tag = 'ecran_manche')
                            #fltk.repere(50)
                            if gagnant_final=="R":
                                fltk.cercle(410, 245, TAILLE_CEL*0.6, remplissage ='red', epaisseur = 1, tag = 'winner')
                                if systeme_points=='total':
                                    fltk.texte(595, 380, f"{liste_score_totaux[0]}", ancrage = 'center', couleur = 'black', taille=35, tag = 'winner')
                                elif systeme_points=='manches':
                                    fltk.texte(595, 380, f"{points_manches_rouge}", ancrage = 'center', couleur = 'black', taille=35, tag = 'winner')
                            if gagnant_final=="V":
                                fltk.cercle(410, 245, TAILLE_CEL*0.6, remplissage ='green', epaisseur = 1, tag = 'winner')
                                if systeme_points=='total':
                                    fltk.texte(595, 380, f"{liste_score_totaux[1]}", ancrage = 'center', couleur = 'black', taille=35, tag = 'winner')
                                elif systeme_points=='manches':
                                    fltk.texte(595, 380, f"{points_manches_vert}", ancrage = 'center', couleur = 'black', taille=35, tag = 'winner')
                            if gagnant_final=="J":
                                fltk.cercle(410, 245, TAILLE_CEL*0.6, remplissage ='yellow', epaisseur = 1, tag = 'winner')
                                if systeme_points=='total':
                                    fltk.texte(595, 380, f"{liste_score_totaux[2]}", ancrage = 'center', couleur = 'black', taille=35, tag = 'winner')
                                elif systeme_points=='manches':
                                    fltk.texte(595, 380, f"{points_manches_jaune}", ancrage = 'center', couleur = 'black', taille=35, tag = 'winner')
                            if gagnant_final=="B":
                                fltk.cercle(410, 245, TAILLE_CEL*0.6, remplissage ='blue', epaisseur = 1, tag = 'winner')
                                if systeme_points=='total':
                                    fltk.texte(595, 380, f"{liste_score_totaux[3]}", ancrage = 'center', couleur = 'black', taille=35, tag = 'winner')
                                elif systeme_points=='manches':
                                    fltk.texte(595, 380, f"{points_manches_bleu}", ancrage = 'center', couleur = 'black', taille=35, tag = 'winner')
                            
                            
                            ev = fltk.attend_ev()
                            type_ev = fltk.type_ev(ev)
                            if type_ev == "ClicGauche" :
                                x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                                if x > 440 and x < 980 and y > 540 and y < 670: #retour à l'accueil
                                    ecran_de_victoire = False
                                    etat_jeu = {}
                                    ecrivain = open('sav.txt', 'w')
                                    contenu = json.dump(etat_jeu, ecrivain)
                                    ecrivain.close()
                        
                        
                        
                        
            elif x > 560 and x < 770 and y > 625 and y < 665:
                fltk.efface_tout()
                fltk.image (670, 377, 'fond_blanc.gif', ancrage = 'center', tag ='im')
                quitter_identifiant = fltk.image (670, 377, 'quitter.gif', ancrage = 'center', tag ='im')
                
                #fltk.repere(50)
                yes = True
                while yes:
                    ev = fltk.attend_ev()
                    type_ev = fltk.type_ev(ev)
                    if type_ev == "ClicGauche" :
                        x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                        if x > 550 and x < 620 and y > 395 and y < 420:
                            fltk.efface_tout()
                            yes = False
                            page_acceuil = False
                            fltk.ferme_fenetre()
                            break
                        if x > 730 and x < 790 and y > 395 and y < 420:
                            fltk.efface_tout()
                            page_acceuil = True
                            yes = False



    

