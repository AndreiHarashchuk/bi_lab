"""
Write a program that prints the numbers from 1 to 100,
but for multiples of three print “Fizz” instead of the number
and for multiples of five print “Buzz”. For numbers which
are multiples of both three and five, print “FizzBuzz”.
"""
print("\n".join(
    [("Fizz" * (not i % 3) + "Buzz" * (not i % 5) + str(i) *
      (i % 3 != 0 and i % 5 != 0)) for i in range(1, 101)]))
