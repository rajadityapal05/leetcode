class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def to_minutes(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m

        start = to_minutes(loginTime)
        end = to_minutes(logoutTime)

        if end < start:
            end += 1440

        start = (start + 14) // 15
        end //= 15

        return max(0, end - start)