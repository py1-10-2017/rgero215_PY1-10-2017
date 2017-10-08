# def odd_even():
#     for count in range(1, 2001):
#         if count % 2 == 1:
#             print "Number is {}. This is an odd number.".format(count)
#
#         if count % 2 == 0:
#             print "Number is {}. This is an even number.".format(count)
#
# odd_even()

def multiply(my_list, multiplied_by):
    for number in range(len(my_list)):
        my_list[number] *= multiplied_by
    return my_list

a = [2, 4, 10, 16]
print multiply(a, 5)

def layered_multiples(arr):
    new_array = []
    for number in arr:
        temp = []
        for n in range(0, number):
            temp.append(1)
        new_array.append(temp)


    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
