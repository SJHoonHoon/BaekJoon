a=int(input())
b=list(map(int, input().split()))

b.sort()

total=0
total2=0

for i in b:
    total = total + i
    total2 = total + total2

print(total2)