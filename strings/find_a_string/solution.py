#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

def count_substring(string, sub_string):
    occurences = 0
    sub_string_length = len(sub_string)
    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            if sub_string in string[i:i+sub_string_length]:
                occurences = occurences + 1

    return occurences

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)