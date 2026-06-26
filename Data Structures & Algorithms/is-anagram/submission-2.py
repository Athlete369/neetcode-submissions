class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False
        s_hash_set = [0] * 26
        t_hash_set = [0] * 26

        for i in range(0, n):
            s_hash_set[ord(s[i]) - 97] +=1
            t_hash_set[ord(t[i]) - 97] += 1

        if s_hash_set == t_hash_set:
            return True
        return False