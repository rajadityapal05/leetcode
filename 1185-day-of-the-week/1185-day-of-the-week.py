class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ]

        month_days = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        total_days = 0

        # Count complete years from 1971
        for y in range(1971, year):
            if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
                total_days += 366
            else:
                total_days += 365

        # Count complete months of the current year
        for m in range(1, month):
            total_days += month_days[m - 1]

            if m == 2:
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    total_days += 1

        # Count days before the given date
        total_days += day - 1

        # January 1, 1971 = Friday
        # Friday is index 5
        return days[(5 + total_days) % 7]
        