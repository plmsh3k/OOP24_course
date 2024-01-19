from datetime import date

def list_years(dates: list):
    ans = []
    for i in range(len(dates)):
        ans.append(dates[i].year)
    ans.sort()
    return ans


date1 = date(2019,2,3)
date2 = date(2006,10,10)
date3 = date(1996,5,9)

years = list_years([date1, date2, date3])
print(years)