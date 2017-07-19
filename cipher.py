# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:11:04 2017

@author: Sameer
"""

"""
The function char_equivalent(p,q) accepts two numbers that defines the range.
It iterates through p to q+1 to determine character equivalents of each number.
Then it divides the each number in the range by 26 until we reached a number 
less than 26, takes the remainder each time and adding 65, since 65 is cooresponds
to 'A' in the ASCII table.

"""

def char_equivalent(p,q):
    for i in range(p,(q+1)):
        div=i
        string=""
        while div>0:
            mod=(div-1)%26
            string=chr(65+mod)+string
            div=int((div-mod)/26)
        print string
    return None
    
m, n = [int(x) for x in raw_input("Enter values of m & n here: ").split()]
char_equivalent(m,n)