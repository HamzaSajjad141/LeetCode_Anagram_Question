class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        # Hash Map Technique is used
        # Check if the lengths of the two strings are different
        if len(s) != len(t):
            return False

        # Create dictionaries to store character counts for each string
        Counts = {}  # Dictionary to store character counts for string s
        Countt = {}  # Dictionary to store character counts for string t

        # Iterate through the characters of the strings
        for i in range(len(s)):
            # Increment the count of the current character in the Counts dictionary for string s
            Counts[s[i]] = 1 + Counts.get(s[i], 0)
            # Increment the count of the current character in the Countt dictionary for string t
            Countt[t[i]] = 1 + Countt.get(t[i], 0)  # Corrected the typo here

        # Compare character counts in the Counts dictionary with the Countt dictionary
        for j in Counts:
            if Counts[j] != Countt.get(j, 0):
                return False

        return True

        #other approach this also counts the occurences of each alphabet it can tell the anagram Counter Technique
        Counter(s) == Counter(t)


        #other approach we use sort it can anagram Sorting Technique
        sorted(s) == sorted(t)