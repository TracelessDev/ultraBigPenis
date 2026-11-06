#списки и строки. Методы split() и join()

# students = ["петух", "чмо", "гном", "даун", "утырок"]

# print(students[0])
# print(students[-1])
# print(students[len(students)-1])

# data = ["victor", 27, 75, True]
# name = 0
# age = 1
# weight = 2
# check = 3

# print(f"имя: {data[name]} Возраст: {data[age]} Вес: {data[weight]} Тупой: {students[check]}")



# #срезы списков
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(numbers[1:3])
# print(numbers[:3])
# print(numbers[3:])
# print(numbers[::-1])
# #print(numbers[старт:стоп:шаг])

# #методы для списков
# numbers.append(11) #добавление элемента в конец списка
# print(numbers)
# numbers.insert(0, 99) #делает вставку по индексу. 1й арг - индекс, 2арг - то, что нужно вставить 
# print(numbers)
# numbers.remove(1) #удалить по значению
# print(numbers)
# numbers.pop(1) #удалить по индексу
# print(numbers)
# numbers.reverse() #развернуть задом наперед
# print(numbers)
# numbers.sort() #сортировка по возрастанию значений
# print(numbers)
# numbers.clear() #очистить список 
# print(numbers)



# # функции для списков
# print(len(numbers)) #длинна списка. Считает колво элементов
# print(max(numbers)) #показывает макс число
# print(min(numbers)) #показывает мин число
# print(sum(numbers)) #сумма элементов списка

# print(0 in numbers) #проверка наличия значения в списке (числа и строки)
# print(10 in numbers)

#цикл + список

# for num in numbers:
#     print(num)


# summ=0
# for num in numbers:
#     summ+=num
# print(summ)

# # генератор списков

# numbers = []
# for i in range(1, 11):
#     numbers.append(i)

# print(numbers)

# #или 

# numbers = [i for i in range(1,6) if i % 2 == 0] #сокращенка
# print(numbers)




#1
marks = [2, 3, 4, 4, 3, 4, 5, 4, 5, 2, 4, 5]
print("колво оценок:", len(marks))
print("средняя оценка:", sum(marks)/len(marks))
print("макс:", max(marks))
print("мин:", min(marks))

print("\n")

#2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    if num % 2 == 0:
        print(num)

nums.clear() #на всякий

print("\n")

#3
buyList = ["икра", "краб", "лобстер"]
buyList.append("перфоратор")
buyList.append("подшипники")
buyList.pop(0)

print("\n")


for item in buyList:
    print(item)

print("\n")

#4 
nums = [1, 3, 4, 6, 7, 11, 175, 494]
inp = int(input("введите число: "))
if inp in nums:
    print("такое число есть")
else:
    print("такого нет")

print("\n")
