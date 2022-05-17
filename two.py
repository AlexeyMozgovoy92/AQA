def find_min_number(num_1, num_2, num_3):

    if num_1 < num_2 and num_1 < num_3:
        return num_1
    elif num_2 < num_3 and num_2 < num_1:
        return num_2
    elif num_3 < num_2 and num_3 < num_1:
        return num_3
    else:
        return "все числа равны"

