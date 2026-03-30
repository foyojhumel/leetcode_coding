# First solution
#  Brute force using nested for loop
#  Execution time = 1727ms, Memory size = 19.6mb
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1+i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Second solution
#  Similar to a nested for loop, but taking advantage of Python's "in"
#   keyword to check forward through the array at each iteration of
#   for loop
#  Execution time = 298ms, Memory size = 19.6mb
def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first iteration in nums list to check all values
        for position, value in enumerate(nums):
            if (target - value) in nums[position+1:]:
                return (nums.index(value), nums.index(target-value,position+1))

# Third solution
#  Using dictionary, similar to a hash table, to look only once in the
#   given array then look into the dictionary for complement at each
#   iteration
#  Execution time = 0ms, Memory size = 20.5mb
def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dictionary to contain all elements and their index in the given
        # list at each loop iteration
        value_index_dict = {}

        #iterate through nums list
        for position, value in enumerate(nums):
            #compute for the target's complement at each value
            complement = target - value

            #check if complement is in the dictionary
            # NOTE: using "in" keyword to a dictionary is faster than
            #  using it to a list
            # NOTE: "in" keyword checks the keys of dictionary by default
            if complement in value_index_dict:
                return (value_index_dict[complement], position)
            
            #if complement is not present in the dictionary, add the current
            # nums value to the dictionary and its position (index)
            value_index_dict[value] = position
        
        return []