# ask user for width and loop until they
#enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

#main routine starts here...

keep_going = ""
while keep_going == "":

    #get width and height
    width = num_check("width: ")
    height = num_check("height: ")

    #calculate area and / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    #display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"area: {area} square units")

    #ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for usin the area/ perimeter calculator")
