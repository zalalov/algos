# Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# 
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: ["()"]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        double_n = n * 2
        result = []
        
        self.backtrack(result, '', 0, 0, n)
        
        return result

    def backtrack(self, result, string, opened, closed, n):
        if len(string) == n * 2:
            result.append(string)

        if opened < n: 
            self.backtrack(
                result, 
                string + '(', 
                opened + 1, 
                closed,
                n
            )

        if closed < opened:
            self.backtrack(
                result, 
                string + ')', 
                opened, 
                closed + 1,
                n
            )
