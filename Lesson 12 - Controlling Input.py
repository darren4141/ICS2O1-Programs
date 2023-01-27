#restricting string input

while True:
    age=input("Enter your age: ");
    print()
    try:
        val = float(age);
        print("The age entered was ", val);
        break;
    except ValueError:
        print("That's not a number, Try again");
print("Done!");




while True:
    num=input("enter a number from 0 to 5: ");
    print()
    try:
        inp = float(num);
        print("The number entered was ", num);
        break;
    except ValueError:
        print("That's not a number, try again!");
print("Done!");
