class Solution:
    def anagrams(self, strs):
        map, result = {}, []
        if len(strs) >= 1:
            for str in strs:
                sorted_str = "".join(sorted(str))
                if sorted_str not in map:
                    map[sorted_str] = [str]
                else:
                    map[sorted_str].append(str)
            for word in map:
                if len(map[word]) > 1:
                    result += map[word]
        return result