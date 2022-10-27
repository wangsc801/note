"""
============================================
There exists 4 forms of simplified tan(α+β).
The process is as follow.
============================================

           sin(α + β)
tan(α+β)= ------------
           cos(α + β)

          sinα·cosβ + cosα·sinβ
        = ---------------------
          cosα·cosβ - sinα·sinβ

>> extract sinα·cosβ from the formula above will get

1 + cotα·tanβ
-------------         (formula_1)
cotα - tanβ

>> extract cosα·sinβ

1 + tanα·cotβ
-------------         (formula_2)
cotβ - tanα

>> extract cosα·cosβ

tanα + tanβ
-------------         (formula_3)
1 - tanα·tanβ

>> extract cosα·cosβ

cotα + cotβ
-------------         (formula_4)
cotα·cotβ - 1


for verifying the four formulas that I calculated are of equivalence value,
in other word, verifying that if I am wrong,
I wrote this script for confirmation.
"""

from cmath import tan
from cmath import pi


def formula_1(a, b):
    cota = 1/tan(a)
    cotb = 1/tan(b)
    return (cota+cotb)/(cota*cotb-1)


def formula_2(a, b):
    tana = tan(a)
    cotb = 1/tan(b)
    return (cotb*tana+1)/(cotb-tana)


def formula_3(a, b):
    tana = tan(a)
    tanb = tan(b)
    return (tana+tanb)/(1-tana*tanb)


def formula_4(a, b):
    cota = 1/tan(a)
    tanb = tan(b)
    return (cota*tanb+1)/(cota-tanb)


def summary(a, b):
    print(formula_1(a, b))
    print(formula_2(a, b))
    print(formula_3(a, b))
    print(formula_4(a, b))


def simple_certification():
    # tan(120°) = tan(2/3π) = tan(1/2π + 1/6π) = -√3
    tan120 = tan(2*pi/3)
    # print the value of tan(120°)
    print('tan(2*pi/3) i.e tan(120°) = '+str(tan120), end='\n\n')
    # print the value of -√3
    print('-√3 = -%f' % (3**0.5), end='\n\n')
    # print the four formulas
    print('--- result of the four formulas ---')
    summary(pi/2, pi/6)


def general_certification(a_plus_b, a, b):
    print("tan({:.7f}) = {}\n".format(a_plus_b, tan(a_plus_b)))
    print("{:.7f} + {:.7f} = {:.7f}\n".format(a,b,a+b))
    print('--- four formulas with args {:.7f} and {:.7f} ---'.format(a,b))
    summary(a, b)


general_certification(2*pi/3, pi/2, pi/6)
