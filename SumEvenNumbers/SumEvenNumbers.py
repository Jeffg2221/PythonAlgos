def sum_even(arr):
    sum = 0
    for num in arr:
        if num % 2 ==0:
            sum += num
    print(sum)
    return sum


array = [1,2,3,4]
sum_even(array)
# print(sum_even(array))