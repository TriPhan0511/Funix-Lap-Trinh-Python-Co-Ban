##
# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:

# X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

# Test your file on the mbox.txt and mbox-short.txt files.
#

def compute_average_spam_confidence():
    while True:
        file_name = input('\nEnter a file_name:\n')
        try:
            fhand = open(file_name)
        except FileNotFoundError:
            print('\nFile cannot be found.\nPlease enter another file name.')
            continue
        else:
            count = 0
            total = 0
            searched_str = 'X-DSPAM-Confidence:'
            for line in fhand:
                if not line.startswith(searched_str):
                    continue
                total += float(line[len(searched_str) + 1:])
                count += 1
            break
    if count != 0:
        print(f'\nAverage spam confidence: {(total / count):.12f}')
    else:
        print('\nCannot find any spam confidence.')


if __name__ == '__main__':
    compute_average_spam_confidence()
