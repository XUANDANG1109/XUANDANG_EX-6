# NAME: XUAN DANG

# Phase 1
import random

def dice_roll():
    a = random.randint(1,6)
    return a
number = dice_roll()
while number !=6:
    print(number)
    number = dice_roll()
print(number)

# Phase 2
import random
def dice_roll(side):
    a = random.randint(1,side)
    return a
number_side = int(input("The number of sides on the dice:"))
number = dice_roll(number_side)
while number != number_side:
    print(number)
    number = dice_roll(number_side)
print(number_side)

# Phase 3
number_gallon = float(input("Input gallons"))
def gallonsinliters(gallons):
    liter = gallons * 3.785
    return liter
while number_gallon >=0:
    print(number_gallon, f"gallons = {gallonsinliters(number_gallon):.4f} liters")
    number_gallon = float(input("Input gallons"))

# Phase 4
list = []

number = int(input("Input the number"))
list.append(number)
def sum(list):
    numbersum = 0
    for i in list:
        numbersum += i
    return numbersum
while True:
    number = input("Input the number")
    if number =="":
        break
    x = int(number)
    list.append(x)
print("Sum of list:", sum(list))

# Phase 5
oldlist = []
newlist = []
def removelist(numlist):
    for i in reversed(numlist):
        if i % 2 == 1:
            numlist.remove(i)
    return numlist

while True:
    number = input("Input the number:")
    if number == "":
        break
    x = int(number)
    oldlist.append(x)
    newlist.append(x)

removelist(newlist)

print("List:", oldlist)
print("New List:", newlist)

# Phase 6
pizza1 = float(input("The diameter of pizza 1:"))
pizza2 = float(input("The diameter of pizza 2:"))
price1 = float(input("The price of pizza 1:"))
price2 = float(input("The price of pizza 2:"))
import math
def price (diameter, price, name):
    area = diameter ** 2 * math.pi
    result = price /(area * 0.0001)
    return result
if price (pizza1,price1,1) > price (pizza2,price2,2):
    print("Pizza 2 is cheaper than pizza 1")
elif price (pizza1,price1,1) < price(pizza2,price2,2):
    print("Pizza 1 is cheaper than pizza 2")
else:
    print("Same price, take whatever you want")
# *********************************************************

# Phase 1 solution ( Ex 5)

n = int(input("How manny time to roll a dice"))
dice_sum = 0
for i in range(n):
    dice = random.randint(1,6)
    print(str(dice), end=" ")
    dice_sum = dice_sum + dice
print(f"\nThe sum off the dice is: {dice_sum}")

# Phase 2 solution
number = []
prompt = "Give me a number"
s = input(prompt)
while s!= "":
    number.append(float(s))
    s = input(prompt)
number.sort(reverse=True)
print(number[0:min(5,len(number))])
# or print(number[0:5])

# Phase 3
n = int(input("Give the number:"))
for i in range(2,int(math.sqrt(n)+1)):
    if n % i ==0:
        print(f"Divide by {i}")
        break
else:
    print("This is a prime number")

# Phase 4:
cities = []
for n in range (5):
    cities.append(input("Give me the name of the city"))
for city in cities:
    print(city)
# *************************************

# Phase 1 (Ex6)
import math
import random
def dice_roll():
    return random.randint(1,6)

while True:
    dice = dice_roll()
    print(f"Dice {dice}")
    if dice == 6:
        break

# Phase 2:
def dice_roll_max():
    return random.randint(1,n)
n = int(input("How many sides in your dice?"))

while True:
    dice = dice_roll_max()
    print(f"Dice {dice}")
    if dice == n:
        break

# Phase 3:
def gallons_to_litters(gallons)
    return 3.7654 * gallons

while True:
    g = float(input("How many gallons?"))
    if g < 0:
        break
   # print(f"{g} gallons are {gallons_to_litters(0):.1f}") not done

# Phase 4:
def sum(l):
    s = 0
    for e in l:
        s +=e
    return s

numberlist = []
for n in range (10):
    numberlist.append(random.randint(1,10))
print("List is")
for i in range (len(numberlist)):
    print(numberlist[i], end="")
# print(f"\nSum is {numberlist}") not done

# Phase 5:
def make_even(l):
    result = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            result.append(l[i])
    return result

def print_list(prompt,l):
    print(prompt, end=": ")
    for i in range(len(l)):
        print(l[i], end=" ")

numberlist = []
for n in range(10):
    numberlist.append(random.randint(1,99))
#not done

# Phase 6
def pizza_effiency (0,price):
    return price / math.pi * (d/200.)**2

p1_d = float(input("give the diameter of the first pizza"))
p1_price = float(input("give the price 1"))
p2_d = float(input("give the diameter of the second pizza"))
p2_price = float(input("give the price 2"))


if pizza_effiency(p1_d,p1_price) < pizza_effiency(p2_d,p2_price):
    print("First pizza give better performance")
else:
    print("Second pizza give better performance")

