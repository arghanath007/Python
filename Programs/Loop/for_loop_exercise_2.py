dice_result = [5, 6, 4, 2, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 5]
count_6 = count_1 = count_66 = 0
for i in dice_result:
    if i == 6:
        count_6 += 1
    if i == 1:
        count_1 += 1
    if i == 6 and (i+1) == 6:
        count_66 += 1

print(f'Count of 6s is {count_6}')
print(f'Count of 1s is {count_1}')
print(f'Count of two 6s in a row is {count_66}')
