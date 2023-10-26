def largest_subarray_sum(input_list):
    i = len(input_list)
    result = 0
    sub_array_sum = 0


    for l in range(0, i):
        for j in range(l, i):



            result += input_list[j]
            if result > sub_array_sum:
                sub_array_sum = result
        result = 0

    print(sub_array_sum)


input_list = [1, -2, 3, 10, -4, 7, 2, -5]
largest_subarray_sum(input_list)






