#1)Create a program that asks the user for two numbers. Then find the
#Greatest Common Factor (GCF) between the two numbers.

num1 = int(input())
num2 = int(input())
if num1 > num2:
    smallestnum = num2
else:
    smallestnum = num1

for i in range (1, smallestnum + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcf = i

print(gcf)


#2)Create a program that inputs 3 numbers and then sorts the three
#numbers from largest to smallest 
inp1 = int(input())
inp2 = int(input())
inp3 = int(input())

if inp1 < inp2:
    pos1 = inp2
    pos2 = inp1
else:
    pos1 = inp1
    pos2 = inp2

if pos2 < inp3:
    pos3 = pos2
    pos2 = inp3
else:
    pos3 = inp3

if pos1 < pos2:
    temp = pos1
    pos1 = pos2
    pos2 = temp

print(pos1, pos2, pos3)
