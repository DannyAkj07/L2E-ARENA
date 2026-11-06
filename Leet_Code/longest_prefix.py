def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    first_word = strs[0]
    for i in range(len(first_word)):
        char = first_word[i]
        for s in strs[1:]:
            if i == len(s) or s[i] != char:
                return first_word[:i]

    return first_word

 

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["a"]))