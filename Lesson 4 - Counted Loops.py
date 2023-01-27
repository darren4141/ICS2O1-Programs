#COUNTED LOOPS

for x in range(5): 
    print(x);
#this loop will print out the numbers 0, 1, 2, 3, 4
#the loop never gets to 5 as it starts at 0
#it does 5 iterations


for x in range(3, 6):
    print(x);
#this loop now has a start and end
#this loop will print the numbers 3, 4, 5

primes = [1, 2, 3, 5, 7];
for prime in primes:
    print(prime);

#this loop has a specified range
#it will print the entire array

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
#this loop has an if statement to only print odd numbers

count=0;
print(count);
while True:
    count += 1;
    print(count);
    if count >= 5:
        break;
#this while loop uses an if statement and break as a condition
