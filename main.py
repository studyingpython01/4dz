
def simple_separator():
    print('*'*10)
    pass
print(simple_separator() == '**********')  # True


def long_separator(count):
    print('*'*count)
    pass
print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


def separator(simbol, count):
  result = print(simbol*count)
  return result


def hello_world():
    print('**********')
    print('Hello World!')
    print('##########')
    pass


'''
**********
Hello World!
##########
'''
hello_world()



def hello_who(who='World'):
    print('**********')
    print('Hello', who)
    print('##########')
    pass
def pow_many(power, *args):
    result1 = args
    result3 = sum(args)
    result2 = result3**power
    return result2
    pass
print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(k, '-->', v)
    pass
print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    nums = []
    for i in iterable:
        if function (i) == True:
            nums.append(i)
    print(nums)
    return nums

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True




