
def get_multiplied_digits (number):
    str_number= str(number)  # строковое значение чтобы можно было применить оператор [] для доступа по номеру индекса
    first = int(str_number[0])
    if len(str_number)>1:
     return first * get_multiplied_digits(int(str_number[1:]))
    else:
     return first
result1 = get_multiplied_digits(int(str(40203) + str(1)))
print(result1)
result2 = get_multiplied_digits(int(str(503030) + str(1)))
print(result2)


