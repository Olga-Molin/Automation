import pytest

from string_utils import StringUtils

string_util = StringUtils()
# Тест-кейс №1: Делает ли функция "capitalize" первую букву заглавной

@pytest.mark.parametrize('string, result', [
        #позитивные проверки:
        ("olga", "Olga"),
        ("mariAnna", "Marianna"),
        ("mari Anna", "Mari anna"),
        ("mary's", "Mary's"),
        ("petr1", "Petr1"),
        #негативные проверки
        ("Olga", "Olga"),
        ("BMW", "Bmw"),
        ("2024year", "2024year"),
        ("first-timer", "First-timer"),
        ("", "")  
])
    
def test_capitilize(string, result):
       string_util = StringUtils()
       print(f"Input string: {string}")
       print(f"Expected result: {result}")
       res = string_util.capitilize(string)
       print(f"Actual result: {res}")
       assert res == result

#Тест-кейс №2: Удаляет ли функция "trim" пустое пространство перед строкой
@pytest.mark.parametrize('string, result', [
        #позитивные проверки
        ("   cat", "cat"),
        ("   LOL", "LOL"),
        ("  2024", "2024"),
        ("   Nikolay2", "Nikolay2"),
        ("   test-case", "test-case"),
        #негативные проверки
        ("", ""),
        ("ma ma", "ma ma"),
        ("test", "test"),
        ("2024   ", "2024   ")
    ])
def test_trim(string, result):
        string_util = StringUtils()
        print(f"Input string: {string}")
        print(f"Expected result: {result}")
        res = string_util.trim(string)
        print(f"Actual result: {res}")
        assert res == result

#Тест-кейс№3: Преобразует ли функция "to_list" строку в список
@pytest.mark.parametrize('string, divider, result', [
        #позитивные проверки
        ("one,two,three", ",", ["one", "two", "three"]),
        ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
        ("первое,второе,третье", ",", ["первое", "второе", "третье"]),
        #негативные проверки
        ("", None, []),
        ("10,20,30,40")
        ("10, 20, 30, 40, 50", None, ["10", "20", "30", "40 50"])
    ])    
def test_to_list(string, divider, result):
        print(f"Input string: {string}")
        print(f"Expected result: {result}")

        if divider is None:
            res = string_util.to_list(string)
        else:
            res = string_util.to_list(string, divider)
        print(f"Actual result: {res}")
        assert res == result

#Тест-кейс №4 Содержит ли строка искомый символ с помощью функции "contains"
@pytest.mark.parametrize('string, symbol, result', [
        #позитивные проверки
        ("test", "t", True),
        ("pig", "i", True),
        ("Olga", "a", True),
        ("987", "9", True),
        ("ABC", "C", True),
        ("", "", True),
        #негативные проверки
        ("Olga", "f", False),
        ("Olga", "&", False),
        ("city", "C", False),
        ("dog", "8", False),
        ("", "l", False)
    ])   
def test_contains(string, symbol, result):
        string_util = StringUtils()
        print(f"Input string: {string}")
        print(f"Inputed symbol: {symbol}")
        print(f"Expected result: {result}")
        res = string_util.contains(string, symbol)
        print(f"Actual result: {res}")
        assert res == result

# Тест-кейс №5: Удаляет ли функция "delete_symbol" указанный символ
@pytest.mark.parametrize('string, symbol, result', [
        #позитивные проверки
        ("cat", "c", "at"),
        ("Test", "s", "Tet"),
        ("Olga", "a", "Olg"),
        ("204", "2", "04"),
        ("Saint-Petersburg", "-", "SaintPetersburg"),
        ("foto555lab", "555", "fotolab"),
        #негативные проверки
        ("Olga", "d", "Olga"),
        ("", "", ""),
        ("", "f", ""),
        ("soon", "", "soon"),
                     
   ])
def test_delete_symbol(string, symbol, result):
       string_util = StringUtils()
       res = string_util.delete_symbol(string, symbol)
       assert res == result

#Туст-кейс №6: Идентифицирует ли функция "starts_with" начальный символ
@pytest.mark.parametrize('string, symbol, result', [
       #позитивные проверки
       ("soon", "s", True),
       ("", "", True),
       ("Olga", "O", True),
       ("  cat", "", True),
       ("2024", "2", True),
       #негативные проверки
       ("Call", "v", False),
       ("Olga", "o", False),
       ("seven", "n", False),
       ("2024", "0", False)
])    
def test_starts_with(string, symbol, result):
       string_util = StringUtils()
       res = string_util.starts_with(string, symbol)
       assert res == result

#Тест-кейс №7: Идентифицирует ли функция "end_with" конечный символ
@pytest.mark.parametrize('string, symbol, result', [
       #позитивные проверки
       ("end", "d", True),
       ("LESSON", "N", True),
       ("", "", True),
       ("1985", "5", True),
       ("Nikolay2", "2", True),
       ("test ", " ", True),
       #негативные проверки
       ("main", "L", False),
       ("Call", "C", False),
       ("", "k", False),
       ("lasson", "N", False)   
])
def test_end_with(string, symbol, result):
       string_util = StringUtils()
       res = string_util.end_with(string, symbol)
       assert res == result

#Тест-кейс №8: Идентифицирует ли функция "is_empty" пустую строку
@pytest.mark.parametrize('string, result', [
       #позитивные проверки
       ("", True),
       ("  ", True),
       #негативные проверки
       ("line", False),
       ("  Olga", False),
       ("2024", False),
       ("dog  ", False)
])
def test_is_emply(string, result):
       string_util = StringUtils()
       res = string_util.is_empty(string)
       assert res == result

#Тест-кейс №9: Преобразует ли функция "list_to_string" список в строку
@pytest.mark.parametrize('lst, joiner, result', [
    #позитивные проверки:
    (["a", "b", "c"], ",", "a,b,c"),
    ([10, 11, 12, 13, 14], None, "10, 11, 12, 13, 14"),
    (["a", "b", "c"], "", "abc"),
    (["one", "two", "three", "four"], ",", "one,two,three,four"),
    #негативные проверки:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    print(f"Input list: {lst}")
    print(f"Expected result: {result}")
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    print(f"Actual result: {res}")
    assert res == result                    
       
                 