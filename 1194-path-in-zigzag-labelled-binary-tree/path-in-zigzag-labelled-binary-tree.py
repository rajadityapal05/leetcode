class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        path = []

        while label >= 1:
            path.append(label)

            level = label.bit_length() - 1
            start = 1 << level
            end = (1 << (level + 1)) - 1

            # Convert zigzag label to normal binary-tree label
            label = start + end - label

            # Move to parent
            label //= 2

        return path[::-1]