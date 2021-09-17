from Cellule import *
import pygame

class Grille :

    def __init__(self, nbX, nbY):
        self.tabCellules = []
        self.nbX = nbX
        self.nbY = nbY
        self.tour = 0

    def init(self):
        for i in range(self.nbX):
            self.tabCellules.append([])

        for x in range(self.nbX) :
            for y in range(self.nbY) :
                self.tabCellules[x].append(Cellule(x,y,0))

        for x in range(len(self.tabCellules)) :
            for y in range(len(self.tabCellules[x])) :
                self.tabCellules[x][y].voisines(self.tabCellules, self.nbX, self.nbY)


    def verifEtats(self):
        print("verif etat")
        for x in range(len(self.tabCellules)):
            for y in range(len(self.tabCellules[x])):
                self.tabCellules[x][y].verifEtat()


    def verifVoisines(self):
        print("verif voisine")
        for x in range(len(self.tabCellules)):
            for y in range(len(self.tabCellules[x])):
                self.tabCellules[x][y].voisines(self.tabCellules, self.nbX, self.nbY)


    def afficherGrille(self, fenetre):
        for x in range(len(self.tabCellules)):
            for y in range(len(self.tabCellules[x])):
                self.tabCellules[x][y].afficherCellule(fenetre)

    def clear(self):
        for x in range(len(self.tabCellules)) :
            for y in range(len(self.tabCellules[x])) :
                self.tabCellules[x][y].etat = 0

    def copy(self, grille):
        for x in range(len(self.tabCellules)) :
            for y in range(len(self.tabCellules[x])) :
                self.tabCellules[x][y].etat = grille.tabCellules[x][y].etat