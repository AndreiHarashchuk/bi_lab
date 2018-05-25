"""
Write a program to calculate total cost. One item costs M dollars and N cents.
Customer bought L items. Print total price in dollars and cents for L items.
For example
Input data:  one item price is 3 dollars 20 cents, calculate price for 3 items
Output data: Total cost:  9 dollars 20 cents.
"""
q1 = float(input('Введите цену товара: '))

q2 = int(input('Введите количества товаров: '))

check = q1 * q2

print('Итого ', ' = ', check, '$')
