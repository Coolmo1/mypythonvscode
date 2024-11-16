"""Using python.. create a logic that accepts user input for age and prints to the user's screen whether they are allow to vote or not.
Minimum voting age is 18."""

print("Official Voting Website")

fname = input("Firstname: ")
mname = input("(Optional) Middle name: ")
lname = input("Lastname: ")
age = int(input("Age: "))

if age >= 18 and age < 66:

    print("Which is better")
    print("1. for cookie and 2. for cupcake")
    vote = int(input("Choose between 1. or 2.: "))
    if vote == 1:
        print("You have voted for Cookies")
    elif vote == 2:
        print("You have voted for Cupcake")
    else:
        print("Your vote hase not been counted, because you have not typed a registerd vote")

elif age < 18:
    print(fname + "Sorry you are not able to Vote, because you are to young")

elif age < 0 :
    print("Can you type in your real age")
