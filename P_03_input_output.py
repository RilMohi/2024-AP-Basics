#ask the user for their name
username = input("what is your name?")

#ask the user for their favorite number (interger)
fav_num = int(input("what is your favorite number? "))

#double, halve and square the user's favorite number
double = fav_num * 2
halve = fav_num/ 2
square = fav_num * fav_num

#greet the user
print(f"hi {username}, your favorite number is {fav_num}")

#output the results of doubling, halving and
# squaring their favorite number
print(f"double {fav_num} is {double}")
print(f"halve {fav_num} is {halve}")
print(f"{fav_num} squared is {square}")
print()
print("have a nice day")
