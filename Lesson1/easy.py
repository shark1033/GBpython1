__author__ = 'Украинцев Антон Вячеславович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

def first_task_for():
    number=input()
    for i in number:
        print(i+" ", end="  ")

def first_task_while(): #использована арифметика + цикл while
    number = input()
    lenght=len(number)
    number=int(number)
    delim="1"
    for i in range(0,lenght-1):
        delim+="0"

    print(delim)
    if lenght==1:
        print(number)
        return None
    delim=int(delim)

    counter=1
    while True:
        cur_num=number//delim #first number
        print("Цифра №" + str(counter) + " - " +str(cur_num))

        number=number%delim
        #print(number)
        delim = delim // 10
        counter+=1


        if len(str(number)) == 1:
            number = str(number)
            number = number[-1]
            print("Цифра №"+str(counter)+" - " + number)
            break


#first_task_for()
#first_task_while()


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

def second_task_math():
    n, k=[int(i) for i in input().split()]
    n=n-k
    k=k+n
    n=k-n
    print(n, k)
def second_task_variable():
    n, k = [int(i) for i in input().split()]
    x=n
    n=k
    k=x
    print(n, k)

#second_task_variable()


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
def third_task():
    age=input()
    if age>=18:
        print("Доступ разрешен")
    else:
        print("Извините, пользование данным ресурсом только с 18 лет")