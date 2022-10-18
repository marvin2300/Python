from datetime import date
import datetime

while True:
    try:

        today = datetime.datetime.now()
        t_year = today.year
        t_month = today.month
        t_day = today.day

        year = int(input("Insert a year: \n"))
        month = int(input("Insert a month: \n"))
        day = int(input("Insert a day: \n"))

        date_born = date(year, month, day)
        date_today = date(t_year, t_month, t_day)

        delta = date_today - date_born

        print(delta)

        delta_years = t_year - year
        delta_months = t_month - month
        delta_days = t_day - day

        print(delta_years, delta_months, delta_days)

        exit()

    except ValueError:
        print("Error, try again!")

