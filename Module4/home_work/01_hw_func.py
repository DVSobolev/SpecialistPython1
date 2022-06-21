# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(number):
    digit_1 = number // 100000
    digit_2 = (number // 10000) % 10
    digit_3 = (number // 1000) % 10
    digit_4 = (number // 100) % 10
    digit_5 = (number // 10) % 10
    digit_6 = number % 10
    summa_1 = digit_1 + digit_2 + digit_3
    summa_2 = digit_4 + digit_5 + digit_6
    if summa_1 == summa_2:
        return True
    else:
        return False

if lucky_ticket():
    print("Билет счастливый")
else:
    print("Билет несчастливый")


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
