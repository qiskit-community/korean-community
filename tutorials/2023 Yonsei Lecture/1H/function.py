def test_dj1(input):
    # dis orcle is a balanced one
    length = len(input)
    input_i = int(input, base=2)
    if input_i % 2 == 0:
        return 1
    else:
        return 0   

def test_dj2(input):
    length = len(input)
    input_i = int(input, base=2)
    if input_i < 16:
        return 1
    else:
        return 0 

def test_dj3(input):
    return 1

def prepare_5_bit():
    n = 5
    a = []
    for i in range(2 ** n):
        s = str(bin(i))
        s = s[2:]
        s = s.zfill(n)
        a.append(s)
    return a

