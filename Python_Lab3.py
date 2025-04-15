#Program 1


for num in range(1500,2701):    
    if num%7==0 and num%5==0:        
        print(num)





#Program 2

c=input('Enter temperature in Celsius')
f=input('Enter temperaure in Fahrenheit')
c=(5*(int(f)-32))/9
f=int(c)*(9/5) +32
print('Temperature in Celsius',c)
print('Temperature in Fahrenheit',f)







#Program 3

import random

ntg = random.randint(1, 9)

while True:

    ug = int(input("Guess a number between 1 and 9: "))
    
    
    if ug == ntg:
        print("Guessed successfully!")
        break  
    else:
        print("Wrong guess, try again!")






#Program 4

for i in range(1,6):
    print('*'*i)
for j in range(4,0,-1):
    print('*'*j)






#Program 5

word = input("Enter a word: ")

reversed_word = ""

for char in word:
    reversed_word = char + reversed_word 


print("Reversed word:", reversed_word)






#Program 6 

even_count = 0
odd_count = 0

while True:
    num = int(input("Enter a number (or type '0' to stop): "))
    
    
    if num == 0:
        break
    

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)






#program 7

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print(f"Item: {item} - Type: {type(item)}")






#program 8

for i in range(7):  
    if i == 3 or i == 6:
        continue
    print(i)






#program 9 

a=0
b=1
while b<50:
        if b!=0:
            print (b)
        a,b=b,a+b





#program 10

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))


result = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    result.append(row)


print(result)


#prgrm 11

lines = []

while True:
    line = input("Enter a line (press Enter to stop): ")
    if line == "":
        break
    lines.append(line.lower())

for l in lines:
    print(l)


#prgrm 12

data = input("Enter comma-separated 4-digit binary numbers: ").split(',')
result = []

for b in data:
    if int(b, 2) % 5 == 0:
        result.append(b)

print(','.join(result))



#prgrm 13

s = input("Enter a string: ")

letters = 0
digits = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)


#prgrm 14

password = input("Enter your password: ")

has_lower = False
has_upper = False
has_digit = False
has_special = False
special_chars = "$#@"

if 6 <= len(password) <= 16:
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if has_lower and has_upper and has_digit and has_special:
        print("Valid password")
    else:
        print("Invalid password: does not meet all requirements.")
else:
    print("Invalid password: length should be between 6 and 16.")
