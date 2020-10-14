#!/bin/python3

import math
import os
import random
import re
import sys

def weird_notweird(value):
    if value % 2 != 0:
        print("Weird")
    if value % 2 == 0 and ( value >= 2 and value <= 5 ):
        print("Not Weird")
    if value % 2 == 0 and ( value >= 6 and value <= 20 ):
        print("Weird")
    if value % 2 == 0 and value > 20:
        print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    weird_notweird(n)