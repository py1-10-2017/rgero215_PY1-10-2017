def checkerboard():
    starsOne = "* * * * * * * * * *"
    starsTwo = " * * * * * * * * * *"
    myList = [starsOne, starsTwo]
    for s in range(0, 4):
        for item in myList:

            print item
    pass

checkerboard()
