"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""

def fn(strs):
    if len(strs) == 0:
        return ""
    longest = min([x for x in strs])
    i, j = 0, len(longest)
    for k in range(j):
        for string in strs:
            if j == 0:
                return ""
            if longest[i:j] == string[i:j]:
                continue
            else:
                j -= 1
    return longest[i:j]

        

            
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    print(fn(strs))