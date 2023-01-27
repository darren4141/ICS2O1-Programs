#Case insensitive checking
#casefold() ignores all cases
#lower()    makes all lowercase
#upper()    makes all uppercase

name = input("enter your name : ");
print(name.lower());
print(name.upper());

#if stop is entered as a name program will stop

while(name.casefold() != "stop"):   #program will accept stop no matter the cases
    print("your name is:", name);
    name=input("Enter another name! Enter stop to exit ");
print("stop entered, ending program");


#eval function

x = eval(input("enter a number: "));
print("x =", x);
print("type:", type(x));
#if a float is entered, the eval function will make x a float
#if an int is entered, the eval function will make x an int
