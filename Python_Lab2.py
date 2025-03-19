count=0
while(count<3):
    count = count+1
    print("Hello Geek")

#single statement while block

count=0
while(count==0):
    count=count+1
    print("Hello Geek")


#Iterating over a list

print("List Iteration")
l=["geeks","for","geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t=("geeks","for","geeks")
for i in t:
    print(i)

# Python program to illustrate
# Iterating by index
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print (list[index])

# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print ('Current Letter :', letter)
    var = 10


for letter in 'geeksforgeeks':
# break the loop as soon it sees 'e'or 's'
    if letter == 'e' or letter == 's':
        break
    print ('Current Letter :'), letter   


def my_function():
    print("Hello from a function")
my_function()


def my_function(fname):
    print(fname + " Ref")
my_function("Email")
my_function("Tobias")
my_function("Linus")


def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
