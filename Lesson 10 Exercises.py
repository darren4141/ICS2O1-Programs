#1. Write a program that asks the user to enter an
#integer and determines if a number entered is even or odd.

print("even or odd machine");
num = int(input("Enter a number! "));
if num%2 == 0:
        print("number is even!");

if num%2 == 1:
        print("number is odd!");

#2. Write a program that asks the user to enter two
#integers and determines if the first number enter is
#divisible by the second number.
print("divisibility machine");
dividend = int(input("dividend: "));
divisor = int(input("divisor: "));

if dividend%divisor == 0:
    print("numbers are divisible!");
else:
    print("numbers are not divisible!");
    
#3. Write a program that asks the user to enter two integers
#and determines which number is larger and then determines if
#the larger number is divisible by the smaller number.
print("comparison machine");
print("divide larger number by smaller number");
num1 = int(input("1st number: "));
num2 = int(input("2nd number: "));

if num1 > num2:
    larger = num1
    smaller = num2
elif num1 <= num2:
    larger = num2
    smaller = num1

if larger%smaller == 0:
    print(larger, "is divisible by", smaller);
else:
    print(larger, "is not divisible by", smaller);
