import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations 


def printSubstrings(s):
    """Theory: for string of length n, there are ((n+1) choose 2 == n(n+1)/2) substrings"""
    n = len(s)
    print("Original string: " + s)
    res = [s[x:y] for x, y in combinations(range(n + 1), r = 2)] 
    print("All substrings of string are : " + str(res)) 
    print(f"len(res) = {len(res)} === (n+1) choose 2 = {n*(n+1)//2}\n")
    

def printAnagrams(s):
    """Theory: for string of length n, there are (n choose 2 == n(n-1)/2) anagrams"""
    n = len(s)
    print("Original string: " + s)
    res = [s[x:y] for x, y in combinations(range(n + 1), r = 2)] 
    print("All substrings of string are : " + str(res)) 
    print(f"len(res) = {len(res)} === n choose 2 = {n*(n-1)//2}\n")
    

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    """wo strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

    It must return an integer that represents the number of anagrammatic pairs of substrings in ."""
    counter, len_s = 0, len(s)
    
    print(f"Original string: {s}. length: {len_s}")
    for chunk in range(1, len_s):
        arr = []
        for i in range(0, len_s - chunk + 1):
            ex1 = "".join(s[i:i+chunk])
            ex = "".join(sorted(s[i:i+chunk]))
            print(f"chunk: {chunk}, i: {i}, sub: {ex1}, sub_sorted: {ex}")
            arr.append(ex)

        c = Counter(arr)
        for key in c:
            val = c[key]
            if val > 1:
                counter += (val * (val - 1)) // 2
    
        print(f"chunk: {chunk}, # counter: {counter}, Counter: {str(c)}\n")
    print(f"Result: {counter}.")
    return counter 


if __name__ == '__main__':
    # sherlockAndAnagrams("ifailuhkqq")  # ans: 3
    printSubstrings("abc")
    # q = int(input())

    # for q_itr in range(q):
    #     s = input()

    #     result = sherlockAndAnagrams(s)

    #     print(str(result) + '\n')
