prev = 1
current = 1
next = 0
while next < 4000000:
    next = prev + current
    if next % 2 == 0:
        sum = sum + next
    print(next)
    prev = current
    current = next

print(sum)

#Answer - 4613732