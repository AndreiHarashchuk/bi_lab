def generate_numbers(num=20):
    dict1 = {a: a ** 2 for a in range(1, num + 1)}
    return dict1


def count_characters(count_me_string='Hello, world!'):
    dict2 = dict.fromkeys(count_me_string, 0)
    for i in count_me_string:
        dict2[i] += 1
    return dict2


def fizzbuzz():
    val_list = []
    for i in range(1, 101):
        if i % 15 == 0:
            val_list.append("FizzBuzz")
        elif i % 3 == 0:
            val_list.append("Fizz")
        elif i % 5 == 0:
            val_list.append("Buzz")
        else:
            val_list.append(str(i))
    return val_list


# poly = lambda word='wow': word == word[::-1]
def poly(word='wow'):
    return word == word[::-1]


def happy(n, past=set()):
    m = sum(int(i) ** 2 for i in str(n))
    if m == 1:
        return True
    if m in past:
        return False
    past.add(m)
    return happy(m, past)


def happy_numbers(n=101):
    return [x for x in range(1, n) if happy(x, set())]
