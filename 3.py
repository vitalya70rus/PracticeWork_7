def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

sequence = [8,9,-10,12,11]
bubble_sort(sequence)
for num in sequence:
    if num / 10 >= 1:
        print(num)