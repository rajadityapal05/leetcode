
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid, event, timestamp = log.split(":")
            fid = int(fid)
            timestamp = int(timestamp)

            if event == "start":
                if stack:
                    result[stack[-1]] += timestamp - prev_time

                stack.append(fid)
                prev_time = timestamp

            else:
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return result
