import os

def saveinfo():
    man = []
    other = []
    
    os.getcwd()
    os.chdir("../Documents/")
    #os.chdir("../Dropbox/Documents/个人/volnet.github.io/docs/book/HeadFirstPython/samples/chapter04/")
    os.getcwd()
    data = open('sketch.txt')

    try:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)
                role = role.strip()
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass

        data.close()

        try:
            man_file = open('man_file.txt', 'w')
            other_file = open('other.txt', 'w')

            print(man, file=man_file)
            print(other, file=other_file)

        except IOError:
            print('File error')

        finally:
            if 'man_file' in locals():
                print("----------", file=man_file)
                man_file.close()
            if 'other_file' in locals():
                print("----------", file=other_file)
                other_file.close()

    except IOError:
        print("The data file is missing!")

    try:
        data = open('missing.txt')
        print(data.readline(), end='')
    except IOError as err:
        print('File error' + str(err))
    finally:
        if 'data' in locals():
            data.close()

    

    data = open('sketch.txt')
    try:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)
                role = role.strip()
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass

        data.close()

        try:
            with open('man_file.txt', 'a') as man_file:
                print(man, file=man_file)
            with open('other.txt', 'a') as other_file:
                print(other, file=other_file)
            with open('man_file.txt', 'a') as man_file, open('other.txt', 'a') as other_file:
                print(man, file=man_file)
                print("----------", file=man_file)
                print(other, file=other_file)
                print("----------", file=other_file)

        except IOError:
            print('File error')

    except IOError:
        print("The data file is missing!")


    import pickle
    try:
        with open('pickle.txt', 'wb') as pickle_wb:
            pickle.dump(['a', 'b', 'c'], pickle_wb)
        with open('pickle.txt', 'rb') as pickle_rb:
            pickle_restore = pickle.load(pickle_rb)
            print(pickle_restore)
    except IOError as ioErr:
        print('IOError' + str(ioErr))
    except pickle.PickleError as pickleErr:
        print('PickleError' + str(pickleErr))
