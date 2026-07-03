class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        - dictionary for all the of s 
        - dictionary for all of t 
        - check if they are same 

        '''

        #initialize the dictionary for s
        dicS = {}
        #initialize the dictionary for t
        dicT = {}

        #transport all of us in DictionaryS
        for letter in s:
            dicS[letter] = s.count(letter)
        
        for letter in t:
            dicT[letter] = t.count(letter)
        
        if dicS == dicT:
            return True
        else: 
            return False
        