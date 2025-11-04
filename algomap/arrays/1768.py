"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

def fn(word1, word2):
    r = ""
    l1 = len(word1)
    l2 = len(word2)
    puntero = 0
    if l1 < l2:
        short = word1
        long = word2
    else:
        short = word2
        long = word1
    for i in range(min(l1,l2)):
        puntero = i
        r += (word1[i] + word2[i])
    r += long[puntero+1:len(long)]
    return r

if __name__ == "__main__":
    test1 = ("abc", "pqr")
    test2 = ("ab", "pqrs")
    print(fn(test1[0],test1[1]))
    
