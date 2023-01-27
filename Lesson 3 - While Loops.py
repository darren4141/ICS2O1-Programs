#program that starts at 0 and counts by 5 and exits when it reaches 25

count = 0; #initialize variable
while count <= 30: #will stop the program when it reaches 30
    print(count);
    count = count + 5;

#----------------------EXERCISES----------------------#

#--------------------------1--------------------------#
#WRITE A PROGRAM TO ENTER A NUMBER REPEATEDLY
#AND EXIT WHEN A NEGATIVE NUMBER IS ENTERED
print(" ");
print(" ");

num=0;
while num > -1: #stops when number is negative
    print("enter a number!");
    num=float(input());
          
print("number is negative, end of program.");



#--------------------------2--------------------------#
#WRITE A PROGRAM TO ENTER A WORD REPEATEDLY
#AND EXIT WHEN THE WORD "STOP" IS ENTERED
print(" ");
print(" ");

print("enter a word!");
word=input();
print("your word is", word);

while word != "stop" and word != "STOP" and word != "Stop": #stops when "stop" is enterd
    print("enter a word!");
    word=input();
    print("your word is", word);

print("stop entered, ending program.")



#--------------------------3--------------------------#
#WRITE A PROGRAM THAT ASKS FOR A NUMBER AND THEN COUNTS FROM 0 TO THAT NUMBER
print(" ");
print(" ");

countto=0;
i=0;
print("enter a number for me to count to!");
countto=int(input());

while i <= countto:
    print(i);
    i = i+1;

print("done counting, ending program.");



#------------------------4 & 5------------------------#
#WRITE A PROGRM THAT HAS A NUMBER BETWEEN 1 AND 10 AND ASKS THAT THE USER GUESSES THE NUMBER
#STOP WHEN THE USER GUESSES THE ANSWER CORRECT
#AND OUTPUTS A NICE COMMENT AND TELLS THE USER HOW MANY GUESSES THEY TOOK
print(" ");
print(" ");

print("guess a number between 1-10!");
random=7;
guess=0;
tries=0;

while guess != random:
    guess=int(input());
    if(guess!=7):
        print("try again!");

    if(guess == 7):
        print("good job!");
    tries = tries + 1;

if(tries > 1):
    print("you got it in", tries, "tries!");
if(tries == 1):
    print("you got it in", tries, "try!");

