class Solution:
    def isSolvable(self, words, result):
        chars = set("".join(words) + result)

        if len(chars) > 10:
            return False

        # A single-letter word/result may be 0.
        # Multi-letter numbers cannot start with 0.
        leading = set()

        for word in words:
            if len(word) > 1:
                leading.add(word[0])

        if len(result) > 1:
            leading.add(result[0])

        max_len = max(
            max(len(word) for word in words),
            len(result)
        )

        mapping = {}
        used = [False] * 10

        def dfs(col, row, total):
            # Processed every column
            if col == max_len:
                return total == 0

            # Process all words for this column
            if row < len(words):
                word = words[row]

                # This word has no character in this column
                if col >= len(word):
                    return dfs(col, row + 1, total)

                ch = word[-1 - col]

                # Already assigned
                if ch in mapping:
                    return dfs(
                        col,
                        row + 1,
                        total + mapping[ch]
                    )

                # Try every unused digit
                for digit in range(10):
                    if used[digit]:
                        continue

                    if digit == 0 and ch in leading:
                        continue

                    mapping[ch] = digit
                    used[digit] = True

                    if dfs(
                        col,
                        row + 1,
                        total + digit
                    ):
                        return True

                    del mapping[ch]
                    used[digit] = False

                return False

            # All words processed.
            # Now process the result character.
            if col >= len(result):
                # Result has no digit in this column.
                # Therefore the column total must be 0.
                return total == 0 and dfs(col + 1, 0, 0)

            ch = result[-1 - col]

            digit = total % 10
            carry = total // 10

            # Result character already assigned
            if ch in mapping:
                if mapping[ch] != digit:
                    return False

                return dfs(col + 1, 0, carry)

            # Result character is unassigned
            if used[digit]:
                return False

            if digit == 0 and ch in leading:
                return False

            mapping[ch] = digit
            used[digit] = True

            if dfs(col + 1, 0, carry):
                return True

            del mapping[ch]
            used[digit] = False

            return False

        return dfs(0, 0, 0)