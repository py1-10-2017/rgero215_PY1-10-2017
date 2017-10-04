"""
Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000.
Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""
#odd numbers from 1 to 1,000
for counter in range(1, 1000):
    if counter % 2 == 1:
        print counter
#multiples of 5 from 5 up to 1,000,000 not including 1,000,000
#to include 1,000,000 I can subtitude 1000000 for 1000001
for counter in range(5, 1000000):
    if counter % 5 == 0:
        print counter
#sum of elements on list a
a = [1, 2, 5, 10, 255, 3]
result = 0;
for item in a:
    result += item
print result
#average of list a
avg = 0
for item in a:
    avg += item
print avg / len(a)
