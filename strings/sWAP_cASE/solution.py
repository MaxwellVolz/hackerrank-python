#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

def swap_case(s):
    return str(s).swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)