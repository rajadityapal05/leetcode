class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        def days_from_start(date):
            year, month, day = map(int, date.split("-"))

             
            days = 0
            for y in range(1971, year):
                days += 366 if self.isLeap(y) else 365

           
            month_days = [31, 28, 31, 30, 31, 30,
                          31, 31, 30, 31, 30, 31]

            for m in range(1, month):
                days += month_days[m - 1]

                if m == 2 and self.isLeap(year):
                    days += 1

            
            days += day

            return days

        return abs(days_from_start(date1) - days_from_start(date2))

    def isLeap(self, year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)