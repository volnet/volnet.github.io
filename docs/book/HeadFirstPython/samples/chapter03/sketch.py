import os

def getinfo():
    os.getcwd()
    os.chdir("../Documents/")
    #os.chdir("../Dropbox/Documents/个人/volnet.github.io/docs/book/HeadFirstPython/samples/chapter03/")
    os.getcwd()

    try:
        data = open('sketch.txt')
        print(data.readline(), end='')
        print(data.readline(), end='')

        print("---------")

        data.seek(0)
        """
        # use if to deal with the error
        for each_line in data:
            if not each_line.find(":") == -1 :
                (role, line_spoken) = each_line.split(":", 1)
                print(role, end = '')
                print(" said: ", end = '')
                print(line_spoken, end='')
        """

        # use except to deal with the error
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)
                print(role, end = '')
                print(" said: ", end = '')
                print(line_spoken, end='')
            except ValueError:
                pass

        data.close()

    except IOError:
        print("The data file is missing!")

    x = 1
    if x != 1:
        print("x != 1")
    else:
        print("x == 1")