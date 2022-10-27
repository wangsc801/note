import random

'''
# solution without Comprehension

def random_num(len, lower, upper):
    li = []
    for n in range(0, len):
        li.append(random.randint(lower, upper))
    return li
'''

# solution use Comprehension

def random_num(len, lower, upper):
    if len > 0 and lower < upper:
        return [random.randint(lower, upper) for n in range(0, len)]
    else:
        print('The length of the random number list cannot less than 0.\n' +
              'And the second parameter ought to less than the third parameter.')
