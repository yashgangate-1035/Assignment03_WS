#Use the datetime module to calculate the number of days between two dates.

from datetime import datetime

date1 = input("Enter first date (YYYY-MM-DD): ")
date2 = input("Enter second date (YYYY-MM-DD): ")
d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")
print("Number of days between the dates:", abs((d2 - d1).days))
