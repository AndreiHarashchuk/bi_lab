def fizzbuzz(number):
    if not number % 3:
        if not number % 5:
            return 'fizzbuzz'
        else:
            return 'fizz'
    if not number % 5:
        return 'buzz'
    return number


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
