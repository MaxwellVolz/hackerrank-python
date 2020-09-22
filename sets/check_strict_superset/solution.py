#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

if __name__ == '__main__':
    set_a = set(input().split())
    N = int(input())
    result = True


    for x in range(N):

        z = set(input().split())
        temp_set_a = set_a
        
        if not temp_set_a.issuperset(z):
            result = False

    print(result)

    