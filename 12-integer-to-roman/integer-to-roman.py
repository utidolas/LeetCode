class Solution:
    def intToRoman(self, num: int) -> str:

        '''
        - 6 cases where a smaller value comes before a bigger: 4-9-40-90-400-900
        - add them in order in our hashmap
        - iterate from bigger to smaller
        - WHILE input value is bigger than our current iteration:
        - subtract from input value (int to be transformed in Roman)
        - after loop, return result
        '''

        result = ""
        romanTranslated = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        # iterate through a list of roman int numbers in descending order
        for number in sorted(romanTranslated.keys(), reverse=True):
            while num >= number: # if the input value is greater than the current number, add the letter corresponding to our current number to the result and subtract the input value
                result += romanTranslated[number]
                num -= number
        return result