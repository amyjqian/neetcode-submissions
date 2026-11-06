import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        operators = {"+", "-", "*", "/"}
        stack = []


        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if token == "+":
                    stack.append(val2 + val1)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val2 * val1)
                elif token == "/":
                    stack.append(math.trunc(val2 / val1))
                else:
                    print("oh no!!!!")
        return stack.pop()
