def print_params(a=1, b='строка', c=True):
    print(a,b,c)
# параметры по умолчанию позволяют указывать лишь измененные параметры, ошибки не происходит :
print_params(b=25)
print_params(c = [1,2,3])
values_list = [(1,2,3),9,'параметр']
print_params(*values_list)
values_dict = {'a':True,'b':'Столбец','c':3}
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)