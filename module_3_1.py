calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(s):
    answer = (len(s), s.upper(), s.lower())
    count_calls()
    return answer

def is_contains(s, l):
    flag = False
    for text in l:
        if text.lower() == s.lower():
            flag = True
            break
    count_calls()
    return flag

print(string_info('Pizza'))
print(string_info('Project'))
print(is_contains('urBan', ['URBaN', 'InDeX', 'speach']))
print(is_contains('LoW', ['lower', 'UPPER']))
print(calls)