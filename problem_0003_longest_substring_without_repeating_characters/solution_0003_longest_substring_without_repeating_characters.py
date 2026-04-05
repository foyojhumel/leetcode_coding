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

# Second solution
#  no nested for loop, but a much more longer execution time with while loop
# Execution time = 1685ms, Memory size = 19.5mb
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #the goal is to return the longest chain of non-repeating characters
        #the possible longest will be 26, the count of English alphabets
        #there are many possible chain of non-repeating characters, we are
        # only to return the maximum count

        #if list contains one or no character, return its length
        if (len(s) < 2):
            return len(s)

        #count the letters seen during check of all letters in the string
        letter_count = 0

        #remember the longest count seen so far
        lengthiest = 0

        #count of step up to end of string
        count = 1

        #continuous check while not seeing the whole string
        while ((count != len(s)) and (lengthiest < len(s[letter_count:]))):
            #check if the current letter is in the preceeding substring
            if s[count] not in s[letter_count:count]:
                count += 1
                if (count == len(s)):
                    return len(s[letter_count:])
            else:
                #if repeating character is found in the substring, compute the
                # length
                current_length = count - letter_count
                if current_length > lengthiest:
                    lengthiest = current_length
                #add the count value to letter_count, to track the number of
                # letters seen
                letter_count += 1
                count = letter_count + 1
        
        return lengthiest