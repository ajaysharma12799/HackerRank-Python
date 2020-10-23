m = int(input())
mInteger = set( map(int, input().split()) )

n = int(input())
nInteger = set( map(int, input().split()) )

result = mInteger.symmetric_difference(nInteger)
value = sorted(result)

for i in value:
    print(i)