# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:47:08 2020

@author: Harachili
"""
from numpy import lcm
def symmetricgroup():
    Sn = int(input("Select the degree of the symmetric group: "))
    print(f"\nSymmetric group of degree {Sn}.\n" 
          f"S{Sn} =", "{", str([_ for _ in range(1, Sn + 1)])[1:-1], "}\n")
    return Sn


permutations = []


def permute(array, start=0):
    if start == len(array) - 1:
        permutations.append(list(array))
        return
    for i in range(start, len(array)):
        array[start], array[i] = array[i], array[start]
        permute(array, start + 1)
        array[start], array[i] = array[i], array[start]


def build_array(Sn):
    perm = []
    for i in range(1, Sn + 1):
        n = int(input(f"insert the {i}^ number: "))
        while n in perm or not 0 < n < Sn + 1:
            n = int(input(f"insert the {i}^ number: "))
        perm.append(n)
    print(f"\nYour permutation is: ({str(perm)[1:-1]})")
    return perm

def inverse(arr):
    print("The inverse permutation is: ", [arr.index(i)+1 for i in range(1, len(arr)+1)])

def period(lista):
    lista = disjoint_cycles(lista)
    arr = [len(a) for a in lista]
    print("The period of you permutation is: ", 
          [lcm(i, j) for i, j in zip(arr, arr[1:])][-1])# The lcm of all the values is the period

def disjoint_cycles(perm):
    lung = range(1, len(perm)+1)
    zipped = {a: b for a, b in zip([_ for _ in lung], perm)}
    res = []
    for a in lung:
        if a in zipped:
            b = zipped.pop(a)
        else: # The value is already in a cycle
            continue
        tmp = [a]
        while a != b:
            tmp.append(b)
            b = zipped.pop(b)
        res.append(tmp)
    return res

def parity(perm):
    p   = disjoint_cycles(perm)
    res = sum([len(a)-1 for a in p]) % 2 == 0
    
    if res: print('The permutation is even')
    else: print('The permutation is odd')
    
def calculateAll(arr):
    inverse(arr)
    print("The permutation in disjoint cycles is: ", disjoint_cycles(arr))
    period(arr)
    parity(arr)    
    
if __name__ == "main":
    Sn = symmetricgroup()
    choice = input(
        f"1 ==> Calculate all of the elements of S{Sn}\n"
        f"2 ==> Insert a permutation of S{Sn}\n"
    )
    if choice == "1":
        array = [_ for _ in range(1, int(Sn) + 1)]
        permute(array)
        print(f"The order of the group is: {Sn}! = {len(permutations)}")
        for i in permutations:
            print(i)
    else:
        arr = build_array(Sn)
        info_perm = input("1 ==> calculate the inverse permutation\n"
                          "2 ==> calculate the product in disjoint cycles\n"
                          "3 ==> calculate the period of the permutation\n"
                          "4 ==> calculate the parity of the permutation\n"
                          "5 ==> show it all\n")
        if info_perm == "1":
            inverse(arr)
        elif info_perm == "2":
            print("The permutation in disjoint cycles is: ", disjoint_cycles(arr))
        elif info_perm == "3":
            period(arr)
        elif info_perm == "4":
            parity(arr)
        elif info_perm == "5":
            calculateAll(arr)
            
            
            
            
            
            
            
            
            
            
            