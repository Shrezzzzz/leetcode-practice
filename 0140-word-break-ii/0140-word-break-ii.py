class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]  # base case: empty continuation
            
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Get all valid ways to break the REST of the string
                    for rest in backtrack(end):
                        sentence = word if not rest else word + " " + rest
                        sentences.append(sentence)
            
            memo[start] = sentences
            return sentences
        
        return backtrack(0)