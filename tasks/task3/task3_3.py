# 1


def generate_numbers(num=20):
    dict1 = {a: a ** 2 for a in range(1, num + 1)}
    return dict1


print(generate_numbers(num=int(input("Input your number: "))),
      '\nDefault value:\n', generate_numbers())

# 2


def count_characters(count_me_string):
    dict2 = dict.fromkeys(count_me_string, 0)
    for i in count_me_string:
        dict2[i] += 1
    return dict2


print(count_characters(count_me_string=input("Input your string: ")))
