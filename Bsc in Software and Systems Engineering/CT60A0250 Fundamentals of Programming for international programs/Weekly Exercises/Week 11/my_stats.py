def my_mean(L):
    return sum(L) / len(L)

def my_variance(L):
    mean = my_mean(L)
    diff_sum = sum((i-mean) ** 2 for i in L)
    return diff_sum / len(L)

def my_mode(L):
    mode = 0
    appeared = 0
    for n in L:
        appears = 0
        for f in range(0, len(L)):
            if n == L[f]:
                appears += 1
        if appears > appeared:
            mode = n
        elif appears == appeared and n > mode:
            mode = n
    return mode
