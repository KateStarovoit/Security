
from random import random
"""Отрмуємо від консюмера відкритий ключ і ключ який треба закодувати"""
open_key=(5, 155189)
key=100



"""Закодовуємо наш key за open_key використовуючи функцію """
def RSA_encoding(open_key,key):
    return key**open_key[0]%open_key[1]
result= RSA_encoding(open_key,key)



"""Закодуэмо наше повідомлення що генерує продюсер функцією"""
def triple_encoding(strng,n):
    lst = []
    count = -1
    for i in strng:
        count += 1
        if i == " ":
            lst.append(count)
    for k in range(n):
        strng = strng.replace(" ", "")
        strng = strng.split()
        strng = strng[0][len(strng) - n - 1:] + strng[0][:len(strng) - n - 1]
        for i in range(len(lst)):
            strng = strng[:lst[i]] + " " + strng[lst[i]:]
        strng = strng.split(" ")
        for i in range(len(strng)):
            for j in range(n):
                strng[i] = strng[i][-1] + strng[i][:-1]
        result = ""
        for i in range(len(strng)):
            if i == len(strng) - 1:
                result += strng[i]
            else:
                result += strng[i] + " "
        strng = result
    x=random()
    # print(strng)
    strng=str(x)[:10]+strng[:]
    # print(strng)
    count = 1
    mem = ""
    lst = []
    returned_str = ""
    for i in range(len(strng)):
        if count == n:
            lst.append((strng[i], count))
            count -= 1
            mem = "-"
        elif count == 1:
            lst.append((strng[i], count))
            count += 1
            mem = "+"
        elif mem == "+":
            lst.append((strng[i], count))
            count += 1
        elif mem == "-":
            lst.append((strng[i], count))
            count -= 1

    def takeSecond(elem):
        return elem[1]

    lst.sort(key=takeSecond)
    for i in lst:
        returned_str += i[0]
    coding_word = "drebotiy"
    keytext = ""

    if len(keytext) >= n:
        keytext = coding_word;
    else:
        while True:
            if len(keytext) < n:
                keytext = keytext + coding_word
                continue
            elif len(keytext) >= n:
                break

    alp = 'abcdefghijklmnopqrstuvwxyz.,@/ABCDEFGHIJKLMNOPQRSTUVWXYZ~`!#$%^&*()_+-=:.<>?/1234567890'
    f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % 87) % 87]
    return ''.join(map(f, zip(returned_str, keytext)))
generated_message="" #Повідомлення що генерую продюсер
returned_encoded_message=triple_encoding(generated_message,key) #Наше закодоване повідомлення


"""Тепер надішлемо консюмеру наше закодоване повідомлення returned_encoded_message і ключ закодований за РСА result= RSA_encoding(open_key,key)"""