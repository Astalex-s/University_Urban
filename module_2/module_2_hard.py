import random

cell_ = random.randint(3, 20)


def ancient_cipher():
    code = []
    num_1 = cell_ // 10
    for i in range(1, cell_):
        for j in range(1, cell_):
            if j != num_1:
                num = (i + j)
                if cell_ % num == 0 and i < j:
                    code.append(i)
                    code.append(j)

    return code


result = ancient_cipher()

print(cell_, '-', *result)
