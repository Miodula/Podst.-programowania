def list_sum(n):
    if not n:
        return 0
    return n[0] + list_sum(n[1:])

print(list_sum([244,333,222]))