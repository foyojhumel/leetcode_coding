# First solution
#  dumb day, cheating because of using sorted method in python
# Execution time = 79ms, Memory size = 17.1mb
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numlist = sorted(nums1 + nums2)
        median = int(len(numlist) / 2)
        if len(numlist) == 0:
            return 0.00000
        elif len(numlist) % 2 == 0:
            return float(f"{((numlist[median - 1] + numlist[median]) / 2):.5f}")
        else:
            return float(f"{numlist[int((len(numlist) - 1) / 2)]:.5f}")