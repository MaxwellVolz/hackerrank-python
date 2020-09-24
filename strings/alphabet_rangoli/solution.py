#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

alphabet = "abcdefghijklmnopqrstuvwxyz&"

def print_rangoli(size):
    # your code goes here
    rangoli_width = size*4-3
    rangoli_height = size*2-1
    center = int(rangoli_width / 2)

    output_lines = []

    for x in range(size):
        letters = alphabet[size-x-1:size]
        letters = letters[::-1] + letters[1:]
        output_lines.append(letters)

    output_lines = output_lines[:-1] + output_lines[::-1]

    # print(output_lines)

    for line in output_lines:
        print('-'.join(list(line)).center(rangoli_width,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)