def type_list(test):
    myStr = ""
    mySum = 0
    typeOf = ""
    for item in test:
        if isinstance(item, (str, int, float)):
            if type(item) is float:
                mySum += item
                typeOf = "The list your enter is of mixed type"
            elif type(item) is int:
                mySum += item
                typeOf = "The list your enter is of integer type"
            else:
                myStr += " " + item
                if mySum == 0:
                    typeOf = "The list your enter is of string type"
    print typeOf
    if myStr != "":
        print "String:" + myStr
    if mySum != 0:
        print "Sum: " + str(mySum)

    pass

# l = ['magical','unicorns']
l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]

type_list(l)
