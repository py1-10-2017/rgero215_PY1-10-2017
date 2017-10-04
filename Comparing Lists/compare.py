def compare(list_one, list_two):
    result = ""
    for item in list_one:
        for element in list_two:
            if item == element:
                result = "The list are the same"
            else:
                result = "The list are not the same"
    print result

    pass

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
#
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']

compare(list_one, list_two)
