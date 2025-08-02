class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize Hashmap 
        hashMap = defaultdict(int)

        # iterate through nums list and get index (i) and value (number) for them using enumerate
        for i, number in enumerate(nums):
            _targetNumber = target - number # get the number that add with 'number' will sum to target

            # check if _targetNumber exist as a key in hashMap
            if _targetNumber in hashMap:
                return[hashMap[_targetNumber], i] # return the hashMap stored in the previous loop and the current
            
            hashMap[number] = i # assign 'i' as the value for the key 'number'