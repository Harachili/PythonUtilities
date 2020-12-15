# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:24:00 2020

@author: Harachili
"""
#CALCOLO DETERMINANTE DI UNA MATRICE

scalaMatrice = lambda m, i, j: [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
def trovaDeterminante(m):
    if len(m) == 1: return m[0][0]
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    
    determinante = 0
    for c in range(len(m)):
        segno = (-1)**c
        determinante += segno*m[0][c]*trovaDeterminante(scalaMatrice(m,0,c))
    return determinante