#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

vowels = "AEIOU"
def minion_game(string):
    # your code goes here
    kevin_score = 0
    stuart_score = 0

    stuart_words = set()
    kevin_words = set()

    for x in range(len(string)):

        for y in range(len(string)):
            # print(string[x:y])

            if string[x] not in vowels:
                stuart_words.add(string[x:y+1])
            if string[x] in vowels:
                kevin_words.add(string[x:y+1])

    stuart_words.remove('')
    kevin_words.remove('')
   
    for x in stuart_words:
        start = 0

        while start < len(string):
            pos = string.find(x,start)

            if pos != -1:
                start = pos+1
                stuart_score += 1
            else:
                break

    for x in kevin_words:
        start = 0

        while start < len(string):
            pos = string.find(x,start)

            if pos != -1:
                start = pos+1
                kevin_score += 1
            else:
                break

    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif stuart_score > kevin_score:
        print('Stuart', stuart_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)