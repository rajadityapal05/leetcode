import math

class Solution:
    def kthSmallestPath(self, destination, k):
        row, col = destination
        result = []

        while row > 0 or col > 0:
            if col > 0:
                # Number of paths if we choose H here
                count = math.comb(row + col - 1, row)

                if k <= count:
                    result.append('H')
                    col -= 1
                else:
                    result.append('V')
                    row -= 1
                    k -= count
            else:
                result.append('V')
                row -= 1

        return ''.join(result)