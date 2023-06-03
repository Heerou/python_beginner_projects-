def main():
    print("Lest convert US dollars to Pounds Sterling")
    dollars = eval(input("Set the total of dollar that you want to convert: "))
    pounds = convert_to_pounds(dollars)
    print("The conversion is: ", pounds)


convert_to_pounds = lambda dollars: dollars * 0.82

main()
