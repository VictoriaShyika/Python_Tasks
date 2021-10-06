def even_or_odd(s):
    odd_arr = []
    even_arr = []
    for x in s:
        if int(x) % 2 == 0:
            even_arr.append(int(x))
        else:
            odd_arr.append(int(x))
    odd_sum = sum(odd_arr)
    even_sum = sum(even_arr)
    if odd_sum > even_sum:
        return 'Odd is greater than Even'
    elif even_sum == odd_sum:
        return 'Even and Odd are the same'
    else:
        return 'Even is greater than Odd'

if __name__ == '__main__':
    print(compress("The bumble bee"))
