from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        - create Dict to store values/indexes
        - iterate through list using enumerate
        - compute the targetNumber (number that add with current number in iterator == target)
        - if targetNumber in dict, return list
        - if not, assign the key & value in dict

        [2,7,11,15]   target = 9

        k  , v
        {2 : 0,
         7 : 1
        }
        '''

        # init hashMap
        hashMap = defaultdict(int)

        for i, number in enumerate(nums):
            targetNumber = target - number

            if targetNumber in hashMap:
                return [hashMap[targetNumber], i]

            hashMap[number] = i
        
