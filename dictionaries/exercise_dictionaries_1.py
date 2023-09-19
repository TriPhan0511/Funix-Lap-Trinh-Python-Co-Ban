import os


def check_existing(file_name, s):
    absolute_path = os.path.dirname(__file__)
    # relative_path = 'src/lib'
    # full_path = os.path.join(absolute_path, relative_path)
    try:
        fhand = open(f'{absolute_path}/{file_name}')
        d = {}

        # for line in fhand:
        #     line = line.strip()
        #     words = line.split(' ')
        #     if len(words) < 2:
        #         continue
        #     for word in words:
        #         word = word.lower()
        #         if word not in d:
        #             d[word] = 1
        #         else:
        #             d[word] += 1
        lines = [line.strip() for line in fhand]
        words = [word.split(' ') for word in lines]

        print(words)

        for line in fhand:
            line = line.strip()
            words = line.split(' ')
            if len(words) < 2:
                continue
            for word in words:
                word = word.lower()
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1

        # print(d)
        return s in d

    except FileNotFoundError:
        return


def main():
    file_name = 'words.txt'
    # s = 'abc' # False
    s = 'book'  # True
    print(check_existing(file_name, s))


if __name__ == '__main__':
    main()
    # list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # numbers = [number for lst in list_of_list for number in lst]
    # print(numbers)
