def even_nums(n):
    for i in range (0, n+1, 2):
        yield i

n = int(input())
print(list(even_nums(n)))
