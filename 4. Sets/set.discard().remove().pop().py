n = int(input())
s = set(map(int, input().split()))
set_sum = 0
number_of_command = int(input())
for i in range(number_of_command):
    choice = input().split()
    if choice[0] == "pop":
        s.pop()
    elif choice[0] == "remove":
        s.remove(int(choice[1]))
    elif choice[0] == "discard":
        s.discard(int(choice[1]))


print(sum(s))