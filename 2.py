my_list = [(1, 5), (3, 2), (7, 8)]

def output_list(my_list):
    result = []
    for x, y in my_list:
        result.append((y, x))
    return result

print(output_list(my_list))
