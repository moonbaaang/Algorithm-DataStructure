# 회문 (palindrome) (뒤집어도 같은 문장)
from typing import List
def isPalindrome(s : str) -> bool:
    i = 0
    j = len(s) - 1

    s = s.lower()

    while i<j:
        while i<j:
            if s[i].isalnum():
                break
            i+=1


        while i<j:
            if s[j].isalnum():
                break
            j-=1

        if s[i] != s[j]:
            return False

        i+=1
        j-=1

    return True

print(isPalindrome("abcba"))


# 공백과 특수문자 제거
s = "AbbC, cbb a"
s1 = [ch for ch in s if ch.isalnum()]
word1 = "".join(s1).lower()

s2 = list(filter(str.isalnum, s))
word2 = "".join(s2).lower()


print(word1)
print(word2)

print(isPalindrome(word1))
print(isPalindrome(word2))
