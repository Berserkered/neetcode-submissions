class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                openStack.append(s[i])
            if s[i] == "]" or s[i] == "}" or s[i] == ")":
                if not openStack or openStack.pop() != mapping[s[i]]:
                    return False
        if len(openStack) == 0:
            return True
        else:
            return False
