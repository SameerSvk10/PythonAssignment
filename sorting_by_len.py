# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:44:59 2017

@author: Sameer
"""
"""
sorting_list(in_list) function accepts a list of strings which is genereated from
the user input.
sorted() function sorts the in_list by the length of each element(strings) by 
specifying 'key=len'
"""
def sorting_list(in_list):
    return sorted(in_list, key=len)
        
input_list = [x for x in raw_input("Please enter a space-delimited set of Strings:").split()]
sorted_list = sorting_list(input_list)
print sorted_list