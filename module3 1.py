calls = 0
def count_calls():
    global calls
    calls +=1
    return calls

def string_info(string):
    count_calls()
    s= [len(string),string.upper(),string.lower()]
    return s

def is_contains(string,list_to_search):
    count_calls()
      # return string.lower in [s.lower() for s in list_to_search]
    for i in range(len(list_to_search)):
       if string.upper() in list_to_search[i].upper():
        return True
    return False
    # return string.lower in [s.lower() for s in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)