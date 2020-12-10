# -*- coding: utf-8 -*-
"""
Created on Thu Dec 8 21:20:29 2020

@author: Harachili
"""

import numpy as np

def matrice_ridotta_scala(A):
    
    #Se la matrice non ha colonne né righe allora è in forma ridotta
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    #Cerco il primo elemento != 0
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        #Se ogni elemento è zero passo alla seconda
        B = matrice_ridotta_scala(A[:,1:])
        #E aggiungo alla fine la colonna di zeri
        return np.hstack([A[:,:1], B])

    # Scambio le righe se lo zero non era nella prima riga
    if i > 0:
        A[i], A[0] = A[0], A[i]

    # Divido la prima riga per l'elemento in posizione 0
    A[0] = A[0] / A[0,0]
    # Sottraggo a tutte le righe successive l'elemento in posizione 0(che è 1) 
    # Moltiplicato per il valore del primo elemento della riga
    A[1:] -= A[0] * A[1:,0:1]

    # Applico ricorsivamente l'algoritmo passando a riga e colonna successivi
    B = matrice_ridotta_scala(A[1:,1:])

    # Riaggiungo la prima riga e la prima colonna e li ritorno
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])

A = np.array([[5,5,5,5,5],
              [5,1,5,5,5],
              [5,5,5,5,5]], dtype='float')

matRidotta = matrice_ridotta_scala(A)
rank = sum([1 for i in matRidotta if sum(i) != 0])
print(matRidotta)
print()
print("Il rango della matrice è:", rank)
