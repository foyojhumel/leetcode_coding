# First solution
#  nested for loop
# Execution time = 420ms, Memory size = 17.2mb
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #to contain the substring
        countlist = []
        #immediately return the length if list is 1
        if len(s) < 2:
            return len(s)
        else:
            #loop through the list
            for i in range(len(s)):
                count = 0
                for j in range(i+1, len(s)):
                    #checks if the current letter is in the preceeding
                    # substring
                    if s[j] in s[i:j]:
                        countlist.append(j - i)
                        break
                    else:
                        count = len(s[i:j+1])
                #add the substring count to count list
                countlist.append(count)

            return max(countlist)