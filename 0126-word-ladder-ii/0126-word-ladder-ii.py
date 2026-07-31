from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        # Step 1: BFS to build a "parents" map — parents[word] = set of words
        # that can reach `word` in one valid step on some shortest path
        layer = {beginWord}
        parents = defaultdict(set)
        word_set.discard(beginWord)
        found = False
        
        while layer and not found:
            next_layer = defaultdict(set)
            
            for word in layer:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in word_set:
                            next_layer[new_word].add(word)
            
            # Remove this layer's words from word_set so we never revisit
            # them (ensures each word's shortest distance is fixed)
            for word in next_layer:
                if word == endWord:
                    found = True
                parents[word] |= next_layer[word]
            
            word_set -= set(next_layer.keys())
            layer = set(next_layer.keys())
        
        if not found:
            return []
        
        # Step 2: backtrack from endWord to beginWord using the parents map
        result = []
        path = [endWord]
        
        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()
        
        backtrack(endWord)
        return result