from all import *  # noqa


def output(arg):
    result = eval(arg + '()')
    print("Demonstrating function", arg, ":\n", result)
    return False


def runner(*args):
    flag = True
    for arg in args:
            flag = output(arg)
    if flag:
        output('generate_numbers')
        output('count_characters')
        output('fizzbuzz')
        output('poly')
        output('happy_numbers')


runner('poly', 'happy_numbers')
