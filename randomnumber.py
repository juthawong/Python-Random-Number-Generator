from random import randint
number = int(raw_input("How many number you want to random : "));
defa = "";
for i in range(0,number):
    defa += str(randint(0,9))
print(defa);
