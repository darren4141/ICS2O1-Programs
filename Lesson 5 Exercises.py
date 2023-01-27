#Write a program that asks the user to guess a number between 1 to 10. Have the program
#provide hints if the answer is not correct (ie. The number is higher or the number is lower)
#Extend the above exercise 1 to have a repeat option after the user guesses the correct answer

number = 7
guess = 0
repeat = "y"

while repeat == "y":
    guess = 0
    print("guess my number between 1-10!")
    while guess != number:
        guess = int(input());
        if guess == number:
            print("you guessed correctly!");
        elif guess > number:
            print("my number is lower!");
        elif guess < number:
            print("my number is higher!");
    print("");
    print("would you like to play again? (y/n)");
    repeat = input();
#Have the user enter a login name and a password. After 3 attempts have the program
#prompt that the user must change their password.

username = "darren"
password = "wordpass"
i = 0
correct = False

print("enter your username and password");
while i < 3:
    i = i + 1;
    usernameinp = input("Username: ")
    passwordinp = input("Password: ")
    if usernameinp != username or passwordinp != password:
        print("incorrect password, please try again")
    if usernameinp == username and passwordinp == password:
        print("access granted")
        correct = True
        break;

if correct == False:
    print("attempt to login failed too many times, please change your password");
    
#Have the user enter 10 numbers and the program should keep track of the smallest, and
#largest number and output them at the end of the program.
for x in range(10):
    print("enter a number")
    number = int(input());
    if x == 0:
        highest = number
        lowest = number
    if number < lowest:
        lowest = number
    if number > highest:
        highest = number
print("the highest number is", highest);
print("the lowest number is", lowest);

#Program calculates an equation a table of values f(x) = 3x^2 - 2x+1 and keeps track of the min
#y value. The dependent variable x should go up in 0.1 decimal increments. One suggest is
#to set the domain (x) between -1 and 2 for this equation
print("enter min and max for the equation");

y=float(input());
max=float(input());



#TABLE UI
print("");
print(" y = 3x^2 - 2x + 1");
print("____________________________");
print("       y     |         x  ");
print("_____________|______________");

#LOOP
for x in range(1,32):
    print("{:10}".format(y), "  |", "{:10}".format(3 * (y**2) - (2*y) + 1));
    y = y*10
    y += 1
    y = y/10

#Create a program to ask 5 multiple choice questions (a,b,c,d) and output a personality type
#as a result. Ie. You are an outgoing social personality type
print("")
print("")
a=0
b=0
repeat = "y"

while repeat =="y":
    print("PERSONALITY TYPE TEST")
    print("this test will be 9 questions long, please answer truthfully for the best result")
    print("answer with 'a' or 'b'")


    print("how would you describe yourself?")
    print("a) loud")
    print("b) quiet")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1

    print("where would you like to be right now?")
    print("a) outside")
    print("b) at home")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1


    print("what is your favorite thing to do")
    print("a) talk/socialize")
    print("b) enjoy my hobby")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1


    print("what do you prefer")
    print("a) having lots of friends")
    print("b) having a few close friends")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1

    print("where are you more productive?")
    print("a) in a loud cafe")
    print("b) in a quiet room")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1

    print("after a long day what would you prefer?")
    print("a) going out to have fun with my friends")
    print("b) having fun at home watching a movie or playing a game")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1

    print("which do you prefer?")
    print("a) working in a group")
    print("b) working alone")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1

    print("you feel like you learn more during a")
    print("a) discussion")
    print("b) lesson")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1

    print("what do you do when you get a personal achievement?")
    print("a) show my friends")
    print("b) keep it to myself")

    answer=input()
    if(answer=="a"):
        a = a+1

    if(answer=="b"):
        b = b+1

    if(a > b):
        print("you are an extrovert")

    if(b > a):
        print("you are an introvert")

    print("would you like to take the test again? ('y' or 'n'")
    repeat=input()
