def compute_prev_date(dates_list:list):
    prev_dates_list = []

    #month dictionary
    monthdict = {
    '01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun',
    '07':'Jul','08':'Aug','09':'Sept','10':'Oct','11':'Nov','12':'Dec'
    }

    for i in dates_list:
        year = i[0:4]
        month = i[5:7]
        day = int(i[8:10])

        if(day == 1):
            day = 30
            month = int(month)-1
        else:
            day = day-1

        prev_date = str(day) + " " + monthdict[(str(month))] + " " + year
        prev_dates_list.append(prev_date)
    return [print(prev_dates_list)]

#User input#
dates_list = []
length = int(input("Number of dates to add to list: "))
for i in range(0,length):
    date = input()
    dates_list.append(date)

#Output#
print("\nCurrent dates: \n",dates_list)
print("\nPrevious Date: ")
compute_prev_date(dates_list)
