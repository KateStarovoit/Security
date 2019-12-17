def encode_vijn(text, n):
    coding_word="drebotiy"
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
    f = lambda arg: alp[(alp.index(arg[0])+alp.index(arg[1])%87)%87]
    return ''.join(map(f, zip(text, keytext)))


def decode_vijn(coded_text, n):
    keytext = ""
    coding_word="drebotiy"
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
    f = lambda arg: alp[alp.index(arg[0])-alp.index(arg[1])%87]
    return ''.join(map(f, zip(coded_text, keytext)))


print(encode_vijn("0..58.762.15035.0209216", 12))

print(decode_vijn(encode_vijn("0.37293919365059525",100), 100))




