# # writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()

# Using readlines()
from utils.utils import open_file

file_name = 'postcode.txt'
PATH = r'sample input/' + file_name

file = open(PATH, 'r')
Lines = file.readlines()
file.close()

thisdict = {}
# Strips the newline character
for line in Lines:
    postcode = line.split(",")

    # print('{}: {}: {}'.format(postcode[0], postcode[1], postcode[2]))
    print(line)
    if thisdict.get(postcode[1]) is None:
        thisdict[postcode[1]] = []
    else:
        thisdict[postcode[1]].append(postcode[0])

# for key, value in thisdict.items():
#     if value:
#         print(key, value)
