"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence 
of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""

def fn(s,t):
    index = len(s)
    conteo = 0
    if index == 0:
        return True
    for i in t:
        if s[conteo] == i:
            conteo += 1
        if conteo == index:
            return True
    return True if conteo == index else False

if __name__ == "__main__":
    test1 = ("abd", "ahbgdc")
    test3 = ("axc", "ahbgdc")
    print(fn(test3[0], test3[1]))