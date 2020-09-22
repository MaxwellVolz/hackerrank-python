#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

def print_formatted(number):
    # your code goes here
    spacer = len(bin(number)) - 1

    for x in range(number):
        print('{decimal}{octal}{hexadecimal}{binary}'.format(
        decimal=str(x+1).rjust(spacer-1), 
        octal=oct(x+1)[2:].rjust(spacer),
        hexadecimal=hex(x+1)[2:].rjust(spacer).upper(),
        binary=bin(x+1)[2:].rjust(spacer)))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



