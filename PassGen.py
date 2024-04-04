import random
length=int(input("enter the length of password you want to generate: "))
string_cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string_small="abcdefghijklmnopqrstuvwxyz"
string_special="!@#$%^&*()_+"
combination=string_cap+string_small+string_special

password = ''
for i in range(length):
    password=password+(random.choice(combination))

print(password)