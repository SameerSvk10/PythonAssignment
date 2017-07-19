# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:11:22 2017

@author: Sameer
"""

"""
In this program, the number whose factors are to be found is taken from user.
In the function factorisation(n), we use a for loop to iterate from 2(not 1 as we
want factors which are greater than 1)  to square root of that number plus one,
and only append it to the factors list if, it perfectly divides our number. 
If the length of the list containing factors is not greater than one,it implies
that the entered number is a prime number.
"""
def factorisation(n):
    factors= set()
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n/i))
    return factors
    
factors_out=factorisation(int(raw_input("Enter an integer whose factors are to be generated:")))

if len(factors_out)>1:
    print "Factors of entered number are:",sorted(factors_out)
else:
    print "The Entered number is a prime number"
