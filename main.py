import pygame
from Grille import *
from constantes import *
from Cellule import *
import sys
import time


class Jeu:

    def __init__(self):
        self.ecran = pygame.display.set_mode(TAILLEFENETRE)
        pygame.display.set_caption('Jeu de la vie')
        self.jeu_encours = True
        self.grille = Grille(NBCASEX, NBCASEY)
        self.grille.init()
        self.pause = True
        self.saved_grille = Grille(NBCASEX,NBCASEY)
        self.saved_grille.init()


    def boucle_principale(self):
        while self.jeu_encours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.pause :
                            self.pause = False
                            self.saved_grille.copy(self.grille)
                        else:
                            self.pause = True
                    if event.key == pygame.K_ESCAPE:
                        self.grille.clear()
                        self.ecran.fill(BLANC)
                        self.grille.afficherGrille(self.ecran)
                        pygame.display.flip()
                        self.pause = True
                    if event.key == pygame.K_s:
                        self.grille.copy(self.saved_grille)
                if event.type == pygame.MOUSEBUTTONDOWN and self.pause == True:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    if 0 <= x <= NBCASEX*TAILLECARRE and 0 <= y <= NBCASEY*TAILLECARRE:
                        if self.grille.tabCellules[int(x/TAILLECARRE)][int(y/TAILLECARRE)].etat == 1 :
                            self.grille.tabCellules[int(x/TAILLECARRE)][int(y/TAILLECARRE)].etat = 0
                        elif self.grille.tabCellules[int(x/TAILLECARRE)][int(y/TAILLECARRE)].etat == 0 :
                            self.grille.tabCellules[int(x/TAILLECARRE)][int(y/TAILLECARRE)].etat = 1
                        self.grille.verifVoisines()
            if not(self.pause):
                self.grille.verifVoisines()
                self.grille.verifEtats()
                time.sleep(0.5)
            self.ecran.fill(BLANC)
            self.grille.afficherGrille(self.ecran)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()


