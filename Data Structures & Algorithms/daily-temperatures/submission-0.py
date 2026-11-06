class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if we encounter a number that is SMALLER and ANS[0] append 0
        # if we encounter a number that is SMALLER and ANS[] jump there
        # if we encounter a number that is BIGGER  
        ans = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            # print(f"outer loop, i: {i}, temp[i]: {temperatures[i]}")
            while j < len(temperatures):
                # print(f"    inner loop, j: {j}, temp[j]: {temperatures[j]}")
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
                    # print(f"    ans: {ans}")
                    break
                if temperatures[i] >= temperatures[j]:
                    if ans[j] == 0:
                        ans[i] = 0
                        # print(f"    ans: {ans}")
                        break
                    else:
                        j += ans[j]
                        # print(f"    ans: {ans}")
        return ans

        