class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        hash_map = dict()
        for s in strs:
            tem_list = [0]*26
            for i in s:
                tem_list[ord(i)-ord('a')] += 1
            if str(tem_list) not in hash_map:
                hash_map[str(tem_list)] = []
            hash_map[str(tem_list)].append(s)
        # print(hash_map_map)
        for k, v in hash_map.items():
            anagrams.append(v)
        return anagrams