setA = set(map(int, input().split()))
other_set_length = int(input())
flag = 0
setOther = []
for i in range(other_set_length):
    setOther.append(set(map(int, input().split())))
    if not setA.issuperset(setOther[i]):
        print("False")
        break
else:
    print("True")