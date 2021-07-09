import os



def dots():
    if "input.txt" in os.listdir(r"C:\Users\delsi\PycharmProjects\pythonProject"):
        f = open("input.txt", "r")
        for line in f.readlines():
            line = str(line)

            if line[0:2] == "R=":
                r = int(line[2:])

            if line[0:2] == "x=":
                x = int(line[2:])

            if line[0:2] == "y=":
                y = int(line[2:])
                return x, y, r


