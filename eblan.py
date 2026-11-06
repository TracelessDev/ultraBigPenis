# name = "rodion"
# def hello(name):
#     print("Hello!", name) #эт параметр

# hello(name)
# hello("rodion")


# def show_sum(a,b)
#     return a+b

# print(show_sum(5,10)) #вернет а+б

# summ = show_sum(5,10) #результат работы функции можно присвоить в переменную. При этом должен быть объявлен return
# print(summ)


# def func1(a, b):
#     return a / b 
# print(func1(2, 4))

# def func2(a, b):
#     return a**b
# print(func1(5, 5))

# def func3(a, b):
#     return a % b 
# print(func1(99, 5))


# def check_num(num):
#     if num > 0:
#         return "положительное число"
#     elif num < 0: 
#         return "отрицательное число"
#     else:
#         return "нуль"
    
# print(check_num(4))
# print(check_num(-9))
# print(check_num(0))

# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)

# grades = [2, 2, 2, 3, 4, 1, 5, 5, 5, 2, 5, 5, 4, 3,3, 4]
# average = calculate_average(grades)
# print("average оценка: ", average)

# def get_even_nums(nums):
#     result = []
#     for num in nums:
#         if num % 2 == 0:
#             result.append(num)
#     return result


# nums = [5, 7, 2, 44, 78, 67, 52]
# print(get_even_nums(nums))




















# #1
# def calc_area(w, h):
#     return w*h
# print(calc_area(50, 20))

# #2
# def check_age(age):
#     if age < 18:
#         return "дост запрещен"
#     else:
#         return "дост разрешен"

# print(check_age(21))


# #3
# def analyze_nums(numbers):
#     listSum = sum(numbers)
#     listMin = min(numbers)
#     listMax = max(numbers)

#     return listSum, listMin, listMax
# numbers = [2, 4, 5, 1, 10, 55, 31, 32, 4]
# print("сумма, минималка, максималка:", analyze_nums(numbers))







def show_balance(balance):
    print("ваш баланс:", balance, "руб")

def deposit(balance, amount):
    if amount > 0:
        balance += amount 
        print("баланс пополнен на", amount, "руб")
    else:
        print("сумма пополнения должна быть больше нуля")
    
    return balance

def withdraw(balance, amount):
    if amount <= 0:
        print("сумма снятия должна быть больше нуля")
    elif amount > balance:
        print("недостаточно средств")
    else:
        balacne -= amount
        print("вы сняли", amount, "руб")
    return balance 

def main():
    balance = 1000
    while True:
        print("|мини банкомат|")
        print("1 - баланс")
        print("2 - пополнить баланс")
        print("3 - снять деньги")
        print("4 - съебаться")
        choice = input("выберите действие: ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            amount == float(input("сумма пополнения: "))
            balance = deposit(balance, amount)
        elif choice == "3":
            amount = float(input("Сумма снятия: "))
            balance = withdraw(balance, amount)
        elif choice == "4":
            print("вы успешно съебались. До свидания")
        else:
            print("неверная команда")

main()