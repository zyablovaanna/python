#1. Зяблова Анна МОиАИС 9 группа
# Телефонная книга маленького городка хранит номер абонента по ФИО при помощи
# словаря. Ключом является кортеж «фамилия, имя, отчество». Предусмотреть
# следующие возможности:
# – добавить контакт,
# – удалить контакт,
# – вывести отдельный номер по ФИО человека,
# – вывести весь словарь (ФИО и номер в виде таблицы),
# – напечатать только все ФИО попавших в книгу жителей без номеров,
# – очистить телефонную книгу,
# – при вводе номера 88005553535 программа должна издавать писк и не выполнять
# указанное действие,
# – вывести среднюю длину хранящихся фамилий

abonents_1 = {
           ('Иванов', 'Василий', 'Иванович') : 89514653423,
           ('Васильков', 'Петр', 'Васильевич') : 89006078980,
           ('Сусанин', 'Иван', 'Павлович') : '',
           ('Долгова', 'Ксения', 'Владимировна') : 89002344332, 
           ('Ульянова', 'София', 'Владиславовна') : 89515653423
           }

abonents_2 = {
           ('Иванов', 'Игорь', 'Вячеславович') : 89514653423,
           ('Васильков', 'Петр', 'Васильевич') : 89006078980,
           ('Васильев', 'Иван', 'Павлович') : '',
           ('Петрова', 'Римма', 'Владимировна') : 89002344332, 
           ('Ульянова', 'София', 'Олеговна') : 89515653423
           }
abonents_3 = {}

PHONE = '88005553535'

#ввод выбора пользователя
def input_choice():
    print("1. Добавить контакт" , 
          "2. Удалить контакт",
          "3. Вывести отдельный номер по ФИО человека",
          "4. Вывести весь словарь",
          "5. Напечатать только все ФИО попавших в книгу жителей без номеров",
          "6. Очистить телефонную книгу",
          "7. Вывести среднюю длину хранящихся фамилий",
          "8. Завершение работы", sep = '\n')

    choice = input("Выберите пункт меню: ")

    while True:
        if choice >= '1' and choice <= '8' and len(choice) == 1:
            return choice
        else:
            print("\nНеправильный ввод данных!")
            choice = input("Выберите пункт меню: ")

#проверка правильности ввода номера пользователем (либо пустой, либо с +, либо цифры)
def input_number():
    numb = input("Введите номер телефона абонента (если абонент без номера, нажмите Enter): ")
    while True:
        if (numb == '' or numb.isdigit() or (numb[0]== '+' and numb[1:].isdigit())):
            return numb
        else:
            print("\nНеправильный ввод данных!")
            numb = input("Введите номер телефона абонента (если абонент без номера, нажмите Enter): ")

#добавление контакта + проверка на 88005553535 :))
def add_contact(abonents):
    print("\nВведите данные абонента, которого хотели бы добавить (без пробелов):")
    surname = input("Введите фамилию абонента: ")
    name = input("Введите имя абонента: ")
    patronymic = input("Введите отчество абонента: ")
    number = input_number();
    if (number == PHONE):
        print('\a')
        return
    if (surname, name, patronymic) in abonents and abonents[(surname, name, patronymic)] == number:
        print("\nКонтакт уже записан в телефонную книгу!")
    else:
       abonents[(surname, name, patronymic)] = number
       print("Добавление успешно")

#удаление контакта
def del_contact(abonents):
    print("\nВведите данные абонента, которого хотели бы удалить (без пробелов):")
    surname = input("Введите фамилию абонента: ")
    name = input("Введите имя абонента: ")
    patronymic = input("Введите отчество абонента: ")
    if (surname, name, patronymic) in abonents:
        abonents.pop((surname, name, patronymic))
        print("\nУдаление успешно")
    else:
        print("\nДанный контакт не найден!")

#печать номера абонента, которого выбрал пользователь
def print_number(abonents):
    print("\nВведите данные абонента, номер которого нужно распечатать (без пробелов):")
    surname = input("Введите фамилию абонента: ")
    name = input("Введите имя абонента: ")
    patronymic = input("Введите отчество абонента: ")
    if (surname, name, patronymic) in abonents:
        print(abonents.get((surname, name, patronymic)))
    else:
        print("\nДанный контакт не найден!")

#печать телефонной книги в виде таблицы
def print_dict(abonents):
    print("\n{0:^15} {1:^15} {2:^20} {3:^10}".format("Фамилия", "Имя", "Отчество", "Номер телефона"))
    for s,n,p in abonents:
        print("{0:<15} {1:<15} {2:<20} {3:>10}".format(s,n,p,abonents[s,n,p]))

def print_without_numbers(abonents):
    k = 0
    for s,n,p in abonents:
        if abonents.get((s,n,p)) == '':
            print("{0:<10} {1:<10} {2:<15}".format(s,n,p))
            k+=1
    if k==0:
        print("\nВ словаре нет абонентов, не имеющих номера")
    
#рассчет и печать средней длины хранящихся фамилий
def len_surname(abonents):
    cnt = 0;
    ch = 0;
    print()
    keys = abonents.keys()
    if not keys:
        print("\nСловарь пуст!")
        return
    else:
        for abonent in keys:
            ch += len(abonent[0])
            cnt+=1
        if (cnt!=0):
            res = ch/cnt
            print("\nСредняя длина хранящихся фамилий: %.2f" % res)
        


#основная программа

choice = input_choice()
while choice!='8':
    if choice == '1':
       add_contact(abonents_1)
    elif choice == '2':
       del_contact(abonents_1)
    elif choice == '3':
       print_number(abonents_1)
    elif choice == '4':
       print_dict(abonents_1)
    elif choice == '5':
       print_without_numbers(abonents_1)
    elif choice == '6':
       abonents_1.clear();
    elif choice == '7':
       len_surname(abonents_1)
    print()
    choice = input_choice()
