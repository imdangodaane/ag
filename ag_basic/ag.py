import sys


def find_index_of_found_pattern(pattern, line):
    current_index = 0
    while True:
        current_index = line.find(pattern, current_index)
        if current_index == -1:
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


def ag():
    if len(sys.argv) == 4:
        option = sys.argv[1]
        pattern = sys.argv[2]
        file_name = sys.argv[3]
        num = 0
        count = 0
        list_index_of_pattern = []

        f = open(file_name, 'r')
        lines = f.read().split('\n')[:-1]

        for line in lines:
            num += 1
            if option == '--case-sensitive':
                compare = line
                list_index_of_pattern = into_a_list(pattern, compare)
                if len(list_index_of_pattern) == 0:
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
            elif option != '--case-sensitive':
                pattern = pattern.lower()
                compare = line.lower()
                list_index_of_pattern = into_a_list(pattern, compare)
                if len(list_index_of_pattern) == 0:
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

    else:
        pattern = sys.argv[1]
        pattern = pattern.lower()
        file_name = sys.argv[2]
        num = 0
        count = 0
        list_index_of_pattern = []

        f = open(file_name, 'r')
        lines = f.read().split('\n')[:-1]

        for line in lines:
            num += 1
            compare = line.lower()
            list_index_of_pattern = into_a_list(pattern, compare)
            if len(list_index_of_pattern) == 0:
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


ag()
