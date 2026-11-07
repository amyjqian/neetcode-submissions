class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # optimized space complexity: each entry only depends on prev row 
        
        dp = [0] * (min(len(text1), len(text2)) + 1)
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        for i in range(len(text1) - 1, -1, -1):
            diag = 0
            for j in range(len(text2) - 1, -1, -1):
                below = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + diag
                else:
                    dp[j] = max(dp[j + 1], below)
                diag = below
        
        
        return dp[0]






        # time complexity: O(m*n)
        # space complexity: O(m*n)
        # dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) -1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        #         # print(dp)
        # return dp[0][0]

        
        
        