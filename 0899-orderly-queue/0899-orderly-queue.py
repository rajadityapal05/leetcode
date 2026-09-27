class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            # Only rotations are possible
            return min(s[i:] + s[:i] for i in range(len(s)))

        # With k >= 2, any permutation can be achieved
        return ''.join(sorted(s)) 