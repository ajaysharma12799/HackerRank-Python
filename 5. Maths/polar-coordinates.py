import math
import cmath

complex_number = complex(input())
x, y = (complex_number.real, complex_number.imag)

r = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
symbol = cmath.phase(complex_number)

print(r)
print(symbol)