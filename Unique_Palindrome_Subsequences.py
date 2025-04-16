
def getUnqiuqPalindromeSubsequences(s : str) -> int:
    
    left = 0
    palindrome = ""
    counts = 0

    for right in range(1, len(s)+1):
        palindrome = s[left:right]
        if palindrome == palindrome[::-1]:
            counts += 1
        else:
            left = right - 1
            palindrome = s[left:right]
            if palindrome == palindrome[::-1]:
                counts += 1
    
    return counts

# Test cases
print( getUnqiuqPalindromeSubsequences("a") )
print( getUnqiuqPalindromeSubsequences("") )
print( getUnqiuqPalindromeSubsequences("aab") )
