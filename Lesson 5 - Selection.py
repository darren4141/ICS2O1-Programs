#LESSON 5 - SELECTION

x = 0;
print("enter your mark!");
x = int(input());
if x<0 or x >100:
    print("invalid mark!");
elif x >=50:
    print("D");
elif x >= 60:
    print("C");
elif x >= 70:
    print("B");
elif x >= 80:
    print("A");
else:
    print("F");
#this program has a logical error, as everything above 50 will be counted as a D

#correct program, reverse the order of the if statements:

print("enter your mark!");
x = int(input());
if x<0 or x >100:
    print("invalid mark!");
elif x >= 80:
    print("A");
elif x >= 70:
    print("B");
elif x >= 60:
    print("C");
elif x >= 50:
    print("D");
else:
    print("F");
