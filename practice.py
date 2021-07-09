import sys

import ...
# головной модуль
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
keywords = ['and', 'array', 'begin', 'case', 'const', 'div', 'do', 'downto', 'else', 'end', 'file', 'for', 'function',
             'goto', 'if', 'in', 'label', 'mod', 'nil', 'not', 'of', 'or', 'packed', 'procedure', 'program', 'record',
             'repeat', 'set', 'then', 'to', 'type', 'until', 'var', 'while', 'with']
value_type = ['boolean', 'byte', 'char', 'integer', 'longint', 'real', 'string', 'word']


# блок ввода данных
def string_input():
    file = open("input.txt", "r")
    string = file.readline()
    file.close()
    return string


# блок транслитерации
def transliteration(string):
    string = string_format(string)
    symbol_list = []                # список ("символ цепочки", "класс символа цепочки ")
    for i in range(len(string)):
        temp = []
        temp.append(string[i])
        if string[i] in alphabet:
             temp.append("буква")
        elif string[i] in number:
            temp.append("цифра")
        elif string[i] == "_":
            temp.append("подчерк")
        elif string[i] == ":":
            temp.append("двтч")
        elif string[i] == ";":
            temp.append("тчкзпт")
        elif string[i] == ",":
            temp.append("зпт")
        elif string[i] == "[":
            temp.append("скобка [")
        elif string[i] == "]":
            temp.append("скобка ]")
        elif string[i] == " ":
            temp.append("пробел")
        else:
            return 0
        symbol_list.append(temp)
    return symbol_list


# блок преобразования строки
def string_format(string):
    string = string.lower()         # переводим в нижний регистр
    string = string.strip()         # удаляем пробелы перед строкой и после нее
    return string


# лексический блок
def lexical_block(raw_list):
    global temp
    lexical_list = []               # список ("символ входного языка", "класс символа входного языка")
    i = 0                           # индекс символа, который сейчас обрабатывается
    status = "нач"                  # состояние распознавателя

    while i < len(raw_list):
        if status == "нач":
            if raw_list[i][1] == "буква":
                temp = raw_list[i][0]
                status = "клслово"
                i += 1
            else:
                return 0
        elif status == "клслово":
            while raw_list[i][1] == "буква":
                temp += raw_list[i][0]
                i += 1
            lexical_list.append([temp,  keyword_recognize(temp)])
            if raw_list[i][1] == "пробел":
                status = "пробел1"
                i += 1
            else:
                return 0
        elif status == "пробел1":
            if raw_list[i][1] == "пробел":
                i += 1
            elif raw_list[i][1] == "буква":
                temp = raw_list[i][0]
                status = "имя"
                i += 1
            else:
                return 0
        elif status == "имя":
            while raw_list[i][1] == "буква" or raw_list[i][1] == "цифра" or raw_list[i][1] == "подчерк":
                temp += raw_list[i][0]
                i += 1
            lexical_list.append([temp,  keyword_recognize(temp)])
            if raw_list[i][1] == "пробел":
                status = "пробел2"
                i += 1
            elif raw_list[i][1] == "зпт":
                lexical_list.append([raw_list[i][0], "зпт"])
                status = "зпт"
                i += 1
            elif raw_list[i][1] == "двтч":
                lexical_list.append([raw_list[i][0], "двтч"])
                status = "двтч"
                i += 1
            else:
                return 0
        elif status == "пробел2":
            if raw_list[i][1] == "пробел":
                i += 1
            elif raw_list[i][1] == "зпт":
                lexical_list.append([raw_list[i][0], "зпт"])
                status = "зпт"
                i += 1
            elif raw_list[i][1] == "двтч":
                lexical_list.append([raw_list[i][0], "двтч"])
                status = "двтч"
                i += 1
            else:
                return 0
        elif status == "зпт":
            if raw_list[i][1] == "буква":
                temp = raw_list[i][0]
                status = "имя"
                i += 1
            elif raw_list[i][1] == "пробел":
                i += 1
            else:
                return 0
        elif status == "двтч":
            if raw_list[i][1] == "буква":
                temp = raw_list[i][0]
                status = "тип"
                i += 1
            elif raw_list[i][1] == "пробел":
                i += 1
            else:
                return 0
        elif status == "тип":
            while raw_list[i][1] == "буква":
                temp += raw_list[i][0]
                i += 1
            lexical_list.append([temp, keyword_recognize(temp)])
            if raw_list[i][1] == "пробел":
                status = "пробел5"
                i += 1
            elif raw_list[i][1] == "скобка [":
                lexical_list.append([raw_list[i][0], "скобка ["])
                status = "скобка1"
                i += 1
            elif raw_list[i][1] == "тчкзпт":
                lexical_list.append([raw_list[i][0], "тчкзпт"])
                status = "тчкзпт"
                i += 1
            else:
                return 0
        elif status == "пробел5":
            if raw_list[i][1] == "пробел":
                i += 1
            elif raw_list[i][1] == "скобка [":
                lexical_list.append([raw_list[i][0], "скобка ["])
                status = "скобка1"
                i += 1
            elif raw_list[i][1] == "тчкзпт":
                lexical_list.append([raw_list[i][0], "тчкзпт"])
                status = "тчкзпт"
                i += 1
            else:
                return 0
        elif status == "скобка1":
            if raw_list[i][1] == "цифра":
                temp = raw_list[i][0]
                status = "длина"
                i += 1
            elif raw_list[i] == "пробел":
                i += 1
            else:
                return 0
        elif status == "длина":
            while raw_list[i][1] == "цифра":
                temp += raw_list[i][0]
                i += 1
            lexical_list.append([temp, "длина"])
            if raw_list[i][1] == "пробел":
                status = "пробел7"
                i += 1
            elif raw_list[i][1] == "скобка ]":
                lexical_list.append([raw_list[i][0], "скобка ]"])
                status = "скобка2"
                i += 1
            else:
                return 0
        elif status == "пробел7":
            if raw_list[i][1] == "пробел":
                i += 1
            elif raw_list[i][1] == "скобка ]":
                lexical_list.append([raw_list[i][0], "скобка ]"])
                status = "скобка2"
                i += 1
            else:
                return 0
        elif status == "скобка2":
            if raw_list[i][1] == "пробел":
                i += 1
            elif raw_list[i][1] == "тчкзпт":
                lexical_list.append([raw_list[i][0], "тчкзпт"])
                status = "тчкзпт"
                i += 1
            else:
                return 0
        elif status == "тчкзпт":
            if raw_list[i][1] == "пробел":
                i += 1
            else:
                return 0
    return lexical_list


# блок идентификации ключевых слов
def keyword_recognize(word):
    if word == "var":
        return "клслово_var"
    elif word in keywords:
        return "клслово"
    elif word in value_type:
        return "тип"
    else:
        return "идент"


# синтаксический блок
def syntax_block(raw_list):
    error = False               # наличие ошибки
    status = "нач"              # состояние автомата
    i = 0                       # индекс обрабатываемой лексемы
    while i < len(raw_list):
        if status == "нач":
            if raw_list[i][1] == "клслово_var":
                status = "var"
                i += 1
            else:
                error = True
                return error
        elif status == "var":
            if raw_list[i][1] == "идент":
                status = "имя"
                i += 1
            else:
                error = True
                return error
        elif status == "имя":
            if raw_list[i][1] == "зпт":
                status = "зпт"
                i += 1
            elif raw_list[i][1] == "двтч":
                status = "двтч"
                i += 1
            else:
                error = True
                return error
        elif status == "зпт":
            if raw_list[i][1] == "идент":
                status = "имя"
                i += 1
            else:
                error = True
                return error
        elif status == "двтч":
            if raw_list[i][1] == "тип":
                status = "тип"
                i += 1
            else:
                error = True
                return error
        elif status == "тип":
            if raw_list[i][1] == "скобка [":
                status = "скобка1"
                i += 1
            elif raw_list[i][1] == "тчкзпт":
                status = "тчкзпт"
                i += 1
            else:
                error = True
                return error
        elif status == "скобка1":
            if raw_list[i][1] == "длина":
                status = "длина"
                i += 1
            else:
                error = True
                return error
        elif status == "длина":
            if raw_list[i][1] == "скобка ]":
                status = "скобка2"
                i += 1
            else:
                error = True
                return error
        elif status == "скобка2":
            if raw_list[i][1] == "тчкзпт":
                status = "тчкзпт"
                i += 1
            else:
                error = True
                return error
        elif status == "тчкзпт":
            i += 1
    if status == "тчкзпт":
        return error
    else:
        error = True
        return error


# блок вывода данных
def output(string, error):
    file = open("output.txt", "w")
    if not error:
        file.write(string + "\t\tACCEPT")
    else:
        file.write(string + "\t\tREJECT")
    file.close()


# основная программа
original_string = string_input()
if not original_string:
    output(original_string, 1)
    sys.exit()

translit_list = transliteration(original_string)
if not translit_list:
    output(original_string, 1)
    sys.exit()

lexical_list = lexical_block(translit_list)
if not lexical_list:
    output(original_string, 1)
    sys.exit()

output(original_string, syntax_block(lexical_list))
