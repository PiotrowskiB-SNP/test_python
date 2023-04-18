def complicated_script() -> list[int]:
    return [1, 'a', 3, ('Ace', [1, 2, 3]), {'a': 1, "b": 666}]


print('This executes always, and when imported right after import')
if __name__ == '__main__':
    print('This executes only when this file is executed as a script')
    print(complicated_script())


def fun_1() -> int:
    return 1


def fun_2() -> int:
    return 2


def fun_3() -> int:
    return 3


def fun_0() -> int:
    return 0
