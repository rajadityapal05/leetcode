class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    # Need to insert '(' before this ')'
                    additions += 1

        # Any unmatched '(' needs a ')'
        return additions + balance