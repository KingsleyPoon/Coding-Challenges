'''
CODING CHALLENGE

https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

Given two strings, determine if they share a common substring. A substring may be as small as one character.

Example:
    S1 = "be"
    S2 = "cat"
    
    These share no common substring. Return False

    S1 = "art"
    S2 = "and"
    
    These share the common substring "a". Return True
    
    
'''

def shareSubstring(S1,S2):
    lengthS1 = len(S1)
    lengthS2 = len(S2)
    
    if lengthS1 < lengthS2:
        shorterWord = S1
        longerWord = S2
    else:
        longerWord = S1
        shorterWord = S2
    
    #Loop through different length of substring
    for i in range(len(shorterWord)):
        
        #Loop through each possible substring
        for n in range(1,len(shorterWord) - i):
            
            #if substring present in other string, return True
            if shorterWord[0:n] in longerWord:
                return True
    # Only return false if no examples are given
    return False

S1 = "and"
S2 = "art"

print(shareSubstring(S1,S2))

