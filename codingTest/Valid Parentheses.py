# () -> T
# (){} -> T
# ({}) -> T
# (] -> F

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', '}': '{', ']': '['}

        for char in s:
            if (char in dic.values()):
                stack.append(char)
            elif (char in dic):
                if stack == [] or (stack.pop() != dic[char]):
                    return False
            else:
                return False

        return stack == []