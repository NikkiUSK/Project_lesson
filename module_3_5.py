def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        if first == 0:
            return int(str_number)
        else:
            n = first * get_multiplied_digits(int(str_number[1:]))
            return n
    elif int(str_number) == 0:
        return 1
    else:
        return int(str_number)

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)



