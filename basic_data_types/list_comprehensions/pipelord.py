#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# pipelord.py
import sys

def read_input():
    lines = [line.rstrip('\n') for line in open('sample_input_0.txt')]
    for my_line in lines:
        sys.stdout.write(my_line)
        sys.stdout.write("\n")

read_input()