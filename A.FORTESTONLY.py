while (character:=input()):
    if len(character)==1:
        print(f'{((ord(character))):04X}')
    else:
        print(f'{((int(character,16) ^ 0x30)):01X}')

'''
a = -5
a >>= 1
print(a)

from bisect import bisect_left  # Binary search
import sys

# Pre-calculate solutions
res = [0, 1, 3]
i = 3
while res[-1] <= 2e9:
    res.append(res[i - 1] + bisect_left(res, i))
    i += 1


def solve(n):
    return bisect_left(res, n)


def main(file):
    res = []
    for line in file:
        n = int(line)
        if n:
            res.append('{}\n'.format(solve(n)))
        else:
            return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
'''