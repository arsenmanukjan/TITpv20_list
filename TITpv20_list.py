spisok=[] # pustoi spisok
numbers=[1,2,3,4,5]
abc=['A', 'B', 'C']
slovo="Programmeerine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список ")
    print("2-склеить списки\n3-добавить букву на i позицию ")
    print("4-удалить элемент\n5-удалить элемент указав его порядковый номер ")
    print("4-узнать индекс элемента\n7-перевернуть список ")
    valik=int(input())
    if valik==1:
     a=input("Введи букву")
     slovo_list.append(a)
     print(f"Добавили {a} новый список",slovo_list)
     a="".join(slovo_list)
     print(a.replace("mm","klassnoe")) # Функция позволяет поменять на (букву, неважно) на то место, которое написал в первый аргумент, на второй
    elif valik==2:
     slovo_list.extend(abc)
     print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить ")
        i=int(input("Введи номер позиции, куда хочешь добавить букву "))
        slovo_list.insert(i-1,a)  #0,1,2...
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить")
        n=slovo_list.count(a)
        print(ord(a[0])) # Выдает код первой буквы со строки
        if n>0:
            for i in range(n):
                slovo_list.remove(a)
        else:
            print("Искомой буквы нет")
            print(slovo_list)
    elif valik==5:
        i=int(input("Введи номер позиции элемента для удаления "))
        n=len(slovo_list) #n=10,i=9
        if i<n:
            slovo_list.pop(i)  
            print(slovo_list)
            a="".join(slovo_list) 
            print(a.title())  # Если список изменяется, то первая буква будет заглавная, а остальные маленькие
            print("Слово состоит из букв" if a.isalpha() else "Слово не состоит из букв")   # Проверяет состоит ли слово или введеный текст из букв(правда пишется слева)
            print("Все буквы в нижнем регистре" if a.islower() else "Одна из букв в верхнем регистре")   # Проверяет состоит ли все буквы из нижних регистров
            print("Все буквы в верхнем регистре" if a.isupper() else "Одна из букв в нижнем регистре")   # Проверяет состоит ли все буквы из верхних регистров
            print("Строка не состоит из неотображаемых символов" if a.isspace() else "Строка состоит из неотрображаемых символов")   #Проверяет состоит ли все буквы неот.симв
            print("Слово начинается с большой буквы" if a.istitle() else "Слово не начинается с большой буквы") # Проверяет не является ли заголовком строка
        else:
            print("Букв меньше, чем указаная позиция")
    elif valik==6:
        a=input("Введи букву, позицию которой хочешь узнать ")
        i=slovo_list.index(a)
        print(f"Элемент {a} стоит на {i+1}-ом месте")
        slovo_list.sort()  # Сортирует с большой буквы, а потом маленькие буквы
        print(slovo_list)  # Сортирует с большой буквы, а потом маленькие буквы
    elif valik==7:
        slovo_list.reverse()
        print(slovo_list)
        print(" / ".join(slovo_list)) # Добавляет между буквами (неважно что), что ты вставил между кавычками
        a="".join(slovo_list)
        print(a.split("mm"))  # Слово делится на две части, и убераются те значения, которые ты написал в аргумент.

  