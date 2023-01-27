'''
for i in range(1,4):
    for j in range(1,3):
        print("two");

for i in range (1,6):
    for j in range (1,11):
        print((i*j), end=" ");
    print();

for i in range(1,5):
    for k in range(1,6):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
'''

#hollow rectangle
l=10
w=10
for i in range (1, l):
    for j in range(1, w):
            if i == 1 or i == l-1 or j == 1 or j == w-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()


print()
print()

#hollow triangle
t=int(input("enter the base: "));
t+= 1
for i in range (1, t):
    for j in range(1, i+1):
            if i == 1 or i == t-1 or j == 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

#isosceles triangle
t=int(input("enter the base (odd numbers only): "));
middle = (t+1)/2
for i in range (0, t):
    for j in range(0, i+1):
            if i < middle-1:
                print(" ", end=" ")
            if j < (t-1)-i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
    print()
