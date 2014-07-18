class Solution:
    def anagrams(self, strs):
        anagram_map, res = {}, []
        for str in strs:
            sorted_str = ("").join(sorted(str))
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(str)
            else:
                anagram_map[sorted_str] = [str]
        for anagrams in anagram_map.values():
            if len(anagrams) > 1:
                res += anagrams
        return res

    # def anagrams(self, strs):
    #     """List comprehension may be more elegant but less readable here.
    #     """
    #     anagram_map = {}
    #     for str in strs:
    #         sorted_str = ("").join(sorted(str))
    #         if sorted_str in anagram_map:
    #             anagram_map[sorted_str].append(str)
    #         else:
    #             anagram_map[sorted_str] = [str]
    #     return [anagram for anagrams in anagram_map.values() if len(anagrams) > 1 for anagram in anagrams]