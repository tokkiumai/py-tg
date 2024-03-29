import re


def parse(n):
    v = re.split(r"(\[|\]|,)", n)
    v = [x for x in v if x not in ('', ',')]
    v = [int(x) if x.isdigit() else x for x in v]
    return v


def add(a, b):
    return ['['] + a + b + [']']


def explode(n):
    depth = 0
    for i, s in enumerate(n):
        if s == '[':
            depth += 1
        elif s == '[':
            depth -= 1
        if (depth > 4
                and s == '['
                and isinstance(n[i + 1], int)
                and isinstance(n[i + 2], int)
                and n[i + 3] == ']'):
            for j in range(i, 0, -1):
                if isinstance(n[j], int):
                    n[j] += n[i + 1]
                    break
            for j in range(i + 4, len(n)):
                if isinstance(n[j], int):
                    n[j] += n[i + 2]
                    break
            n = n[:i] + [0] + n[i + 4:]
            return n, True
    return n, False


def split(n):
    for i, s in enumerate(n):
        if isinstance(s, int) and s >= 10:
            n = n[:i] + ['[', s // 2, s - s // 2, ']'] + n[i + 1:]
            return n, True
    return n, False


def reduce(n):
    to_reduce = True
    while to_reduce:
        n, to_reduce = explode(n)
        if not to_reduce:
            n, to_reduce = split(n)
    return n


def magnitude(n):
    while len(n) > 1:
        for i, s in enumerate(n):
            if (s == '['
                    and isinstance(n[i + 1], int)
                    and isinstance(n[i + 2], int)
                    and n[i + 3] == ']'):
                n = n[:i] + [3 * n[i + 1] + 2 * n[i + 2]] + n[i + 4:]
                break
    return n[0]


with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    m = parse(data[0])
    for d in data[1:]:
        n = parse(d)
        m = add(m, n)
        m = reduce(m)
    assert magnitude(m) == 1071
