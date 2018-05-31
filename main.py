#!usr/bin/env python3.6

# Date: 02-22-18, Feb ~ 22nd 2018 | Synchronocy
# Project: Simpsons Law
# Just did this for a student
# IDLE Python 3.6 64-bit

def calc(a,b,c,d):
    a = a / 3
    e = a *(b + (4*c) +d)
    print(e)

def main():
    a = input("Everything By: ")
    b = input("L Zero: ")
    c = input("L One: ")
    d = input("L Two: ")
    calc(a,b,c,d)

if __name__ == '__main__':
  main()
