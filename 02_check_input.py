def check_temp(min_value):
    error = "Please enter a number that is more " \
            "than {}".format(min_value)

    try:
        response = float(input("Chose a number: "))

        if response < min_value:
            print(error)
        else:
            return response

    except ValueError:
        print(error)


# *** Main Routine ****

while True:
    to_check = check_temp(-273)
    print("Success")