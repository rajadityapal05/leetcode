from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:

        count = Counter(s)

        answer = [0] * 10

        # Unique letters
        answer[0] = count['z']
        answer[2] = count['w']
        answer[4] = count['u']
        answer[6] = count['x']
        answer[8] = count['g']

        # Remove letters used by 0
        count['e'] -= answer[0]
        count['r'] -= answer[0]
        count['o'] -= answer[0]

        # Remove letters used by 2
        count['t'] -= answer[2]
        count['w'] -= answer[2]
        count['o'] -= answer[2]

        # Remove letters used by 4
        count['f'] -= answer[4]
        count['o'] -= answer[4]
        count['r'] -= answer[4]

        # Remove letters used by 6
        count['s'] -= answer[6]
        count['i'] -= answer[6]

        # Remove letters used by 8
        count['e'] -= answer[8]
        count['i'] -= answer[8]
        count['h'] -= answer[8]
        count['t'] -= answer[8]

        # Now identify the remaining digits

        # 3 -> three
        answer[3] = count['h']
        count['t'] -= answer[3]
        count['r'] -= answer[3]
        count['e'] -= 2 * answer[3]

        # 5 -> five
        answer[5] = count['f']
        count['i'] -= answer[5]
        count['v'] -= answer[5]
        count['e'] -= answer[5]

        # 7 -> seven
        answer[7] = count['s']
        count['e'] -= 2 * answer[7]
        count['v'] -= answer[7]
        count['n'] -= answer[7]

        # 9 -> nine
        answer[9] = count['i']
        count['n'] -= 2 * answer[9]
        count['e'] -= answer[9]

        # 1 -> one
        answer[1] = count['o']

        result = ""

        for digit in range(10):
            result += str(digit) * answer[digit]

        return result