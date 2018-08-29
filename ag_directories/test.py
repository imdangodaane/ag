import os


file_list = os.listdir('/tmp/guest-uupvvi/Desktop/nqui/ag_basic/')
for file in file_list:
    print(file)
    f = open(file, 'r')
    a = f.read()
    print(a)

a = '/temp/guest'
