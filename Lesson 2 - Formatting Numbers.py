# f ~ stands for float
# i ~ stands for integer
# s ~ stands for string

v=10.4
print("{:10.4f}".format(v));
print('%10.4f'%v);

numbers = [23.23, 0.23242587, 1, 4.223, 9887.2]
for x in numbers:
    print("{:10.4f}".format(x))

x=10
print("{:4}".format(x))
#to format integers
