import os

def dealinfo():

    os.getcwd()
    os.chdir("../Documents/hfpy_ch5_data")
    #os.chdir("../Dropbox/Documents/个人/volnet.github.io/docs/book/HeadFirstPython/samples/chapter05/")
    os.getcwd()
    
    try:
        """
        with open('james.txt') as a_file:
            data = a_file.readline()
        james = data.strip().split(',')

        with open('julie.txt') as b_file:
            data = b_file.readline()
        julie = data.strip().split(',')

        with open('mikey.txt') as c_file:
            data = c_file.readline()
        mikey = data.strip().split(',')

        with open('sarah.txt') as d_file:
            data = d_file.readline()
        sarah = data.strip().split(',')
        """

        james = get_coach_data('james.txt')
        julie = get_coach_data('julie.txt')
        mikey = get_coach_data('mikey.txt')
        sarah = get_coach_data('sarah.txt')

        print(james)
        print(julie)
        print(mikey)
        print(sarah)

        print('------')

        print(sorted(james))
        print(sorted(julie))
        print(sorted(mikey))
        print(sorted(sarah))

        print('------')

        print(sorted(sanitize_list(james)))
        print(sorted(sanitize_list(julie)))
        print(sorted(sanitize_list(mikey)))
        print(sorted(sanitize_list(sarah)))

        print('------')

        print(sorted([sanitize(item) for item in james]))
        print(sorted([sanitize(item) for item in julie]))
        print(sorted([sanitize(item) for item in mikey]))
        print(sorted([sanitize(item) for item in sarah]))

        print('------')

        print(sorted(unique_list([sanitize(item) for item in james])))
        print(sorted(unique_list([sanitize(item) for item in julie])))
        print(sorted(unique_list([sanitize(item) for item in mikey])))
        print(sorted(unique_list([sanitize(item) for item in sarah])))

        print('------')

        print(sorted(unique_list([sanitize(item) for item in james]))[0:3])
        print(sorted(unique_list([sanitize(item) for item in julie]))[0:3])
        print(sorted(unique_list([sanitize(item) for item in mikey]))[0:3])
        print(sorted(unique_list([sanitize(item) for item in sarah]))[0:3])

        print('------')

        print(sorted(set([sanitize(item) for item in james]))[0:3])
        print(sorted(set([sanitize(item) for item in julie]))[0:3])
        print(sorted(set([sanitize(item) for item in mikey]))[0:3])
        print(sorted(set([sanitize(item) for item in sarah]))[0:3])

        print('------')

        print(sorted(set([sanitize(item) for item in james]), reverse=True)[0:3])
        print(sorted(set([sanitize(item) for item in julie]), reverse=True)[0:3])
        print(sorted(set([sanitize(item) for item in mikey]), reverse=True)[0:3])
        print(sorted(set([sanitize(item) for item in sarah]), reverse=True)[0:3])

    except IOError as err:
        print('error:' + str(err))

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (min, secs) = time_string.split(splitter)
    return min + '.' + secs

def sanitize_list(time_arr):
    time_arr2 = []
    for time_string in time_arr:
        time_arr2.append(sanitize(time_string))
    return (time_arr2)

def unique_list(the_list):
    unique = []
    for item in the_list:
        if item not in unique:
            unique.append(item)
    return unique

def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
        return(data.strip().split(','))
    except IOError as err:
        print('File Error:' + str(err))
        return(None)