import fltk
from random import randint

#---------idees---------
# a chaque lancer de des mettre dans l'espace manquant une case tips avec des tips biens cons sa mere ou alors un camera roll d'images banger tier

#IL FAUT FAIRE
#1) bloquer les lignes quand elles sont finies
#2) valider les lignes
#3) décaler les pions d'un petit peu s'il y en a 2 sur la même case pour pas qu'ils se chevauchent visuellement
#4) marquer la fin de la partie si qqn valide 3 lignes
#------s'il reste plus de pions un 8-8 avancera qu'une fois sur 8

#5) faire le github
#6) permettre le choix des couleurs

#---------idees---------

#---------grille-de-base---------
def init_colonnes():
    nb=3
    nb2=0
    col=2
    ecart=0
    ecart_col=0
    it=0
    for i in range(6):
        for i in range(nb+nb2):
            if it!=((nb+nb2)-1):
                fltk.cercle(525+ecart_col, 950-ecart, 25 , remplissage ='gray', epaisseur = 1.5 , tag = f'colonne_{col}_num_{it}')
            else:
                fltk.cercle(525+ecart_col, 950-ecart, 25 , remplissage ='white', epaisseur = 2.5 , tag = f'colonne_{col}_final')
                fltk.texte(525+ecart_col, 950-ecart, f'{col}', taille = 25, ancrage = 'center', police='impact', tag = 'texte_grille_base')
            ecart+=75
            it+=1
        ecart=0
        ecart_col+=100
        nb+=1
        nb2+=1
        col+=1
        it=0
    nb-=2
    nb2-=2
    for i in range(5):
        for i in range(nb+nb2):
            if it!=((nb+nb2)-1):
                fltk.cercle(525+ecart_col, 950-ecart, 25 , remplissage ='gray', epaisseur = 1.5 , tag = f'colonne_{col}_num_{it}')
            else:
                fltk.cercle(525+ecart_col, 950-ecart, 25 , remplissage ='white', epaisseur = 2.5 , tag = f'colonne_{col}_final')
                fltk.texte(525+ecart_col, 950-ecart, f'{col}', taille = 25, ancrage = 'center', police='impact', tag = 'texte_grille_base')
            ecart+=75
            it+=1
        ecart=0
        ecart_col+=100
        nb-=1
        nb2-=1
        col+=1
        it=0
#---------grille-de-base---------
        
#---------fonctions-du-lancer-de-des--------------
def lancer_des():
    lst_des=[]
    for i in range(4):
        lst_des.append(randint(1, 6))
    return lst_des


def possib_1(lst):
    lst_inter=[]
    lst_inter.append(lst[0]+lst[1])
    lst_inter.append(lst[2]+lst[3])
    return lst_inter


def possib_2(lst):
    lst_inter=[]
    lst_inter.append(lst[0]+lst[2])
    lst_inter.append(lst[1]+lst[3])
    return lst_inter


def possib_3(lst):
    lst_inter=[]
    lst_inter.append(lst[0]+lst[3])
    lst_inter.append(lst[1]+lst[2])
    return lst_inter


def lst_possib(lst):
    lst_final=[]
    lst_final.append(possib_1(lst))
    lst_final.append(possib_2(lst))
    lst_final.append(possib_3(lst))
    return lst_final


def actuellement_en_larmes(lst_lock, lst_pions):
    # la fonction aurait pu etre mieux ecrite mais j'ai eu pleins de bugs et j'ai pété les plombs du coup je l'ai écrite comme si j'avais
    # un an et demi et ça marchait quand même mieux, du coup j'ai laissé tant pis
    if 2 not in lst_pions:
        if 2 not in lst_lock:
            lst_lock.append(2)
    if 3 not in lst_pions:
        if 3 not in lst_lock:
            lst_lock.append(3)
    if 4 not in lst_pions:
        if 4 not in lst_lock:
            lst_lock.append(4)
    if 5 not in lst_pions:
        if 5 not in lst_lock:
            lst_lock.append(5)
    if 6 not in lst_pions:
        if 6 not in lst_lock:
            lst_lock.append(6)
    if 7 not in lst_pions:
        if 7 not in lst_lock:
            lst_lock.append(7)
    if 8 not in lst_pions:
        if 8 not in lst_lock:
            lst_lock.append(8)
    if 9 not in lst_pions:
        if 9 not in lst_lock:
            lst_lock.append(9)
    if 10 not in lst_pions:
        if 10 not in lst_lock:
            lst_lock.append(10)
    if 11 not in lst_pions:
        if 11 not in lst_lock:
            lst_lock.append(11)
    if 12 not in lst_pions:
        if 12 not in lst_lock:
            lst_lock.append(12)
    
        
    
#---------fonction-du-lancer-de-des--------------

#---------fonction-des-blocs-----------
def mastadinguerie():
    fltk.efface('rectangle_possib_1')
    fltk.efface('rectangle_possib_2')
    fltk.efface('rectangle_possib_3')
    fltk.efface('texte_possib_1')
    fltk.efface('texte_possib_2')
    fltk.efface('texte_possib_3')
    
   
def blocs_possib(lst, nb_pions, lst_splice, lst_pions, criteras):
    mastadinguerie()
    lst_pablo=[]
    #ETAPE 1
    end=False
    wrongline_split=False
    wrongline_normal=False
    uno=False
    zero=False
    jsp=None
    if len(lst[0])==0:
        fltk.rectangle(100, 680, 300, 750, couleur='black', remplissage='red', epaisseur=5, tag='rectangle_possib_1')
        fltk.texte(200, 713, 'x', taille = 30, ancrage = 'center', police='impact', tag = 'texte_possib_1')
        lst_pablo.append(False)
        zero=True
    elif len(lst[0])==1:
        uno=True     
    if zero==False:
        lst_pablo.append(True)
        if nb_pions==1:
            bernardo=False
            for elt in lst[0]:
                if elt in lst_pions:
                    bernardo=True
            if bernardo==False:
                if criteras[0]==True:
                    if criteras[2]==1:
                        if criteras[3]==True:
                            if criteras[4]==1:
                                fltk.rectangle(100, 680, 190, 750, couleur='black', remplissage= 'green' , epaisseur=5, tag='rectangle_possib_1')
                                fltk.rectangle(210, 680, 300, 750, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                                fltk.texte(145, 713, f'{lst[0][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                fltk.texte(255, 713, f'{lst[0][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                wrongline_split=True
                            elif criteras[4]==2:
                                fltk.rectangle(100, 680, 190, 750, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                                fltk.rectangle(210, 680, 300, 750, couleur='black', remplissage= 'green' , epaisseur=5, tag='rectangle_possib_1')
                                fltk.texte(145, 713, f'{lst[0][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                fltk.texte(255, 713, f'{lst[0][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                wrongline_split=True
                            lst_splice[0]=True
                            end=True
                jsp=criteras[0] and wrongline_split
                if jsp==False:
                    fltk.rectangle(100, 680, 190, 750, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                    fltk.rectangle(210, 680, 300, 750, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                    fltk.texte(145, 713, f'{lst[0][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                    fltk.texte(255, 713, f'{lst[0][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                    lst_splice[0]=True
                    end=True
        if end==False:
            if criteras[0]==True:
                if criteras[2]==1:
                    fltk.rectangle(100, 680, 300, 750, couleur='black', remplissage= 'green' , epaisseur=5, tag='rectangle_possib_1')
                    wrongline_normal=True
            jsp=criteras[0] and wrongline_normal
            if jsp==False:       
                fltk.rectangle(100, 680, 300, 750, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
            if uno==True:
                fltk.texte(200, 713, f'{lst[0][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
            else:
                fltk.texte(200, 713, f'{lst[0][0]}  -  {lst[0][1]}', taille = 30, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                
    #ETAPE 2            
    end=False
    wrongline_split=False
    wrongline_normal=False
    uno=False
    zero=False
    if len(lst[1])==0:
        fltk.rectangle(100, 580, 300, 650, couleur='black', remplissage='red', epaisseur=5, tag='rectangle_possib_1')
        fltk.texte(200, 613, 'x', taille = 30, ancrage = 'center', police='impact', tag = 'texte_possib_1')
        lst_pablo.append(False)
        zero=True
    elif len(lst[1])==1:
        uno=True     
    if zero==False:
        lst_pablo.append(True)
        if nb_pions==1:
            bernardo=False
            for elt in lst[1]:
                if elt in lst_pions:
                    bernardo=True
            if bernardo==False:
                if criteras[0]==True:
                    if criteras[2]==2:
                        if criteras[3]==True:
                            if criteras[4]==1:
                                fltk.rectangle(100, 580, 190, 650, couleur='black', remplissage= 'green', epaisseur=5, tag='rectangle_possib_1')
                                fltk.rectangle(210, 580, 300, 650, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                                fltk.texte(145, 613, f'{lst[1][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                fltk.texte(255, 613, f'{lst[1][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                wrongline_split=True
                            elif criteras[4]==2:
                                fltk.rectangle(100, 580, 190, 650, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                                fltk.rectangle(210, 580, 300, 650, couleur='black', remplissage= 'green', epaisseur=5, tag='rectangle_possib_1')
                                fltk.texte(145, 613, f'{lst[1][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                fltk.texte(255, 613, f'{lst[1][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                wrongline_split=True
                            lst_splice[1]=True
                            end=True
                jsp=criteras[0] and wrongline_split
                if jsp==False:
                    fltk.rectangle(100, 580, 190, 650, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                    fltk.rectangle(210, 580, 300, 650, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                    fltk.texte(145, 613, f'{lst[1][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                    fltk.texte(255, 613, f'{lst[1][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                    lst_splice[1]=True
                    end=True
        if end==False:
            if criteras[0]==True:
                if criteras[2]==2:
                    fltk.rectangle(100, 580, 300, 650, couleur='black', remplissage= 'green' , epaisseur=5, tag='rectangle_possib_1')
                    wrongline_normal=True
            jsp=criteras[0] and wrongline_normal
            if jsp==False:       
                fltk.rectangle(100, 580, 300, 650, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
            if uno==True:
                fltk.texte(200, 613, f'{lst[1][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
            else:
                fltk.texte(200, 613, f'{lst[1][0]}  -  {lst[1][1]}', taille = 30, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                
                
    #ETAPE 3
    end=False
    wrongline_split=False
    wrongline_normal=False
    uno=False
    zero=False
    if len(lst[2])==0:
        fltk.rectangle(100, 480, 300, 550, couleur='black', remplissage='red', epaisseur=5, tag='rectangle_possib_1')
        fltk.texte(200, 513, 'x', taille = 30, ancrage = 'center', police='impact', tag = 'texte_possib_1')
        lst_pablo.append(False)
        zero=True
    elif len(lst[2])==1:
        uno=True     
    if zero==False:
        lst_pablo.append(True)
        if nb_pions==1:
            bernardo=False
            for elt in lst[2]:
                if elt in lst_pions:
                    bernardo=True
            if bernardo==False:
                if criteras[0]==True:
                    if criteras[2]==3:
                        if criteras[3]==True:
                            if criteras[4]==1:
                                fltk.rectangle(100, 480, 190, 550, couleur='black', remplissage= 'green' , epaisseur=5, tag='rectangle_possib_1')
                                fltk.rectangle(210, 480, 300, 550, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                                fltk.texte(145, 513, f'{lst[2][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                fltk.texte(255, 513, f'{lst[2][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                wrongline_split=True
                            elif criteras[4]==2:
                                fltk.rectangle(100, 480, 190, 550, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                                fltk.rectangle(210, 480, 300, 550, couleur='black', remplissage= 'green' , epaisseur=5, tag='rectangle_possib_1')
                                fltk.texte(145, 513, f'{lst[2][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                fltk.texte(255, 513, f'{lst[2][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                                wrongline_split=True
                            lst_splice[2]=True
                            end=True
                jsp= criteras[0] and wrongline_split
                if jsp==False:
                    fltk.rectangle(100, 480, 190, 550, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                    fltk.rectangle(210, 480, 300, 550, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
                    fltk.texte(145, 513, f'{lst[2][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                    fltk.texte(255, 513, f'{lst[2][1]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
                    lst_splice[2]=True
                    end=True
        if end==False:
            if criteras[0]==True:
                if criteras[2]==3:
                    fltk.rectangle(100, 480, 300, 550, couleur='black', remplissage= 'green', epaisseur=5, tag='rectangle_possib_1')
                    wrongline_normal=True
            jsp=criteras[0] and wrongline_normal
            if jsp==False:        
                fltk.rectangle(100, 480, 300, 550, couleur='black', remplissage='white', epaisseur=5, tag='rectangle_possib_1')
            if uno==True:
                fltk.texte(200, 513, f'{lst[2][0]}', taille = 35, ancrage = 'center', police='impact', tag = 'texte_possib_1')
            else:
                fltk.texte(200, 513, f'{lst[2][0]}  -  {lst[2][1]}', taille = 30, ancrage = 'center', police='impact', tag = 'texte_possib_1')
    
    return lst_pablo
            
                        
def bloc_tour(couleur):
    fltk.rectangle(20, 20, 380, 130, couleur='black', remplissage='gray', epaisseur=10, tag='rectangle_tour')
    fltk.texte(145, 73, 'AU TOUR DE', taille = 30, ancrage = 'center', police='impact', tag = 'texte_tour')
    fltk.efface('couleur_tour')
    fltk.cercle(305, 75, 40, remplissage=f'{couleur}', epaisseur=1, tag='couleur_tour')
        
        
def les_des_sur_lecran(lst_des):
    fltk.efface('de_tour')
    fltk.rectangle(30, 780, 100, 850, couleur='black', remplissage='white', epaisseur=7, tag='de_tour')
    fltk.rectangle(120, 780, 190, 850, couleur='black', remplissage='white', epaisseur=7, tag='de_tour')
    fltk.rectangle(210, 780, 280, 850, couleur='black', remplissage='white', epaisseur=7, tag='de_tour')
    fltk.rectangle(300, 780, 370, 850, couleur='black', remplissage='white', epaisseur=7, tag='de_tour')
    fltk.image(65, 815, f'dice_{lst_des[0]}.png', largeur=57, hauteur=57, ancrage='center', tag='de_tour')
    fltk.image(155, 815, f'dice_{lst_des[1]}.png', largeur=57, hauteur=57, ancrage='center', tag='de_tour')
    fltk.image(245, 815, f'dice_{lst_des[2]}.png', largeur=57, hauteur=57, ancrage='center', tag='de_tour')
    fltk.image(335, 815, f'dice_{lst_des[3]}.png', largeur=57, hauteur=57, ancrage='center', tag='de_tour')
    
    
def bloc_continuer_cours(lst):
    pablo=0
    factor=None
    for lst_sub in lst:
        if len(lst_sub)==0:
            pablo+=1        
    if pablo<3:
        fltk.rectangle(20, 880, 380, 980, couleur='black', remplissage='green', epaisseur=10, tag='continuer_tour')
        fltk.texte(200, 933, 'VOUS POUVEZ BOUGER!', taille = 24, ancrage = 'center', police='impact', tag = 'continuer_tour')
        factor=True
    if pablo==3:
        fltk.rectangle(20, 880, 380, 980, couleur='black', remplissage='red', epaisseur=10, tag='continuer_tour')
        fltk.texte(200, 933, 'FF', taille = 35, ancrage = 'center', police='impact', tag = 'continuer_tour')
        factor=False
    return factor


def actualise_pions(joueur, couleurs_joueurs, lst_scores):
    fltk.efface('pion_tour')
    i=2
    for jsp in range(11):
        fltk.efface(f'pion_joueur_{joueur}_ligne_{i}')
        i+=1
    i=0
    for elt in lst_scores[joueur]:
        if elt!=0:
            fltk.cercle(530+100*i, 955-(75*(lst_scores[joueur][i]-1)), 25 , remplissage=couleurs_joueurs[joueur], epaisseur = 1.5 , tag = f'pion_joueur_{joueur}_ligne_{i+2}')
        i+=1


def bloc_continuer_fin(continuer, joueur, couleurs_joueurs, lst_scores, score_neutral, lignes_finies, lst_scores_finaux):
    if continuer==True:
        fltk.efface('continuer_tour')
        fltk.rectangle(20, 880, 180, 980, couleur='black', remplissage='green', epaisseur=10, tag='continuer_tour_2')
        fltk.rectangle(220, 880, 380, 980, couleur='black', remplissage='red', epaisseur=10, tag='continuer_tour_2')
        fltk.texte(100, 933, 'CONTINUER', taille = 20, ancrage = 'center', police='impact', tag = 'continuer_tour_2')
        fltk.texte(300, 933, 'ARRETER', taille = 20, ancrage = 'center', police='impact', tag = 'continuer_tour_2')
        yes = True
        while yes:
            ev = fltk.attend_ev()
            type_ev = fltk.type_ev(ev)
            if type_ev == "ClicGauche" :
                x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                if x > 20 and x < 180 and y > 880 and y < 980:
                    fltk.efface('continuer_tour_2')
                    return True
                    
                if x > 220 and x < 380 and y > 880 and y < 980:
                    i=0
                    for elt in score_neutral:
                        if elt!=0:  
                            lst_scores[joueur][i]+=score_neutral[i]
                        i+=1
                    
                    lst_wincon = wincon(joueur, lst_scores, couleurs_joueurs)
                    
                    colorie_les_lignes(lst_wincon, lignes_finies, lst_scores_finaux, lst_scores)
                    
                    fltk.efface('continuer_tour_2')
                    actualise_pions(joueur, couleurs_joueurs, lst_scores)
                    return False            
    if continuer==False:
        yes = True
        while yes:
            ev = fltk.attend_ev()
            type_ev = fltk.type_ev(ev)
            if type_ev == "ClicGauche" :
                x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                if x > 15 and x < 385 and y > 875 and y <985:
                    fltk.efface('continuer_tour')
                    fltk.efface('pion_tour')
                    return False
#---------fonction-des-blocs-----------
    
#---------options---------
def options_tour(lst, lst_pablo, score_neutral, nb_pions, lst_splice, lst_pions, score_joueurs, joueur_actif):
    yes = True
    while yes:
        ev = fltk.attend_ev()
        type_ev = fltk.type_ev(ev)
        if type_ev == "ClicGauche" :
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
            if lst_splice[2]==True:
                if x > 100 and x < 190 and y > 480 and y < 550:
                    if lst_pablo[2]==True:
                        blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 3, True, 1])#la fonction est toute neuve ça marche nickel (?)
                        nb_pions=avancer_colonne(lst, 2, score_neutral, True, 0, lst_pions, nb_pions, score_joueurs, joueur_actif)
                        return nb_pions
                if x > 210 and x < 300 and y > 480 and y < 550:
                    if lst_pablo[2]==True:
                        blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 3, True, 2])
                        nb_pions=avancer_colonne(lst, 2, score_neutral, True, 1, lst_pions, nb_pions, score_joueurs, joueur_actif)
                        return nb_pions
            if x > 100 and x < 300 and y > 480 and y < 550:
                if lst_pablo[2]==True:
                    blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 3, False, None])
                    nb_pions=avancer_colonne(lst, 2, score_neutral, False, None, lst_pions, nb_pions, score_joueurs, joueur_actif)
                    return nb_pions
                    
            if lst_splice[1]==True:
                if x > 100 and x < 190 and y > 580 and y < 650:
                    if lst_pablo[1]==True:
                        blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 2, True, 1])
                        nb_pions=avancer_colonne(lst, 1, score_neutral, True, 0, lst_pions, nb_pions, score_joueurs, joueur_actif)
                        return nb_pions
                if x > 210 and x < 300 and y > 580 and y < 650:
                    if lst_pablo[1]==True:
                        blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 2, True, 2])
                        nb_pions=avancer_colonne(lst, 1, score_neutral, True, 1, lst_pions, nb_pions, score_joueurs, joueur_actif)
                        return nb_pions   
            if x > 100 and x < 300 and y > 580 and y < 650:
                if lst_pablo[1]==True:
                    blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 2, False, None])
                    nb_pions=avancer_colonne(lst, 1, score_neutral, False, None, lst_pions, nb_pions, score_joueurs, joueur_actif)
                    return nb_pions
                
            if lst_splice[0]==True:
                if x > 100 and x < 190 and y > 680 and y < 750:
                    if lst_pablo[0]==True:
                        blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 1, True, 1])
                        nb_pions=avancer_colonne(lst, 0, score_neutral, True, 0, lst_pions, nb_pions, score_joueurs, joueur_actif)
                        return nb_pions
                if x > 210 and x < 300 and y > 680 and y < 750:
                    if lst_pablo[0]==True:
                        blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 1, True, 2])
                        nb_pions=avancer_colonne(lst, 0, score_neutral, True, 1, lst_pions, nb_pions, score_joueurs, joueur_actif)
                        return nb_pions
            if x > 100 and x < 300 and y > 680 and y < 750:
                if lst_pablo[0]==True:
                    blocs_possib(lst, nb_pions, lst_splice, lst_pions, [True, "green", 1, False, None])
                    nb_pions=avancer_colonne(lst, 0, score_neutral, False, None, lst_pions, nb_pions, score_joueurs, joueur_actif)
                    return nb_pions


def avancer_colonne(possib, div, score_neutral, split, nb_split, lst_pions, nb_pions, score_joueurs, joueur_actif):
    fltk.efface('pion_tour')
    breaker=False
    if len(possib[div])==2:
        if split==True:
            score_neutral[(possib[div][nb_split])-2]+=1
            deja=False
            if len(lst_pions)==0:
                lst_pions.append(possib[div][nb_split])
                nb_pions-=1
            else:
                for elt in lst_pions:
                    if elt==possib[div][nb_split]:
                        deja=True
                if deja==False:
                    lst_pions.append(possib[div][nb_split])
                    nb_pions-=1
                    
        else:
            score_neutral[(possib[div][0])-2]+=1
            score_neutral[(possib[div][1])-2]+=1

            deja=False
            if len(lst_pions)==0:
                lst_pions.append(possib[div][0])
                nb_pions-=1
            else:
                for elt in lst_pions:
                    if elt==possib[div][0]:
                        deja=True
                if deja==False:
                    lst_pions.append(possib[div][0])
                    nb_pions-=1
                
            deja=False
            if len(lst_pions)==0:
                lst_pions.append(possib[div][1])
                nb_pions-=1            
            else:
                for elt in lst_pions:
                    if elt==possib[div][1]:
                        deja=True
                if deja==False:
                    lst_pions.append(possib[div][1])
                    nb_pions-=1
            
    else:
        score_neutral[(possib[div][0])-2]+=1            
    
    i=0
    for elt in score_neutral:
        if elt != 0:
            fltk.cercle(525+100*i, (950-75*score_neutral[i]+75)-(75*score_joueurs[joueur_actif][i]), 25 , remplissage ='black', epaisseur = 1.5 , tag = 'pion_tour')
        i+=1
    
    return nb_pions
        

def lock_des_lignes(score_neutral, joueur, lst_score, lignes_lock):
    terminade=False
    i=3
    indice=2
    for elt in score_neutral:
        if elt>0:
            truc=(lst_scores[joueur][indice-2])+elt
            if truc>=i:
                if indice not in lignes_lock:
                    lignes_lock.append(indice)
            if i==13:
                terminade=True
            if terminade==False:
                i+=2
            else:
                i-=2
        indice+=1



def wincon(joueur, lst_scores, lst_couleurs):
    lignes_finies=[]
    terminade=False
    i=3
    indice=2
    for elt in lst_scores[joueur]:
        if elt>=i:
            lignes_finies.append([indice, i])
        if i==13:
            terminade=True
        if terminade==False:
            i+=2
        else:
            i-=2
        indice+=1
    return [lignes_finies, joueur, lst_couleurs[joueur]]



def colorie_les_lignes(para, lignes_finies, lst_scores_finaux, lst_scores):
    if len(para[0])>0:
        pedro=0
        for elt in para[0]:
            if para[0][pedro][0] not in lignes_finies:
                ijoueur=0
                for jsptrop in range(len(lst_scores)):
                    fltk.efface(f'pion_joueur_{ijoueur}_ligne_{para[0][pedro][0]}')
                    ijoueur+=1
                i=0
                for jsp in range(para[0][pedro][1]):
                    fltk.cercle(530+100*((para[0][pedro][0])-2), 955-75*i, 25 , remplissage=para[2], epaisseur = 1.5 , tag = 'pion_fini')
                    i+=1
                lignes_finies.append(elt[0])
                lst_scores_finaux[para[1]]+=1
                
                for joueur in lst_scores:
                    lst_scores[para[0][pedro][0]]=0
            pedro+=1


#---------options---------

#---------fonction joueurs-----------
def liste_des_joueurs(lst_scores_finaux):
    lst_joueurs=[]
    nb=int(input("Combien de joueurs ? :"))
    lst_joueurs.append(0)
    lst_joueurs.append(1)
    lst_scores_finaux.append(0)
    lst_scores_finaux.append(0)
    if nb>=3:
        lst_joueurs.append(2)
        lst_scores_finaux.append(0)
    if nb==4:
        lst_joueurs.append(3)
        lst_scores_finaux.append(0)
    return lst_joueurs


def liste_des_couleurs(nb):
    lst_couleurs=[]
    lst_couleurs.append('orange')
    lst_couleurs.append('purple')
    if nb>=3:
        lst_couleurs.append('blue')
    if nb==4:
        lst_couleurs.append('green')
    return lst_couleurs
    

def score_joueurs(nb_joueurs):
    lst_scores=[]
    lst_scores.append([0,0,0,0,0,0,0,0,0,0,0])
    lst_scores.append([0,0,0,0,0,0,0,0,0,0,0])
    if nb_joueurs>=3:
        lst_scores.append([0,0,0,0,0,0,0,0,0,0,0])
    if nb_joueurs==4:
        lst_scores.append([0,0,0,0,0,0,0,0,0,0,0])
    return lst_scores
#---------fonction joueurs-----------        

##########---------MAIN--------##########

#--------constantes---------
largeur=1600
hauteur=1000
lst_init=[0,0,0,0]
lst_scores_finaux=[]
joueur_gagnant=None

finir=False
lignes_lock=[]
lignes_finies=[]
score_neutral=[0,0,0,0,0,0,0,0,0,0,0]
#--------constantes---------

n_j_a=0
lst_joueurs=liste_des_joueurs(lst_scores_finaux)
couleurs_joueurs=liste_des_couleurs(len(lst_joueurs))
lst_scores=score_joueurs(len(lst_joueurs))

fltk.cree_fenetre(largeur,hauteur)
fltk.image(800, 500, 'align2.png', largeur=2000, hauteur=1250, tag='align')
#fltk.repere(50)
init_colonnes()


while finir==False:
    if n_j_a >= len(lst_joueurs):
        n_j_a=0
        
    joueur_actif=lst_joueurs[n_j_a]
    couleur_active=couleurs_joueurs[joueur_actif]
    bloc_tour(couleurs_joueurs[joueur_actif])
    n_j_a+=1
    continuer=True
    lst_lock=[]
    lignes_lock=[]
    
    #actualisation en fonction des lignes déjà finies
    for i in lignes_finies:
        if i not in lst_lock:
            lst_lock.append(i)

    lst_pions=[]
    nb_pions=3
    dejafait=False
    lst_splice=[False, False, False]
    score_neutral=[0,0,0,0,0,0,0,0,0,0,0]
    while continuer==True:   
        des_tour=lancer_des()
        les_des_sur_lecran(des_tour)
        print(des_tour)
        possibilites=lst_possib(des_tour)
        print(possibilites)
        
        #actualisation pendant une manche si le mec est monté trop haut
        lock_des_lignes(score_neutral, joueur_actif, lst_scores, lignes_lock)
        for i in lignes_lock:
            if i not in lst_lock:
                lst_lock.append(i)
                
        if nb_pions==0:
            if dejafait==False:
                actuellement_en_larmes(lst_lock, lst_pions)
                dejafait=True

        i=0
        for jsp in range(2):
            for lst in possibilites:
                i2=0
                for elt in lst:
                    if elt in lst_lock:
                        lst.remove(possibilites[i][i2])
                    i2+=1
                i+=1
            i=0
            i2=0
        print(possibilites)
        print(lst_lock)

        lst_pablo=blocs_possib(possibilites, nb_pions, lst_splice, lst_pions, [False, "white", None, None, None])
        print(lst_pablo)
        
        faut_il_continuer=bloc_continuer_cours(possibilites)
        if faut_il_continuer==True:
            nb_pions=options_tour(possibilites, lst_pablo, score_neutral, nb_pions, lst_splice, lst_pions, lst_scores, joueur_actif)
            success=True
        else:
            success=False


        print(score_neutral)
        print(nb_pions)
        print(lst_pions)
        continuer=bloc_continuer_fin(success, joueur_actif, couleurs_joueurs, lst_scores, score_neutral, lignes_finies, lst_scores_finaux)
        
        if continuer==False:
            i=0
            for elt in lst_scores_finaux:
                if elt>=3:
                    joueur_gagnant=i
                    finir=True
                i+=1

print(f'LA PARTIE EST FINIE! LE GAGNANT EST {couleurs_joueurs[joueur_gagnant]} !!!!')
            
        
    
    
    
    
    
    
    

      

                

    











