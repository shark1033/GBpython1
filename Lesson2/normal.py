# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
from math import sqrt
def task1():
    list1=[2, -5, 8, 9, -25, 25, 4]
    list2=[]
    print(type(sqrt(2)))
    for i in range(0,len(list1)):
        if list1[i]>0 and type(sqrt(list1[i]))!=float:
            list2.append(sqrt(list1[i]))
        else:
            list2.append(list1[i])
        print(list2[i])


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
def task2():                                                   #ЭТО ПРОСТО УЖАСНО ТАК ДЕЛАТЬ....
    example="20.12.2013."
    day=example[0:2]
    mounth=example[3:5]
    year=example[6:10]
    m={"01":"января","02":"февраля","03":"марта","04":"апреля","05":"мая",
       "06":"июня","07":"июля","08":"августа","09":"сентября","10":"октября","11":"ноября","12":"декабря"}


    d={"01":"первое","02":"второе","03":"третье","04":"четвёртое","05":"пятое",
       "06":"шестое","07":"седьмое","08":"восьмое","09":"девятое","10":"десятое","11":"одиннадцатое","12":"двеннадцатое",
       "13":"тринадцатое","14":"четырнадцатое","15":"пятнадцатое","16":"шестнадцатое","17":"семнадцатое",
       "18":"восемнадцатое","19":"девятнадцатое","20":"двадцатое","21":"двадцать первое","22":"двадцать второе","23":"двадцать третье",
       "24": "двадцать четвёртое", "25": "двадцать пятое", "26": "двадцать шестое", "27": "двадцать седьмое", "28": "двадцать восьмое",
       "29": "двадцать девятое", "30": "тридцатое", "31": "тридцать первое"}

    print('{} {} {} года'.format(d.get(day), m.get(mounth), year))




# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
def task3():
    from random import randint
    n=50
    test=[]
    for i in range(0,n-1):
        test.append(randint(-100,100))
        print(test[i])


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
#todo не доделано
def task4():
    lst = [1, 2, 4, 5, 6, 2, 5, 2]
    delete = []
    for i in range(0, len(lst)):
        for y in range(0, len(lst)):
            if lst[i] == lst[y]:
                delete.append(lst[i])

    print("------------")
    for y in range(0, len(delete)):
        lst.remove(delete[y])
    for i in lst:
        print(i)

task4()