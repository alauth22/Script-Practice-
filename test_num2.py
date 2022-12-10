def times_num(num):
    final_num = num * 4
    return final_num

def square_num(num):
    return(num**2)

def letter_num(num):
    return ["X" for i in range(num)]

def name_num(num):
    for i in range(num):
        result = i * "X"
    return(result)