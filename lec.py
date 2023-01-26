import time
import string
import secrets

print()
print("ТЕЛЕФОННЫЙ СПРАВОЧНИК_v1")

# создание файла 
filename = "Tel_book.csv" 
myfile = open(filename, "a+") 
myfile.close
 
# метод главного меню 
def main_menu(): 
    print( "\nГЛАВНОЕ МЕНЮ\n") 
    print( "1. Просмотреть все существующие контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Найти существующий контакт") 
    print( "4. Выход") 
    choice = input("Выберите пункт меню: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "Искомый контакт не обнаружен, сожалею") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Для продолжения нажмите Enter") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Для продолжения нажмите Enter") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Для продолжения нажмите Enter") 
        main_menu() 
    elif choice == "4": 
        print("Спасибо, что используете телефонный справочник!") 
    else: 
        print( "Пожалуйста, повторите ввод\n") 
        enter = input("Для продолжения нажмите Enter")
        main_menu()
 
# метод поиска         
def searchcontact(): 
    searchname = input("Введите ИМЯ для поиска контакта: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print("По вашему запросу найден контакт: ", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print(f"Контакт {searchname} не найден в справочнике, сожалею") 
 
# имя 
def input_firstname(): 
    first = input("Введите ваше имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# фамилия 
def input_lastname(): 
    last = input("Введите вашу фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname

# метод генерации ключа
def key_gen():
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for i in range(4))
    return key
key = key_gen()
 
# сохранение новых данных контакта 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input("Введите ваш номер телефона: ") 
    emailID = input("Введите ваш E-mail: ") 
    contactDetails =(f"{key};" + firstname + " " + lastname + ";" + phoneNum + ";" + emailID +  "\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print("Новая запись в телефонном справочнике: \n " + contactDetails + " успешно создана!")  
 
main_menu()
time.sleep(5)