def polindrom(a):
    b = a[::-1]
    if (a == b):
        print("yes")
    else:
        print("no")

#a = input("1 slovo ")
#polindrom(a)

#-----------------------------------------

import time
import random

def on_time_game():
    target = random.randint(2,6)
    print('\n Your target is {} seconds', format(target))

    input("--Press Enter to begin--")
    start = time.perf_counter()

    input("\n .... Enter to stop")
    elapsed = time.perf_counter() - start

    print('\n elapsed time is {0:.3f}'.format(elapsed))

    if elapsed == target:
        print('you win')
    elif elapsed < target:
        print("your rano for {0:.3f}".format(target-elapsed))
    elif elapsed > target:
        print("your late for {0:.3f}".format(elapsed-target))

#on_time_game()

#-----------------------------------------
#простые множители

def deliteli(a):
    for i in range(2,a//2+1):
        if a % i == 0:
            f = 0
            for j in range(2,i//2+1):
                if (i % j == 0):
                    f = 1
            if (f == 0):
                print(i, end=" ")

def get_prime_factors(a):
    factors = []
    division = 2
    while(division <= a):
        if (a % division) == 0:
            factors.append(division)
            a = a/division
        else:
            division += 1
    return factors


a = int(input())

print(get_prime_factors(a))
deliteli(a)

#-----------------------------------------