class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        large, small = add
        smal, larg = subtract
        '''
        result = 0
        romanTranslate = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(s)):
            # if there's a letter to check AND the current value is LOWER than the second, subtract
            if i + 1 < len(s) and romanTranslate[s[i]] < romanTranslate[s[i+1]]: 
                result -= romanTranslate[s[i]]
            else:
                result += romanTranslate[s[i]]
        return result