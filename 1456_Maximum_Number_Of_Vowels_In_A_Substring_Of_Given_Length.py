class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        interval =  list(s[:k])
        vowel = ['a', 'e', 'i', 'o', 'u']
        count, max_val = 0, 0

        for i in interval:
            if i in vowel:
                count += 1

        max_val = count

        for i in range(k, len(s)):
            start = interval.pop(0)
            if start in vowel:
                count -= 1
            new = s[i]
            interval.append(new)
            if new in vowel:
                count += 1
            if count > max_val:
                max_val = count

        return max_val


        