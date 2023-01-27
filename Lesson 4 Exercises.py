#LESSON 4 EXERCISES

#WRITE A PROGRAM THAT ASKS THE USER TO INPUT 5 NUMBERS
#AND OUTPUT USING A COUNTED LOOP
nums = []


print("enter 5 numbers")
for x in range(5):
    nums.append(int(input()))
    
for x in nums:
    print(x)

average = (nums[0] + nums [1] + nums[2] + nums[3] + nums[4])/5

print("the sum is", average*5);
print("the average is", average);
print("program ending")


#WRITE A PROGRAM THAT ASKS THE USER TO INPUT A NUMBER
#AND OUTPUT THE COUNTING STARTING FORM ZERO TO THAT NUMBER
print("")
print("")

print("enter a number for me to count to!");
count = int(input())
for x in range(count + 1):
    print(x)

#WRITE A PROGRAM THAT GIVES YOU A PERSONALITY TYPE BASED ON 9 QUESTIONS
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

#USING ANY LOOP, HAVE THE USER ENTER A WORD ONE AT A TIME
#AND END WHEN STOP IS ENTERED AND OUTPUT THE NUMBER OF WORDS ENTERED
print("")
print("")

wordcount=0

while True:
    wordcount = wordcount + 1
    print("enter a word");
    word=input()

    if word == "stop" or word == "STOP" or word == "Stop":
            break;

print("stop entered, ending program")
print("you entered", wordcount, "words!");


#WRITE A MATH PROGRAM TO OUTPUT THE VALUES OF X AND Y FOR AN EQUATION
# Y = 2X + 1
# X WILL HAVE DOMAIN OR VALUES BETWEEN 1-10
# OUTPUT A TABLE REPRESENTING X AND Y

#USER INSTRUCTION
print("enter min and max for the equation");
min=int(input())
max=int(input())

#TABLE UI
print("")
print(" y = 2x + 1")
print("_____________")
print("  y   |   x")
print("______|______")

#LOOP
for x in range(min,max+1):
    print("{:3}".format(min), "  |", "{:3}".format((min * 2) + 1))
    min = min + 1
