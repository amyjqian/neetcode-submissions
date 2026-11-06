
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            s1_freq[index] += 1
        
        s2_freq = [0] * 26
        l = 0
        for r in range(len(s2)):
            if r < len(s1):
                index = ord(s2[r]) - ord('a')
                s2_freq[index] += 1
            else:
                if s1_freq == s2_freq:
                    return True
                index_l = ord(s2[l]) - ord('a')
                s2_freq[index_l] -= 1
                l += 1
                index_r = ord(s2[r]) - ord('a')
                s2_freq[index_r] += 1
        return s1_freq == s2_freq
        
        