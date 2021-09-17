from constantes import *
import pygame
import numpy as np

class Cellule :

    def __init__(self, posX, posY, etat):
        self.posX = posX
        self.posY = posY
        self.nbVoisins = 0
        self.etat = etat

    def voisines(self, tabCellules, nbX, nbY):
        ##print(tabCellules[self.posX][self.posY].etat)
        voisines = 0
        if self.posX+1 < nbX :
            if tabCellules[self.posX+1][self.posY].etat == 1 :
                voisines += 1

        if self.posX-1 >= 0 :
            if tabCellules[self.posX-1][self.posY].etat == 1 :
                voisines += 1

        if self.posY+1 < nbY :
            if tabCellules[self.posX][self.posY+1].etat == 1 :
                voisines += 1

        if self.posY-1 >= 0 :
            if tabCellules[self.posX][self.posY-1].etat == 1 :
                voisines += 1

        if self.posX-1 >= 0 and self.posY-1 >= 0 :
            if tabCellules[self.posX-1][self.posY-1].etat == 1 :
                voisines += 1

        if self.posX+1 < nbX and self.posY+1 < nbY :
            if tabCellules[self.posX+1][self.posY+1].etat == 1 :
                voisines += 1

        if self.posX-1 >= 0 and self.posY+1 < nbY :
            if tabCellules[self.posX-1][self.posY+1].etat == 1 :
                voisines += 1

        if self.posX+1 < nbX and self.posY-1 >= 0 :
            if tabCellules[self.posX+1][self.posY-1].etat == 1 :
                voisines += 1
        self.nbVoisins = voisines

    def verifEtat(self):
        if (self.nbVoisins == 3) or (self.etat == 1 and self.nbVoisins == 2):
            self.etat = 1
        else:
            self.etat = 0

    def afficherCellule(self, fenetre):
        if self.etat == 0:  # morte = BLANC
            pygame.draw.rect(fenetre, BLANC, (self.posX * TAILLECARRE, self.posY * TAILLECARRE, TAILLECARRE, TAILLECARRE), 0)
            pygame.draw.line(fenetre, GRISF, (self.posX * TAILLECARRE, self.posY * TAILLECARRE),
                             (self.posX * TAILLECARRE + TAILLECARRE, self.posY * TAILLECARRE), 1)
            pygame.draw.line(fenetre, GRISF, (self.posX * TAILLECARRE, self.posY * TAILLECARRE),
                             (self.posX * TAILLECARRE, self.posY * TAILLECARRE + TAILLECARRE), 1)
            pygame.draw.line(fenetre, GRISF, (self.posX * TAILLECARRE, self.posY * TAILLECARRE + TAILLECARRE),
                             (self.posX * TAILLECARRE + TAILLECARRE, self.posY * TAILLECARRE + TAILLECARRE), 1)
            pygame.draw.line(fenetre, GRISF, (self.posX * TAILLECARRE + TAILLECARRE, self.posY * TAILLECARRE),
                             (self.posX * TAILLECARRE + TAILLECARRE, self.posY * TAILLECARRE + TAILLECARRE), 1)
        if self.etat == 1:  # vivante = NOIRE
            color = list(np.random.choice(range(256), size=3))
            pygame.draw.rect(fenetre, color, (self.posX * TAILLECARRE, self.posY * TAILLECARRE, TAILLECARRE, TAILLECARRE), 0)
            pygame.draw.line(fenetre, GRISC, (self.posX * TAILLECARRE, self.posY * TAILLECARRE),
                             (self.posX * TAILLECARRE + TAILLECARRE, self.posY * TAILLECARRE), 1)
            pygame.draw.line(fenetre, GRISC, (self.posX * TAILLECARRE, self.posY * TAILLECARRE),
                             (self.posX * TAILLECARRE, self.posY * TAILLECARRE + TAILLECARRE), 1)
            pygame.draw.line(fenetre, GRISC, (self.posX * TAILLECARRE, self.posY * TAILLECARRE + TAILLECARRE),
                             (self.posX * TAILLECARRE + TAILLECARRE, self.posY * TAILLECARRE + TAILLECARRE), 1)
            pygame.draw.line(fenetre, GRISC, (self.posX * TAILLECARRE + TAILLECARRE, self.posY * TAILLECARRE),
                             (self.posX * TAILLECARRE + TAILLECARRE, self.posY * TAILLECARRE + TAILLECARRE), 1)









