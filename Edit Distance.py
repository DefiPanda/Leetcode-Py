class Solution:
    def minDistance(self, word1, word2):
        distance = [[i] for i in range(len(word1) + 1)]
        distance[0] = [i for i in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                deletion = distance[i - 1][j] + 1
                addition = distance[i][j - 1] + 1
                substitution = distance[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    substitution += 1
                distance[i].append(min(deletion, addition, substitution))
        return distance[-1][-1]

    def minDistance(self, word1, word2):
        """This is an example of horrible code. Long statement inside the nested for loop 
        is hard to understand.
        """
        distance = [[i] for i in range(len(word1) + 1)]
        distance[0] = [i for i in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                distance[i].append(min(distance[i - 1][j] + 1, distance[i][j - 1] + 1, distance[i - 1][j - 1] + (word1[i - 1] != word2[j - 1])))
        return distance[-1][-1]