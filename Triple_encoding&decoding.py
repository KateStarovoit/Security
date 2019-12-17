# from Vijener import*
from itertools import cycle
from random import random
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

    alp = 'abcdefghijklmnopqrstuvwxyz.,@/ABCDEFGHIJKLMNOPQRSTUVWXYZ~`!#$%^&*() _+-=:.<>?/1234567890'
    f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % 88) % 88]
    return ''.join(map(f, zip(returned_str, keytext)))

def triple_decoding(strng,n):
    keytext = ""
    coding_word = "drebotiy"
    if len(keytext) >= n:
        keytext = coding_word
    else:
        while True:
            if len(keytext) < n:
                keytext = keytext + coding_word
                continue
            elif len(keytext) >= n:
                break

    alp = 'abcdefghijklmnopqrstuvwxyz.,@/ABCDEFGHIJKLMNOPQRSTUVWXYZ~`!#$%^&*() _+-=:.<>?/1234567890'
    f = lambda arg: alp[alp.index(arg[0]) - alp.index(arg[1]) % 88]
    strng=''.join(map(f, zip(strng, keytext)))

    def rail_pattern(n):
        r = list(range(n))
        return cycle(r + r[-2:0:-1])
    p = rail_pattern(n)
    indexes = sorted(range(len(strng)), key=lambda i: next(p))
    result = [''] * len(strng)
    for i, c in zip(indexes, strng):
        result[i] = c
    strng=''.join(result)
    strng = strng[10:]
    count=-1
    lst=[]
    for i in strng:
        count+=1
        if i==" ":
            lst.append(count)
    for k in range(n):
        strng=strng.split(" ")
        for i in strng:
            if i=="":
                strng.remove(i)
        for i in range(len(strng)):
            for j in range(n):
                strng[i] = strng[i][1:]+strng[i][0]
        result=""
        for i in strng:
            result+=i
        strng=result
        strng = strng[n:] + strng[0:n]
        result=""
        for i in range(len(lst)):
            strng = strng[:lst[i]] +" "+strng[lst[i]:]
    return strng



# from itertools import cycle
# from random import random
# def double_encoding(strng,n):
#     lst = []
#     count = -1
#     for i in strng:
#         count += 1
#         if i == ".":
#             lst.append(count)
#     for k in range(n):
#         strng = strng.replace(".", "")
#         strng = strng.split()
#         strng = strng[0][len(strng) - n - 1:] + strng[0][:len(strng) - n - 1]
#         for i in range(len(lst)):
#             strng = strng[:lst[i]] + "." + strng[lst[i]:]
#         strng = strng.split(".")
#         for i in range(len(strng)):
#             for j in range(n):
#                 strng[i] = strng[i][-1] + strng[i][:-1]
#         result = ""
#         for i in range(len(strng)):
#             if i == len(strng) - 1:
#                 result += strng[i]
#             else:
#                 result += strng[i] + "."
#         strng = result
#     x=random()
#     # print(strng)
#     strng=str(x)[:10]+strng[:]
#     # print(strng)
#     count = 1
#     mem = ""
#     lst = []
#     returned_str = ""
#     for i in range(len(strng)):
#         if count == n:
#             lst.append((strng[i], count))
#             count -= 1
#             mem = "-"
#         elif count == 1:
#             lst.append((strng[i], count))
#             count += 1
#             mem = "+"
#         elif mem == "+":
#             lst.append((strng[i], count))
#             count += 1
#         elif mem == "-":
#             lst.append((strng[i], count))
#             count -= 1
#
#     def takeSecond(elem):
#         return elem[1]
#
#     lst.sort(key=takeSecond)
#     for i in lst:
#         returned_str += i[0]
#     return (returned_str)
#
# def double_decoding(strng,n):
#
#     def rail_pattern(n):
#         r = list(range(n))
#         return cycle(r + r[-2:0:-1])
#     p = rail_pattern(n)
#     indexes = sorted(range(len(strng)), key=lambda i: next(p))
#     result = [''] * len(strng)
#     for i, c in zip(indexes, strng):
#         result[i] = c
#     strng=''.join(result)
#     strng = strng[10:]
#     count=-1
#     lst=[]
#     for i in strng:
#         count+=1
#         if i==".":
#             lst.append(count)
#     for k in range(n):
#         strng=strng.split(".")
#         for i in strng:
#             if i=="":
#                 strng.remove(i)
#         for i in range(len(strng)):
#             for j in range(n):
#                 strng[i] = strng[i][1:]+strng[i][0]
#         result=""
#         for i in strng:
#             result+=i
#         strng=result
#         strng = strng[n:] + strng[0:n]
#         result=""
#         for i in range(len(lst)):
#             strng = strng[:lst[i]] +"."+strng[lst[i]:]
#     return strng


print(triple_encoding('Volodymyrshabat@gmail.com',67))


print(triple_decoding(triple_encoding('Volodymyrshabat@gmail.com',67),67))
# print(len(str(random())))
