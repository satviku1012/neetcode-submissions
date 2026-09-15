class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closed_to_open = {}
        closed_to_open[")"] = "("
        closed_to_open["}"] = "{"
        closed_to_open["]"] = "["

        for bracket in s:
            if bracket in closed_to_open:
                # closing bracket
                if not stack or closed_to_open[bracket] != stack.pop():
                    return False
            else:
                # open bracket
                stack.append(bracket)

        return True
            