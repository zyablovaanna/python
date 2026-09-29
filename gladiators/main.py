# 5. Написать декоратор «удача» с параметрами N и M: с шансом N% увеличивает результат в M раз.
# Написать класс «Гладиатор» с полями «имя», «здоровье» и «урон». Декорировать геттер урона.
# Задача должна мочь настраивать двух гладиаторов и устраивать поединок между ними.
import gl 

gladiator_1 = None
gladiator_2 = None

#ввод выбора пользователя
def input_choice():
    print("1. Настроить 1-го гладиатора" , 
          "2. Настроить 2-го гладиатора ",
          "3. Настроить гладиаторов из файла",
          "4. Сохранить гладиаторов в файл",
          "5. Вывести показатели гладиаторов",
          "6. Поединок",
          "7. Завершение работы", sep = '\n')

    choice = input("Выберите пункт меню: ")

    while True:
        if choice >= '1' and choice <= '7' and len(choice) == 1:
            return choice
        else:
            print("\nНеправильный ввод данных!")
            choice = input("Выберите пункт меню: ")

#ввод показателя здоровья/урона
def input_int(message):
    while True:
        user_input = input(message)
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Ошибка: число должно быть больше 0!")
        except ValueError:
            print("Ошибка: введите целое число!")


#добавление гладиатора из консоли
def add_gladiator(number):
    global gladiator_1, gladiator_2;
    name = input("Введите имя гладиатора: ")
    health = input_int("Введите кол-во ед. здоровья гладиатора: ")
    damage = input_int("Введите кол-во ед. урона для гладиатора: ")
    gladiator = gl.Gladiator(name, health, damage)
    if (number == 1):
        gladiator_1 = gladiator;
    if (number == 2):
        gladiator_2 = gladiator;


#добавление гладиаторов из файла
def add_gladiators_from_file():
    global gladiator_1, gladiator_2
    file_name = input("Введите имя файла: ");
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as file:
            data = file.readlines();
            if (len(data) >= 2):
                name_1, health_1, damage_1 = data[0].split();
                name_2, health_2, damage_2 = data[1].split();

                health_1 = int(health_1)
                health_2 = int(health_2)
                damage_1 = int(damage_1)
                damage_2 = int(damage_2)
                

                if (health_1 > 0 and health_2 > 0 and damage_1 > 0 and damage_2 > 0):
                    gladiator_1 = gl.Gladiator(name_1, health_1, damage_1)
                    gladiator_2 = gl.Gladiator(name_2, health_2, damage_2)
                    print("Заполнение из файла успешно");
                else:
                    print("Ошибка в данных")
            else:
                print("Ошибка в данных");
    except Exception as e:
        print(f"Ошибка: {e}")

#сохранение гладиаторов в файл
def save_in_file():
    global gladiator_1, gladiator_2

    if not gladiator_1 or not gladiator_2:
        print("Оба гладиатора должны быть созданы")
        return

    file_name = input("Введите имя файла: ");
    try:
        with open(file_name, 'w', encoding='utf-8-sig') as file:
            file.write(f"{gladiator_1.name} {gladiator_1.health} {gladiator_1.damage}\n")
            file.write(f"{gladiator_2.name} {gladiator_2.health} {gladiator_2.damage}")
            print("Сохранение успешно")
    except Exception as e:
        print(f"Ошибка: {e}")

#печать гладиаторов
def show_gladiators():
    if gladiator_1:
        print(gladiator_1)
    else:
        print("Гладиатор 1 не настроен")
    if gladiator_2:
        print(gladiator_2)
    else:
        print("Гладиатор 2 не настроен")


#поединок
def duel():
    if not gladiator_1 or not gladiator_2:
        print("Оба гладиатора должны быть созданы")
        return
    r = 1;
    name1 = gladiator_1.name
    name2 = gladiator_2.name

    or_health1 = gladiator_1.health;
    or_health2 = gladiator_2.health

    while (gladiator_1.health > 0 and gladiator_2.health > 0):
        damage1 = gladiator_1.damage;
        damage2 = gladiator_2.damage;
        print(f"Раунд {r} Здоровье гладиаторов: гладиатор {name1} : {gladiator_1.health}, гладиатор {name2} : {gladiator_2.health} ")

        gladiator_2.take_damage(damage1);
        print(f"После удара гладиатора {name1} с уроном {damage1} здоровье гладиатора {name2} {gladiator_2.health}")
        if (gladiator_2.health == 0):
            break
        gladiator_1.take_damage(damage2);

        print(f"После удара гладиатора {name2} с уроном {damage2} здоровье гладиатора {name1} {gladiator_1.health}")

        print();
        r+=1;

    print("Поединок завершен!")
    if (gladiator_1.health > 0):
        print(f"Победитель - гладиатор {name1}")
    if (gladiator_2.health > 0):
        print(f"Победитель - гладиатор {name2}")
    gladiator_1.health = or_health1;
    gladiator_2.health = or_health2;


#main
choice = input_choice()
while choice!='7':
    if choice == '1':
       add_gladiator(1);
    elif choice == '2':
       add_gladiator(2);
    elif choice == '3':
       add_gladiators_from_file();
    elif choice == '4':
       save_in_file();
    elif choice == '5':
       show_gladiators();
    elif choice == '6':
       duel();
    print()
    choice = input_choice()
