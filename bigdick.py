#name = "  rodion "
#print(name[0])
#print(name[3])
#print(name[-1])
#print(name[len(name)-1])

#срез
#print(name[0:3]) #эта хуня не включает последний индекс
#print(name[3:]) #ласт три
#print(name[:3]) #первые 3 (индекс 0-2)
#print(name[:])
#шаг строка[старт:стоп:шаг]#
#print(name[::2])
#print(name[::-2])
#инвертирует строку
#print(name[::-1])

#name[0] = "W" не сработает, т. к. строка не изменяема

# print(name.lower(), #ниж. регистр
#       name.upper(), #выс. регистр
#       name.capitalize(), #первая буква выс. регистра
#       name.find("n"), #дает индекс. Может искать кусками 
#       name.count("а"), #дает кол-во символов. Может работать с другими методами.Пр.: name.lower().count("t"). Может так же искать кусками
#       name.replace("m", "a"), #меняет
#       name.strip() #чистит пробелы, что бы без хуни было
#       )


#функции строк

#print(len(name.strip()))

#экранированные последовательности

# print("hello world")
# print("hello\nworld") #перенос строк
# print("hello \tworld") #табуляция
# print("hello \'world") #кавычка
# print("hello world")
# print("hello world")








# #1
# print("\n"*2)
# name = input("имя: ")
# print("прив,", name, 
#       "\nдлина имени:", len(name), "букв",
#       "\nпервая буква:", name[0],
#       "\nпоследняя буква:", name[-1])

# #2
# print("\n"*2)
# sentence = input("предложение: ")
# sentence = sentence.lower().strip().replace(" ", "_")
# countA = sentence.count("а")
# print(sentence, "\nбукв А:", countA, "штук")

# #3
# print("\n"*2)
# word = input("слово: ")
# word = word[::-1]
# print("слово в обратном порядке:", word)

# #4
# print("\n"*2)
# inpStr = input("введи строку: ")
# findStr = input("введи строку для поиска: ")
# replaceStr = input("введи слово для замены: ")
# inpStr = inpStr.replace(findStr, replaceStr)
# print("результат: ", inpStr)




























