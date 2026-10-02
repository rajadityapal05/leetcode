class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = [
            "", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n: int) -> str:
            if n == 0:
                return ""

            if n < 20:
                return below_20[n]

            if n < 100:
                return tens[n // 10] + (
                    " " + below_20[n % 10] if n % 10 else ""
                )

            return (
                below_20[n // 100]
                + " Hundred"
                + (" " + convert(n % 100) if n % 100 else "")
            )

        result = []

        groups = [
            (10**9, "Billion"),
            (10**6, "Million"),
            (10**3, "Thousand")
        ]

        for value, word in groups:
            if num >= value:
                result.append(convert(num // value))
                result.append(word)
                num %= value

        if num:
            result.append(convert(num))

        return " ".join(result)