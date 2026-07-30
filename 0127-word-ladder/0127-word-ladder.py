from collections import deque
class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)  

        if endWord not in wordset:
            return 0 

        queue = deque()
        queue.append((beginWord, 1))

        level = float("inf")
        atoz = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            word, count = queue.popleft()

            if word == endWord:
                level = min(level, count)
                continue  

            for i in range(len(word)):
                for c in atoz:
                    nword = word[:i] + c + word[i + 1 :]
                    if nword in wordset:
                        queue.append((nword, count + 1))
                        wordset.remove(nword)  

        return 0 if level == float("inf") else level