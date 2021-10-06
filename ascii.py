def even_or_odd(s):
    odd_arr = []
    even_arr = []
    for x in s:
        if int(x) % 2 == 0:
            even_arr.append(int(x))

