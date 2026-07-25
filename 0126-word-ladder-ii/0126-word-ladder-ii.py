from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # child -> list of parents
        parents = defaultdict(list)

        queue = deque([beginWord])
        visited = set([beginWord])

        found = False

        while queue and not found:
            levelVisited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        newWord = word[:i] + ch + word[i + 1:]

                        if newWord not in wordSet:
                            continue

                        if newWord not in visited:
                            if newWord not in levelVisited:
                                queue.append(newWord)
                                levelVisited.add(newWord)

                            parents[newWord].append(word)

                            if newWord == endWord:
                                found = True

                        elif newWord in levelVisited:
                            # Another shortest parent in the same level
                            parents[newWord].append(word)

            visited.update(levelVisited)

        if not found:
            return []

        ans = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)
        return ans