from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - init Hash Map and result
        - loop through each string
        - sort each string so they'll have the same key
        - add the current string to the sorted string
        - iterate through each value in dict 
        - add each value in result list
        '''
        anagramHash = defaultdict(list) # create hashmap of default value of empty list
        result = []

        for string in strs:
            # sort string, add the sortedString as the key of dict and the string as value
            sortedString = tuple(sorted(string))
            anagramHash[sortedString].append(string)
        
        for value in anagramHash.values():
            result.append(value)

        return result