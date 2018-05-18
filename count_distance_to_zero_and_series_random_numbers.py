# -*- coding: utf-8 -*-
"""
Created on Fri May 16 17:37:41 2018
@author: souravg

"""
"""
1) How-to-count-distance-to-the-previous-zero
For each value, count the difference back to the previous zero (or the start of the Series,
whichever is closer)
create a new column 'Y'
Consider a DataFrame df where there is an integer column 'X'
import pandas as pd
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a
Series of random numbers.
3) Find the sum of the values in s for every Wednesday
4) Average For each calendar month
5) For each group of four consecutive calendar months in s, find the date on which the
highest value occurred.
"""
import random
import datetime
import calendar
from pandas.tseries.offsets import BDay
import pandas as pd

list_org = [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]
df = pd.DataFrame({'X': list_org})
list_new = []
count_diff_back = 0
for item in list_org:
    if(item !=0):
        count_diff_back += 1
    else:
        count_diff_back = 0
    list_new.append(count_diff_back)
df['Y'] = list_new
print(df)

def all_businessdays(year):
# January 1st of the given year and get the next business day if the 1st is on weekend
       dt = datetime.date(year, 1, 1)
       dt += BDay()
# December 31st of the previuos year and get the next business day of the next year
       prev_dt = datetime.date(year-1, 12, 31)
       prev_dt += BDay()
       
       yield prev_dt
# Iterating through the loop and get the next business day untill the end of year is not weekend  
       while dt.year == year:
        yield dt
        dt += BDay()
# DatetimeIndex created for each business day of the given year and used it to index a Series of random numbers
index_lab = []
random_number = []
index_first_four_month = []
index_middle_four_month = []
index_last_four_month = []
for bdatetime in all_businessdays(2015):
    bdatetime = str(bdatetime)
    index_lab.append(bdatetime)
    random_number.append(random.randint(1,300))
    if('01' in bdatetime[5:7] or '02' in bdatetime[5:7] or '03' in bdatetime[5:7] or '04' in bdatetime[5:7]):
        index_first_four_month.append(bdatetime)
    elif('05' in bdatetime[5:7] or '06' in bdatetime[5:7] or '07' in bdatetime[5:7] or '08' in bdatetime[5:7]):
        index_middle_four_month.append(bdatetime)
    else:
        index_last_four_month.append(bdatetime)
        
business_random = pd.Series(random_number,index = index_lab)
print("\nSeries of Random numbers with DatetimeIndex for each business day of year 2015\n",'-'*78, sep='')
print(business_random.to_string())
print('-'*95, sep='')
wednesday_index_lab = []
month_index_lab = []
for dt in index_lab:
    date_only = pd.to_datetime(dt)
    month = date_only.month
    year = date_only.month
    day = date_only.day
    ans = datetime.date(year, month, day)
    wednesday_index_lab.append(ans.strftime("%A"))
    month_index_lab.append(month)

business_random.index = wednesday_index_lab
#print(business_random.loc['Wednesday'])
print("Sum of the values for every Wednesday of year 2015 is %d\n" %business_random.loc['Wednesday'].sum(),'-'*95, sep='')
business_random.index = month_index_lab
#print(business_random.to_string())
for mon in range(1,13):
    print("Average value for %s'2015 is %0.2f" %(calendar.month_name[mon],business_random.loc[mon].mean()))
print('-'*95, sep='')

business_random.index = index_lab

first_date_of_first_four_month= index_first_four_month[0]
last_date_of_first_four_month= index_first_four_month[len(index_first_four_month)-1]
value_max_date_of_first_four_month = max(business_random.loc[first_date_of_first_four_month:last_date_of_first_four_month])
max_date_of_first_four_month = business_random[business_random == value_max_date_of_first_four_month].index[0]
print("The date with the maximum value being %d for first 4 months of 2015 is %s" %(value_max_date_of_first_four_month,max_date_of_first_four_month))

first_date_of_middle_four_month= index_middle_four_month[0]
last_date_of_middle_four_month= index_middle_four_month[len(index_first_four_month)-1]
value_max_date_of_middle_four_month = max(business_random.loc[first_date_of_middle_four_month:last_date_of_middle_four_month])
max_date_of_middle_four_month = business_random[business_random == value_max_date_of_middle_four_month].index[0]
print("The date with the maximum value being %d for middle 4 months of 2015 is %s" %(value_max_date_of_middle_four_month,max_date_of_middle_four_month))

first_date_of_last_four_month= index_last_four_month[0]
last_date_of_last_four_month= index_last_four_month[len(index_last_four_month)-1]
value_max_date_of_last_four_month = max(business_random.loc[first_date_of_last_four_month:last_date_of_last_four_month])
max_date_of_last_four_month = business_random[business_random == value_max_date_of_last_four_month].index[0]
print("The date with the maximum value being %d for last 4 months of 2015 is %s" %(value_max_date_of_last_four_month,max_date_of_last_four_month))
print('-'*95, sep='')