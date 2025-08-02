class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        - init vars: set, pointers and result (because of immutability and window model)
        - loop through string utilizing right pointer
        - if it's duplicate, shrink window by removing left element from charset and update left element from string
        - if not duplicate, add right pointer to charset and update result with max(past window, current window)
        '''
        # initialize set, left pointer and result
        charSet = set()
        left = 0
        result = 0

        # right pointer to go through every char
        for right in range(len(s)):
            while s[right] in charSet: # while right pointer is a duplicate, remove left pointer and update it.
                charSet.remove(s[left]) 
                left += 1
            charSet.add(s[right]) # add the right pointer to the set
            result = max(result, right - left + 1) # get the result (window stored before or current window)
        return result