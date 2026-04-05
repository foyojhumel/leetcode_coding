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

# Third solution
#  using a single for loop to look into the string once
# Execution time = 23ms, Memory size = 19.21mb
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #the goal is to return the longest chain of non-repeating characters
        #the possible longest will be 26, the count of English alphabets
        #there are many possible chain of non-repeating characters, we are
        # only to return the maximum count

        #if list contains one or no character, return its length
        if (len(s) < 2):
            return len(s)

        #stores the sub_string
        sub_string = []

        #track of sub_string count every time a repeating character is found
        length = 0

        #look into the given string once
        for i in range(len(s)):
            #if current letter is present in the sub_string
            if (s[i] in sub_string):
                #find the index of the same character in the substring
                same_char_index = sub_string.index(s[i])
                #slice the substring
                sub_string = sub_string[same_char_index+1:]
            #add the letter at the end of substring
            sub_string.append(s[i])
            
            #set length to what is larger in length, the current length or
            # length of substring
            length = max(length, len(sub_string))

        return length

# Fourth solution
#  no initialized empty list to hold the sliced string.
#  NOTE! surprisingly, this does not improve the memory size only the execution time
# Execution time = 14ms, Memory size = 19.2mb
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #the goal is to return the longest chain of non-repeating characters
        #the possible longest will be 26, the count of English alphabets
        #there are many possible chain of non-repeating characters, we are
        # only to return the maximum count

        #if list contains one or no character, return its length
        if (len(s) < 2):
            return len(s)

        #sliding index, initially set to 0
        sliding_index = 0

        #track of sub_string count every time a repeating character is found
        length = 0

        for i in range(len(s)):
            #if character is found in the substring
            if (s[i] in s[sliding_index:i]):
                #get the index of same character
                same_char_index = s[sliding_index:i].index(s[i])
                #move sliding_index to the index of same character
                #move one more position to for new substring of sliced list
                sliding_index = sliding_index + same_char_index + 1
            
            #find the length of substring for each iteration
            length = max(length, len(s[sliding_index:i+1]))

        return length