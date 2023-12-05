'''Write a program which will find all such numbers which are divisible
by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).'''
# list = []
# for num in range(2000,3201):
#     if num%7 == 0 and num %5 != 0:
#         list.append(num)
# print(list)
'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a
single line.'''
# def factorial(n):
#     if n >= 0:
#         if n == 0:
#             return 1
#         else:
#             return n * factorial(n-1)
#     else:
#         print("please enter possitive integer")
# output =factorial(8)
# print(output)
# num = int(input("enter a number :"))
# result = 1
# if num >= 0:
#     if num == 0:
#         result = 1
#     else:
#         for n in range(1, num + 1):
#             result = result * (n)
# else:
#     print("please enter positive integer")
# print(f"factorial of given {num} is {result}")
# num = int(input("enter a number :"))
# print(num)
# result = 1
# if num >= 0:
#     if num == 0:
#         result = 1
#     else:
#         while num > 1:
#             result = result * (num)
#             num = num - 1
# else:
#     print("please enter positive integer")
# print(f"factorial of given number is {result}")

# '''With a given integral number n, write a program to generate a
# dictionary that contains (i, i*i) such that is an integral number
# between 1 and n (both included). and then the program should print the
# dictionary.'''
# num = int(input("enter a number : "))
# d = {}
# for i in range(1,num+1):
#     d[i] = i*i
# print(d)

'''Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every
number.''' #34,67,55,33,12,98
# input_seq = input("enter sequence : ")
# l = input_seq.split(',')
# sample_list = []
# #print(l)
# for i in l:
#     sample_list.append(i)
# print(sample_list)
# sample_tuple = print(tuple(sample_list))
'''Write a program that calculates and prints the value according to the
given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.'''
# import math
# C = 50
# H = 30
# input_sequence = input("Enter a sequence of comma-separated values for D: ")
# d_values = input_sequence.split(',')
# result = []
# for i in d_values:
#     D = int(i)
#     Q = round(math.sqrt((2 * C * D)/H))
#     result.append(str(Q))
# print("results is ",result)
# print(",".join(result))

'''Write a program that accepts a comma separated sequence of words as
input and prints the words in a comma-separated sequence after sorting
them alphabetically.'''
# inputword = input("entr comma separated sequence of words :")
# split_word = inputword.split(',')
# sorted_input = sorted(split_word)
# print(sorted_input)
# # list = []
# # for word in split_word:
# #     list.append(word)
# #     list.sort()
# # print(list)
# print(','.join(sorted_input))
'''9. Write a program that accepts sequence of lines as input and prints the
lines after making all characters in the sentence capitalized.'''
# sample_list = []
# while True:
#     seq_line = input("enter sequence of line and 'done when finshed : \n")
#     if seq_line.lower() == 'done':
#         break
#     sample_list.append(seq_line)
# for word in sample_list:
#     print(word.upper())
# i = 1
# while True:
#     print('hi')
#     i = i + 1
#     if i == 7:
#         break

'''10.Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words and
sorting them alphanumerically.'''
# input_word = input("enter series of white spaces separated words :")
# sample_list =[]
# print(type(input_word))
# for word in input_word.split(' '):
#     sample_list.append(word)
# print(sample_list)
# uniq_list = set(sample_list)
# print(uniq_list)
# final_list = sorted(list(uniq_list))
# print(' '.join(final_list))

'''11'Write a program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible
by 5 or not. The numbers that are divisible by 5 are to be printed in
a comma separated sequence.'''
# inp_sequence = input("a sequence of comma separated 4 digit binarynumbers :")
# sample_list = []
# for num in inp_sequence.split(','):
#     num_dec = int(num,2)
#     if num_dec%5 == 0:
#         sample_list.append((num))
# print((sample_list))
# print(','.join(sample_list))

"""12. Write a program, which will find all such numbers between 1000 and
3000 (both included) such that each digit of the number is an even
number."""
# sample_list = []
# for num in range(1000,1500):
#     if num%2 == 0:
#         sample_list.append(str(num))
# #print(sample_list)
# print(type(sample_list[1]))
# #print(','.join(sample_list))

"""13. Write a program that accepts a sentence and calculate the number of
letters and digits."""
# sample_input = input("enter a sentence : ")
# al_result = 0
# num_result = 0
#
# for word in sample_input:
#     if word.isalpha():
#         al_result = al_result + 1
#     elif word.isalnum():
#         num_result = num_result + 1
#     else:
#         print("enter valid character")
# print(f'Total aplphabets count is {al_result} \n Total digits count is {num_result}')
"""Write a program that accepts a sentence and calculate the number of
upper case letters and lower case letters.
"""
# sentence = input("enter the sequence of letters :")
# upper_sentence = 0
# lower_sentence = 0
# for char in sentence:
#     if char.isupper():
#
#         upper_sentence = upper_sentence + 1
#     elif char.islower():
#         lower_sentence = lower_sentence + 1
#     else:
#         print("enter valid character")
# print(f" uppercase count is {upper_sentence} \n lower case count is {lower_sentence}")

# sentence = input("enter the sequence of letters :")
# upper_sentence = []
# lower_sentence = []
# for char in sentence:
#     if char.isupper():
#         upper_sentence.append(char)
#
#
#     elif char.islower():
#         lower_sentence.append(char)
#     else:
#         print("enter valid character")
# upper_char = ''.join(upper_sentence)
# lower_case  = ''.join(lower_sentence)
# print("uppercase count is", len(upper_sentence))
# print(f"entered upper case letters are {upper_char}")
# print("lowercase count is", len(lower_sentence))
# print(f"entered lower case letters are {lower_case}")

''' 15.Write a program that computes the value of a+aa+aaa+aaaa with a given
digit as the value of a.'''

# not done

''' 16. Use a list comprehension to square each odd number in a list. The list
is input by a sequence of comma-separated numbers.'''
# sample_list = input("enter sequence of numbers : ")
# numbers = [int(i) for i in sample_list.split(',')]
# sq_num = [str(num*num) for num in numbers if num%2 !=0]
# print(','.join(sq_num))



