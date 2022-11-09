#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# text = input('Введите текст для кодировки: ')
# print('Закодированный текст:')
# count = 1
# list = ''
# for i in range(len(text)-1):
#     if text[i] == text[i+1]:
#          count += 1
#     else:
#         list = list + str(count) + text[i]
#         count = 1
# if count > 1 or (text[len(text)-2] != text[-1]):
#     list = list + str(count) + text[-1]
# print(list)
# print('')
# print('Декодировка:')
# n = ''
# text = ''
# for i in range(len(list)):
#     if not list[i].isalpha():
#         n += list[i]
#     else:
#         text = text + list[i] * int(n)
#         n = ''
# print(text)

#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input('Введите текст: ')
# text = text.split()
# new_text = ''
# for i in text:
#     if 'абв' not in i:
#         new_text += i + ' '
# print(new_text)