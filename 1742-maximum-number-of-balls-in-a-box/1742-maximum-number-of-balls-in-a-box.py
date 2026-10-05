class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}

        for num in range(lowLimit, highLimit + 1):
            box = sum(map(int, str(num)))
            boxes[box] = boxes.get(box, 0) + 1

        return max(boxes.values()) 