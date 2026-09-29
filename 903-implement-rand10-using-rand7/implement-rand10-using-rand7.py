# The rand7() API is already provided.
# def rand7() -> int:

class Solution:
    def rand10(self):
        while True:
            # Generate a uniform number from 1 to 49
            num = (rand7() - 1) * 7 + rand7()

            # Keep only 1..40
            if num <= 40:
                return (num - 1) % 10 + 1 