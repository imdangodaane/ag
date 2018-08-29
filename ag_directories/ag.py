import os
import sys


def find_index_of_found_pattern(pattern, line):
    current_index = 0
    while True:
        current_index = line.find(pattern, current_index)
        if (current_index == -1):
            return None
        yield current_index
        current_index += len(pattern)


def into_a_list(pattern, line):
    _list = []
    a = find_index_of_found_pattern(pattern, line)
    while True:
        try:
            _list.append(next(a))
        except StopIteration:
            return _list


def find_option():
    options = []
    for i in sys.argv:
        if i[:2] == '--':
            options.append(i)
    return options


def ag_basic(pattern, file_name, option):
    num = 0
    count = 0
    list_index_of_pattern = []

    f = open(file_name, 'r')
    lines = f.read().split('\n')[:-1]

    # find all cases of pattern, then print line contain patterns with color
    for line in lines:
        if (option == '--case-sensitive'):
            compare = line
        else:
            pattern = pattern.lower()
            compare = line.lower()
        num += 1        
        list_index_of_pattern = into_a_list(pattern, compare)

        if (len(list_index_of_pattern) == 0):
            continue

        start = 0
        print('\033[1;33m' + str(num) + '\033[0m' + ':', end='')

        for index in list_index_of_pattern:
            print(
                  line[start:index]
                  + '\033[30;43m'
                  + line[index:index + len(pattern)]
                  + '\033[0m', end=''
                 )
            start = index + len(pattern)
        print(line[index + len(pattern):])


def ag():
    options = find_option()
    if len(options) == 0:
        if len(sys.argv) == 3 and '/' in sys.argv[2]:
            pattern = sys.argv[1]
            path = sys.argv[2]
            file_list = os.listdir(path)
            print(file_list)
            for file in file_list:
                file = os.path.join(path, file)
                print(file)
                if file[0] == '.':
                    continue
                f = open(file, 'r')
                pattern = pattern.lower()
                temp = f.read()
                temp = temp.lower()
                if pattern in temp:
                    print('\033[1;32m' + file + '\033[0m')
                    ag_basic(pattern, file, 'normal')
                    print()
        elif len(sys.argv) == 3 and sys.argv[2] != '.':
            pattern = sys.argv[1]
            file = sys.argv[2]
            if file[0] == '.':
                return None
            f = open(file, 'r')
            pattern = pattern.lower()
            temp = f.read()
            temp = temp.lower()
            if pattern in temp:
                print('\033[1;32m' + file + '\033[0m')
                ag_basic(pattern, file, 'normal')
        else:
            pattern = sys.argv[1]
            file_list = os.listdir()
            file_list = sorted(file_list)
            for file in file_list:
                if file[0] == '.':
                    continue
                f = open(file, 'r')
                pattern = pattern.lower()
                temp = f.read()
                temp = temp.lower()
                if pattern in temp:
                    print('\033[1;32m' + file + '\033[0m')
                    ag_basic(pattern, file, 'normal')
                    print()
    elif len(options) == 1:
        pattern = sys.argv[2]
        file_list = os.listdir()
        file_list = sorted(file_list)
        for file in file_list:
            if options[0] != '--hidden' and file[0] == '.':
                continue
            elif options[0] == '--case-sensitive':
                f = open(file, 'r')
                if pattern in f.read():
                    print('\033[1;32m' + file + '\033[0m')
                    ag_basic(pattern, file, options[0])
                    print()
            else:
                f = open(file, 'r')
                pattern = pattern.lower()
                temp = f.read()
                temp = temp.lower()
                if pattern in temp:
                    print('\033[1;32m' + file + '\033[0m')
                    ag_basic(pattern, file, options[0])
                    print()
    elif len(options) == 2:
        pattern = sys.argv[3]
        file_list = os.listdir()
        file_list = sorted(file_list)
        for file in file_list:
            f = open(file, 'r')
            if pattern in f.read():
                print('\033[1;32m' + file + '\033[0m')
                ag_basic(pattern, file, '--case-sensitive')
                print()


ag()
