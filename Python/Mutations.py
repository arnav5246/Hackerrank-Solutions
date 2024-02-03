def mutate_string(s, i, c):
    #num = ''.join(str(n) for n in i)
    cha =  ''.join(c)
    s = s[:i] + c + s[i+1:]
    return s