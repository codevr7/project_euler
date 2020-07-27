# A sub code for the program prime pair
# Code for returning first prime after given number

import math

def next_prime(num):
    val = num 
    while True:
        val += 1
        if is_prime(val):
            return val

def is_prime(num):
    for i in range(int(math.sqrt(num)), 1, -1):
        if num%i == 0:
            return False
    return True
