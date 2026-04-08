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

# Second solution
#  Using merge sort
# Execution time = 0ms, Memory size = 19.5mb
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #get the total length of nums1 and nums2
        total_nums = len(nums1) + len(nums2)

        if (total_nums % 2 == 0):
            #get the index of median, if total length is even number
            # this is the index of second median
            index_median2 = (total_nums // 2) + 1
        else:
            index_median2 = ((total_nums+1) // 2)

        #initialized variable for pointer to element of nums1 and nums2
        index_nums1 = 0
        index_nums2 = 0

        #to contain the merge sort elements
        merged_order_list = []

        for i in range(index_median2):
            #check if both nums1 and nums2 are not exhausted
            if ((index_nums1 != len(nums1)) and (index_nums2 != len(nums2))):
                #if current element of nums1 is less or equal to current element
                # of nums2
                if (nums1[index_nums1] <= nums2[index_nums2]):
                    #add current element of nums1 to merge sort list
                    merged_order_list.append(nums1[index_nums1])
                    #move the pointer to next element of nums1
                    index_nums1 += 1
                else:
                    merged_order_list.append(nums2[index_nums2])
                    index_nums2 += 1
            #if index_nums1 equals the length of nums1, meaning all nums1 has
            # been search, will look to nums2
            elif (index_nums1 == len(nums1)):
                merged_order_list.append(nums2[index_nums2])
                index_nums2 += 1
            else:
                merged_order_list.append(nums1[index_nums1])
                index_nums1 += 1

        #if total length is odd, return the last element of merge sort list
        if (total_nums % 2 != 0):
            return merged_order_list[index_median2-1]
        #otherwise, return the average of last two element of merge sort list
        else:
            return (merged_order_list[index_median2-1] + merged_order_list[index_median2-2]) / 2