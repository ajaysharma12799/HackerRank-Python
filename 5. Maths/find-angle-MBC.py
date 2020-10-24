from math import *
AB = float(input())
BC = float(input())
deg = int(round(degrees(atan(AB/BC)),0))
print(str(deg)+'°')