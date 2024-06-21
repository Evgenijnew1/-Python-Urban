first = 5
second = 8
third = 8
if first == second == third :
     print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third and first != third:
    print(0)