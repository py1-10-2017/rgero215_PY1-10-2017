def find_Character(listStr):
    result = []
    for item in listStr:
        for charcter in item:
            if "o" in charcter:
                result.append(item)

    print result
    pass
word_list = ['hello','world','my','name','is','Anna']

find_Character(word_list)
