my_dict = {'Victor': 1999, 'Oleg': 2014,"Michail":2005}
print('Dict:',my_dict)
print('Existing value:',my_dict.get('Oleg'))
print('Not existing value:',my_dict.get('Olga'))
my_dict.update({'Petro':2005,'Udro':2008})
print('Deleted value:',my_dict.pop('Victor'))
print('Modified dictionary:',my_dict)
print('         ')
my_set = {1,1,8,8,8,'true','true',True,(1,8,True)}
print('Set:',my_set)
my_set.discard(8)
my_set.update((9,11))
print('Modified Set:',my_set)