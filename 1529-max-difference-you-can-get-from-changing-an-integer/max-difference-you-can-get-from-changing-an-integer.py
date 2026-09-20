class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Maximum value
        max_s = s
        for digit in s:
            if digit != '9':
                max_s = s.replace(digit, '9')
                break

        # Minimum value
        min_s = s

        if s[0] != '1':
            min_s = s.replace(s[0], '1')
        else:
            for digit in s[1:]:
                if digit not in ('0', '1'):
                    min_s = s.replace(digit, '0')
                    break

        return int(max_s) - int(min_s)