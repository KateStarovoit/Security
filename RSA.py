import random
from math import *
def gener_RSA(key):
    lst=[]
    for i in range(500):
        x=""
        j=2
        while j<=sqrt(i):
            if i%j==0:
                x="y"
            j+=1
        if x=="":
            lst.append(i)
    # print(lst)
    lst.remove(0)
    lst.remove(1)
    # print(lst)
    p=random.choice(lst)
    q=random.choice(lst)
    n=p*q
    y=(p-1)*(q-1)
    for i in lst:
        if y<i:
            lst.remove(i)
    e=random.choice(lst)
    open_key=(e,n)
    d=1
    for i in range(1,1000000):
        if (i*e)%y==1:
            d=i
            break
    secret_key=(d,n)
    # print(key,"key")
    # print("---------------------------")
    # print(open_key,"open key")
    # print("---------------------------")
    # print(secret_key,"secret key")
    # print("---------------------------")
    return key , open_key,secret_key

def RSA_encoding(open_key,key):
    return key**open_key[0]%open_key[1]

def RSA_decoding(result_of_cipher,secret_key):
    return (result_of_cipher**secret_key[0])%secret_key[1]

print(gener_RSA(100))