def draw_stars(list):
    for num in list:
        temp = []
        if isinstance(num, int):
            for n in range(0, num):
                temp.append("*")
            print "".join(temp)
        else:
            for n in range(0, len(num)):
                temp.append(num[0])
            print "".join(temp).lower()

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
