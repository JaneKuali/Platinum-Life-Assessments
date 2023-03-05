def is_date_format_correct(date:str)->bool:
    """
    This function takes in a date in string format
    and returns true if the date matches the format
    YYYY-MM-DD and false if it doesn't
    """

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    if date == year + "-" + month + "-" + day:
        return print(True)
    else:
        return print(False)

date = input(str("Enter the date format: "))
is_date_format_correct(date)
