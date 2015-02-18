import sys
INFINITY = sys.maxint


def print_neatly(words, M):
    """ Print text neatly.

    Parameters
    ----------
    words: list of str
            Each string in the list is a word from the file.
    M: int
            The max number of characters per line including spaces

    Returns
    -------
    cost: number
            The optimal value as described in the textbook.
    text: str
            The entire text as one string with newline characters.
            It should not end with a blank line.

    Details
    -------
            Look at print_neatly_test for some code to test the solution.
    """
    n = len(words)
    linecost = [[0 for x in range(n)] for x in range(n)]
    options = [[[0 for x in range(1)] for x in range(2)] for x in range(1)]
    for i in range(0, n):
        linecost[i][i] = M - len(words[i])
        for j in range(i + 1, n):
            linecost[i][j] = linecost[i][j - 1] - len(words[j]) - 1
        for j in range(i, n):
            if (linecost[i][j] < 0):
                linecost[i][j] = INFINITY
            else:
                if (j == n - 1):
                    linecost[i][j] = 0
                    options.append([[0], [i]])
                else:
                    linecost[i][j] = linecost[i][j] ** 3
    optimal = -1
    cost = INFINITY
    which = 1
    for i in range(0, len(options) - 1):
        linestart = -1
        while (linestart != 0):
            linestart, addcost = findPreviousLineStart(
                linecost, n, options[which][1][0])
            options[which][1].insert(0, linestart)
            options[which][0][0] += addcost
        which += 1
        if (options[i + 1][0][0] < cost):
            optimal = i
            cost = options[i + 1][0][0]
    text = oneString(words, options[optimal + 1][1], M)
    return (cost, text)


def oneString(words, indices, M):
    text = ""
    lines = len(indices)
    indices.insert(lines, len(words))
    for i in range(0, lines - 1):
        line = ""
        for j in range(indices[i], indices[i + 1] - 1):
            line += words[j] + ' '
        line += words[indices[i + 1] - 1]
        numspaces = M - len(line)
        line += numspaces * ' ' + '\n'
        text += line
    for j in range(indices[lines - 1], indices[lines]):
        text += words[j] + ' '
    return text


def findPreviousLineStart(linecost, n, next):
    minimum = INFINITY
    linestart = -1
    for i in range(0, next - 1):
        if (linecost[i][next - 1] < minimum):
            minimum = linecost[i][next - 1]
            linestart = i
            addcost = linecost[i][next - 1]
    return linestart, addcost
