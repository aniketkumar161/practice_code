# Break & Continue

# Break for multiple of 6
i = 1

while i <= 10:
    if(i % 6 == 0):
        break
    print(i)           # 1, 2, 3, 4, 5, break
    i += 1

# Skip multiples of 3
i = 0

while(i < 10):
    i += 1
    if(i % 3 == 0):
        continue;      # 1, 2, continue, 4, 5, continue, 7, 8, continue, 10
    print(i)

# Print odd nums from 1 to 10 using continue
i = 0

while(i < 10):
    i += 1
    if(i % 2 == 0):
        continue;      # 1, 3, 5, 7, 9
    print(i)

    