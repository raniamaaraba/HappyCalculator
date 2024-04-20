# Activity Python 1: Task 1
# File: ACT_Python_HeaderTemplate_Team150_maarabrn.py 
# Date:    1 12 2024
# By:      Rania Maaraba
# Section: 09
# Team:    150
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.


####################################################################
def Happy(num):
    count=0
    while num != 1 and count<100:
       count=count+1
    num0=0
    for digit in str(num):
            num0 = num0+(int(digit))**2
            num=num0
    return num == 1
#####################################################################
def Perfect(num):
    divisors = 0
    for i in range(1,num):
        if num % i == 0:
            divisors= divisors + i
    return divisors == num
######################################################################
def Narcissistic(num):
    narcis=0
    num_str = str(num)
    num_digits = len(num_str)
    for digit in num_str:
        narcis = narcis+(int(digit))**num_digits
        
    return narcis == num
######################################################################
##############Start your script here################################

import math

n = int(input('enter a whole number n: '))

number = []
numbertype = []

for num in range(1, n + 1):
        if Happy(num):
            number.append(num)
            numbertype.append('happy')
        elif Perfect(num):
            numbertype.append('perfect')
            number.append(num)
        elif Narcissistic(num):
            numbertype.append('narcissitic')
            number.append(num)
        elif Happy(num) and Narcissistic(num):
            number.append(num)
            numbertype.append('happy & narcissistic')
        elif Narcissistic(num) and Perfect(num):
            number.append(num)
            numbertype.append('narcisistic and perfect')
        elif Happy(num) and Perfect(num):
            number.append(num)
            numbertype.append('happy and perfect')
        

for i in range(len(number)):
    f_n = number[i]
    f_t = numbertype[i]
    print(f"{f_n}: is {f_t}")
