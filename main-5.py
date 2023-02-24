import os  # import os library
import re  # import re library


def os_path(path):  # define function os_path which will search through all folder and sub folders
    for x in os.listdir(path):  # for loop that uses listdir to find all sub folders
        di_r = os.path.join(path, x)  # joins the pathdir with the for loop and puts it in di_r
        if os.path.isdir(di_r):  # checks if there is a directory in di_r
            sub = os.path.basename(di_r)  # if there is a directory split the path and return the tail
            if re.match(r'\w*[A-Z]\w*', sub):  # bool statement that checks for Cap letters using regex
                print(sub)  # print sub variable
            os_path(di_r)  # calls the function with di_r

        else:  # if there is no directory then print di_r
            print(di_r)  # print di_r


os_path('start')  # calls the os_path function with the path start
