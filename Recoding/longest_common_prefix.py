def longestCommonPrefix(strs: list[str]) -> str:
    first_check = ""
    final_check = ""
    n = len(strs)
    for i in range(n):
        new = n[i]
        for j in range(i,n):
            if j[i] == new:
                final_check += final_check + new
    return final_check

print(longestCommonPrefix(["flower","flow","flight"]))