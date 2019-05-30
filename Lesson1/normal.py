__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

def first_task_while(): #использована арифметика + цикл while
    number = input()
    lenght=len(number)
    number=int(number)
    delim="1"
    for i in range(0,lenght-1):
        delim+="0"

    #print(delim)
    if lenght==1:
        print(number)
        return None
    delim=int(delim)

    max_numb=0
    while True:
        cur_num=number//delim #first number
        if cur_num>max_numb:
            max_numb=cur_num

        number=number%delim
        #print(number)
        delim = delim // 10



        if len(str(number)) == 1:
            number = str(number)
            number = number[-1]
            if max_numb<int(number):
                print(number)
            else:
                print(max_numb)
            break

def first_task_for():
    number=input()
    max_numb=0
    for i in range(0,len(number)):
        if max_numb<int(number[i]):
            max_numb=int(number[i])
    print(max_numb)

#first_task_for()
#first_task_while()

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

def second_task_math():
    n, k = [int(i) for i in input().split()]
    n=n-k
    k=n+k
    n=k-n
    print(n,k)

def seconf_task_array():
    n, k = [int(i) for i in input().split()]
    array=[]
    array.append(n)
    array.append(k)
    n=array[1]
    k=array[0]
    print(n,k)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа
from math import sqrt
def calc():
    a,b,c=0,0,0
    numb=[a,b,c]
    args=["a","b","c"]
    a, b, c = numb
    for i in range(0,3):
        numb[i]=int(input("Введите коэфициент "+args[i]+" "))
    a, b, c = numb
    disc=(-1)*b-4*a*c
    print("Дискременант = "+str(disc))
    if disc==0:
        result=(-1)*b/2*a
        print("Единственный корень х: "+str(result))
    elif disc<0:
       print("Нет решений")
    else:
        result=[]
        result.append(((-1)*b+sqrt(disc))/2*a)
        result.append(((-1)*b-sqrt(disc))/2*a)
        print("Корни уравнения: х1 = "+str(result[0])+" х2 = "+str(result[1]))
