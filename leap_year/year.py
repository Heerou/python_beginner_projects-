def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Is a leap year")
            else:
                print("Is not a leap year")
        else:
            print("Is a leap year")
    else:
        print("Is not a leap year")


the_year = int(input("Write your year: "))

leap_year(the_year)
