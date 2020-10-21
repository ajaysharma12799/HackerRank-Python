n = int(input())
country = []

for _ in range(n):
    country.append(input())

convertedSet = set(country)
print(len(convertedSet))