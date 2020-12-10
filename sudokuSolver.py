# -*- coding: utf-8 -*-
"""
Created on Thu Dec 9 21:18:31 2020

@author: Harachili
"""

def numeroPossibile(matrice, y, x, i):
    for n in range(9):
        if matrice[y][n] == i:
            return False
    for n in range(9):
        if matrice[n][x] == i:
            return False
    xx, yy = (x//3)*3, (y//3)*3
    for n in range(3):
        for m in range(3):
            if matrice[yy+n][xx+m] == i:
                return False
    return True
    
    
    
def sudoku(matrice):
    for y in range(9):
        for x in range(9):
            if matrice[y][x] == 0:
                for i in range(1, 10):
                    if numeroPossibile(matrice, y, x, i):
                        matrice[y][x] = i
                        sudoku(matrice)
                        matrice[y][x] = 0
                
                return
    print(matrice)