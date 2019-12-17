"""Згенеровані відкритий ключ і звичайний ключ, який потрібно закодувати"""





x=int(input(''))
RSA=gener_RSA(x)
secret_key=RSA[2]
open_key=RSA[1]
key=RSA[0]
"""Звідси продючеру ми відсилаємо open_key і key"""




"""Отрмаємо від продюсера заколований текст і ключ закодований рса"""
RSA_key=2131 #"""Закодований ключ рса """
String="cNc8nkdwboc3KlcU9N9,fo9" #"""Отримане закодоване повідомлення """



"""Розкодуємо наш РСА ключ за функцією"""
def RSA_decoding(result_of_cipher,secret_key):
    return (result_of_cipher**secret_key[0])%secret_key[1]
key=RSA_decoding(RSA_key,String) #Отримаэмо ключ за яким розкодуэмо наше повідомлення




"""Декодуэмо наше повідомлення за функцією"""
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

    alp = 'abcdefghijklmnopqrstuvwxyz.,@/ABCDEFGHIJKLMNOPQRSTUVWXYZ~`!#$%^&*()_+-=:.<>?/1234567890'
    f = lambda arg: alp[alp.index(arg[0]) - alp.index(arg[1]) % 87]
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



triple_decoding(String,key)
"""Отримаэмо розкодоване повідомлення"""