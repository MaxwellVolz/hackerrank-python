#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[a,b,c] for a in list(range(x+1)) for b in list(range(y+1)) for c in list(range(z+1)) if a+b+c != n])