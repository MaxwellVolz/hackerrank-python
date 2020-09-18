#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# sample_input_0.py

if __name__ == '__main__':
    N = int(input())

    li = []

    # for x in input().split('\n'):
    for x in range(1,N+1):

        command = input()
        
        if(command == 'print'):
            print(li)
        elif(command == 'reverse'):
            li.reverse()
        elif(command == 'pop'):
            li.pop()
        elif(command == 'sort'):
            li.sort()
        else:
            command = command.split()
            if(command[0] == 'insert'):
                li.insert(int(command[1]),int(command[2]))
            elif(command[0] == 'remove'):
                li.remove(int(command[1]))
            elif(command[0] == 'append'):
                li.append(int(command[1]))