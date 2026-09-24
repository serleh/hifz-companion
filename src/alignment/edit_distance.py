def build_table(expected, recited):
    rows = len(expected) + 1
    cols = len(recited) + 1

    table = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        table[i][0] = i

    for j in range(cols):
        table[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if expected[i - 1] == recited[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                insert = table[i][j - 1] + 1
                delete = table[i - 1][j] + 1
                substitute = table[i - 1][j - 1] + 1

                table[i][j] = min(insert, delete, substitute)

    return table


# BACKTRACKING FUNCTION
def backtrack(expected, recited, table):
    i = len(expected)
    j = len(recited)

    operations = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and expected[i - 1] == recited[j - 1]:
            operations.append(("match", expected[i - 1]))
            i -= 1
            j -= 1

        elif (
            i > 0
            and j > 0
            and table[i][j] == table[i - 1][j - 1] + 1
        ):
            operations.append(
                ("substitute", expected[i - 1], recited[j - 1])
            )
            i -= 1
            j -= 1

        elif i > 0 and table[i][j] == table[i - 1][j] + 1:
            operations.append(("skip", expected[i - 1]))
            i -= 1

        elif j > 0:
            operations.append(("extra", recited[j - 1]))
            j -= 1

    operations.reverse()

    return operations
    i = len(expected)
    j = len(recited)

    operations = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and expected[i - 1] == recited[j - 1]:
            operations.append(("match", expected[i - 1]))
            i -= 1
            j -= 1

        elif i > 0 and table[i][j] == table[i - 1][j] + 1:
            operations.append(("skip", expected[i - 1]))
            i -= 1

        elif j > 0:
            operations.append(("extra", recited[j - 1]))
            j -= 1

    operations.reverse()

    return operations