#print ("Hello World")
import random

# Set up variables.
x0 = random.randint(0,99)
y0 = random.randint(0,99)
#x0 = 50
#y0 = 50
print("x0 "); print (x0)
print("y0 "); print (y0)

#random_number = random.random()
#random_number = random.randint(0,9)
#random_number

# Random walk one step.
#if random_number < 0.5:
#    y0 = y0 + 1
#else:
#    y0 = y0 - 1
#if random_number < 5:
#    y0 = y0 + 1
#else:
#    y0 = y0 - 1

#print(random_number)
#random_number = random.randint(0,9)
#random_number
	
#if random_number < 5:
#    x0 = x0 + 1
#else:
#    x0 = x0 - 1
#random_number
#print(random_number)
#print("x0 "); print(x0)
#print("y0 "); print(y0)

x1 = random.randint(0,99)
y1 = random.randint(0,99)
print("x1 "); print(x1)
print("y1 "); print(y1)


distance = ((x0 - x1)**2 + (y0 - y1)**2)**0.5
print("distance "); print(distance)
