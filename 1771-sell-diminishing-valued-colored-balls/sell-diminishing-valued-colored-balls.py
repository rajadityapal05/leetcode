from typing import List

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        inventory.sort(reverse=True)
        inventory.append(0)

        ans = 0
        colors = 1

        for i in range(len(inventory) - 1):
            high = inventory[i]
            low = inventory[i + 1]

            # Number of balls available from high down to low + 1
            count = (high - low) * colors

            if orders >= count:
                # Sell the entire range
                ans += colors * (high + low + 1) * (high - low) // 2
                orders -= count
            else:
                # We only need part of this range
                full_levels = orders // colors
                remainder = orders % colors

                new_low = high - full_levels

                # Sell full levels: high, high-1, ..., new_low+1
                ans += colors * (high + new_low + 1) * full_levels // 2

                # Sell remaining balls at value new_low
                ans += remainder * new_low

                break

            ans %= MOD
            colors += 1

        return ans % MOD   