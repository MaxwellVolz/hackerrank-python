#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

if __name__ == '__main__':
    set_a = set(input().split())
    N = int(input())
    result = True


    for x in range(N):

        z = set(input().split())
        temp_set_a = set_a

        # print([p for p in temp_set_a if p in z])

        if not temp_set_a.issuperset(z):
            result = False


        # for i in z:


        #     try:
        #         temp_set_a.remove(i)
        #     except ValueError:
        #         print('ValueError')
        #         result = False

        #     if len(temp_set_a) == 0:
        #         result = False

    print(result)

    