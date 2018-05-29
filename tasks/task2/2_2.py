"""
Write a program to calculate total cost. One item costs M dollars and N cents.
Customer bought L items. Print total price in dollars and cents for L items.
For example
Input data:  one item price is 3 dollars 20 cents, calculate price for 3 items
Output data: Total cost:  9 dollars 20 cents.
"""

q1 = int(input('Введите цену в долларах: '))

q = int(input('Введите количество центов: '))

q2 = int(input('Введите количества товаров: '))

q1 = q1 * q2 + q * q2 // 100

q = q * q2 % 100

print("Итого: %d долларов и %d центов" % (q1, q))
