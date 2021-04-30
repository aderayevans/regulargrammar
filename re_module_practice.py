import re

def check_capital(char_member):
    if ord(char_member) >= 65 and ord(char_member) <= 90:
        return True
    return False
def check_endline(char_member):
    if char_member == '.' or check_capital(char_member):
        return True
    return False
def check_doublespace(char_member):
    if char_member == ' ':
        return True
    return False
def check_grammar():
    for line_num in range(0, len(line_list)):
        for char_num in range (0, len(line_list[line_num])):
            if char_num == 0:
                if check_capital(line_list[line_num][char_num]) == False:
                    print("TypeError (capital the first char needed) in line %d" % (line_num + 1))
            if char_num == len(line_list[line_num]) - 1:
                if check_endline(line_list[line_num][char_num]) == False:
                    print("TypeError (dot or capital in the end needed) in line %d" % (line_num + 1))
            if line_list[line_num][char_num] == ' ' and char_num < len(line_list[line_num])-1:
                if check_doublespace(line_list[line_num][char_num+1]):
                    print("TypeError (double space found) in line %d" % (line_num + 1))
            if check_capital(line_list[line_num][char_num]) and char_num < len(line_list[line_num])-1:
                if check_capital(line_list[line_num][char_num+1]):
                    print("TypeError (double capital found) in line %d" % (line_num + 1))
def replace_str():
    global _str_
    temp_str = (_str_ + '.')[:-1]
    temp_str = temp_str.replace(".", ' ')
    temp_str = temp_str.replace("@", ' ')
    temp_str = temp_str.replace("<", ' ')
    temp_str = temp_str.replace(">", ' ')
    temp_str = temp_str.replace("/", ' ')
    return temp_str
def split_up_into_words():
    temp_str = replace_str()
    word_list = re.split(r'\s', temp_str)
    while '' in word_list:
        word_list.remove('')
    return word_list
def split_up_into_lines():
    global _str_
    line_list = re.split(r'\n', _str_)
    return line_list
def search_word(reg_):
    global word_list
    found_list = []
    for num in range (0, len(word_list)):
        found = re.findall(reg_, word_list[num])
        if found != []:
            found_list.append(found[0])
    print(found_list)
def search_line(reg_):
    global line_list
    found_list = []
    for num in range (0, len(line_list)-1):
        found = re.findall(reg_, line_list[num])
        if found != []:
            found_list.append(found[0])
    print(found_list)
def replace_word(reg_, hint):
    global word_list
    temp_word_list = word_list.copy()
    print("Before replace:\n")
    print(temp_word_list)
    for wordnum in range (0, len(temp_word_list)):
        temp_word_list[wordnum] = re.sub(reg_, hint, temp_word_list[wordnum])
    print("\nAfter replace:\n")
    print(temp_word_list)
def func_1():
    print (">> A list of words containing 'a-z' and '0-9':\n")
    reg_ = r'\w*[a-z]+\d+|\d+[a-z]+\w*'
    search_word(reg_)
def func_2():
    print ("\n>> A list of words containing 'a' followed by 'b'*:\n")
    reg_ = r'\w*ab*\w*'
    search_word(reg_)
def func_3():
    print ("\n>> A list of words starting with 'a' and ending with 'b':\n")
    reg_ = r'^a.*b$'
    search_word(reg_)
def func_4():
    print ("\n>> A list of words containing only 'a-z' and '_':\n")
    reg_ = r'^[a-z]+_+$'
    search_word(reg_)
def func_5():
    print ("\n>> A list of words containing only 'a-z' and '_':\n")
    reg_ = r'^.{5}$'
    search_word(reg_)
def func_6():
    print ("\n>> A list of words containing 'h':\n")
    reg_ = r'.*h+.*'
    search_word(reg_)
def func_7():
    print ("\n>> A list of words starting with [0-9]:\n")
    reg_ = r'^\d+.*'
    search_word(reg_)
def func_8():
    print ("\n>> Replace '_' with ' ':\n")
    reg_ = r'[_]+'
    hint = ' '
    replace_word(reg_, hint)
def func_9():
    print ("\n>> Replace mm-dd-yy with dd-mm-yy:\n")
    reg_ = r'(\w+)-(\w+)-(\w+)'
    hint = '\\2-\\1-\\3'
    replace_word(reg_, hint)
def func_10():
    print ("\n>> Lines starting with 't' or 'h' and containing 're':\n")
    reg_ = r'^[t|h].*re+.*'
    search_line(reg_)
def func_11():
    print ("\n>> A list of words containing at least 20 characters:\n")
    reg_ = r'.{20,}'
    search_word(reg_)
def func_12():
    print ("\n>> A list of words ending with '?!':\n")
    reg_ = r'.*[?!]+$'
    search_word(reg_)
def func_13():
    print ("\n>> Lines containing 'a' 'r' 's' 'm' 'l' no need to continuous:':\n")
    reg_ = r'.*a+.*r+.*s+.*m+.*l+.*'
    search_line(reg_)
def func_14():
    print ("\n>> Lines not containing ',' and '.':\n")
    reg_ = r'^[^\.|^,]+$'
    search_line(reg_)
def func_15():
    print ("\n>> Lines containing 'mouse':\n")
    reg_ = r'.*mouse+.*'
    search_line(reg_)
def func_16():
    print ("\n>> A list of words containing 'a'+ followed by 'b':\n")
    reg_ = r'\w*ab\w*'
    search_word(reg_)
def func_17():
    print ("\n>> Domain:\n")
    reg_ = r'(\w+)@\w+[\.\w+]+'
    search_line(reg_)
def func_18():
    print ("\n>> Betweem <head> and </head>:\n")
    reg_ = r'<head>(.*)</head>'
    search_line(reg_)


f = open('BT3.txt', 'r')
_str_ = f.read()
line_list = split_up_into_lines()
check_grammar()
word_list = split_up_into_words()
func_1()
func_2()
func_3()
func_4()
func_5()
func_6()
func_7()
func_8()
func_9()
func_10()
func_11()
func_12()
func_13()
func_14()
func_15()
func_16()
func_17()
func_18()