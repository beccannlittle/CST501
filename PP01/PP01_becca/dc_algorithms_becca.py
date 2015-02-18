# -*- coding: utf-8 -*-
from numpy import *  # NOQA

STOCK_PRICE_CHANGES = [13, -3, -25, 20, -3, -16,
                       -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


def find_maximum_subarray_brute(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Implement the brute force method from chapter 4
    time complexity = O(n^2)
    """
    maxSum = float(-inf)
    A = asarray(A)
    n = A.size

    if (low == high):
        return (low, high)
    if (high == -1 and n == 1):
        return (0, 0)
    else:
        for i in range(0, n):
            currentSum = 0
            for j in range(i, n):
                currentSum += A[j]
                if (currentSum > maxSum):
                    maxSum = currentSum
                    low = i
                    high = j
        return (low, high)


def find_maximum_crossing_subarray(A, low, mid, high):
    """
    Find the maximum subarray that crosses mid
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    """
    A = asarray(A)

    leftSum = float(-inf)
    maxLeft = 0
    rightSum = float(-inf)
    maxRight = 0

    currentSum = 0
    for i in range(mid, low - 1, -1):
        currentSum += A[i]
        if (currentSum > leftSum):
            leftSum = currentSum
            maxLeft = i
    currentSum = 0
    for j in range(mid + 1, high + 1):
        currentSum += A[j]
        if (currentSum > rightSum):
            rightSum = currentSum
            maxRight = j
    return (maxLeft, maxRight)


def find_maximum_subarray_recursive(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Recursive method from chapter 4
    """

    A = asarray(A)

    if (high == low):
        return (low, high)
    if (high == -1 and A.size == 1):
        return (0, 0)
    else:
        # assume that if no "high" value was specified,
        # we are looking for max subarray of entire array
        if (high == -1):
            high = A.size - 1
        mid = int(floor((high + low) / 2))

        lefts = find_maximum_subarray_recursive(A, low, mid)
        leftSum = find_sum(A, lefts[0], lefts[1])
        rights = find_maximum_subarray_recursive(A, mid + 1, high)
        rightSum = find_sum(A, rights[0], rights[1])
        crosses = find_maximum_crossing_subarray(A, low, mid, high)
        crossSum = find_sum(A, crosses[0], crosses[1])

        if (leftSum >= rightSum and leftSum >= crossSum):
            return lefts
        if (rightSum >= leftSum and rightSum >= crossSum):
            return rights
        else:
            return crosses


def find_sum(A, low, high):
    """
    Return a value representing the sum of terms from A[low:high].
    """
    subarraySum = 0
    for i in range(low, high + 1):
        subarraySum += A[i]
    return subarraySum


def find_maximum_subarray_iterative(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Do problem 4.1-5 from the book.
    """
    A = asarray(A)

    if (high == low):
        return (low, high)
    if (high == -1 and A.size == 1):
        return (0, 0)

    maxSum = float(-inf)
    left = 0
    right = 0
    currentSum = 0
    currentLeft = 0

    for i in range(0, A.size):
        currentSum += A[i]
        if (currentSum > maxSum):
            maxSum = currentSum
            left = currentLeft
            right = i
        if (currentSum <= 0):
            currentSum = 0
            currentLeft = i + 1
    return (left, right)


def square_matrix_multiply(A, B):
    """
    Return the product AB of matrix multiplication.
    """

    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    assert A.size, "A is empty"

    n = int(A.size ** (0.5))
    C = zeros((n, n))
    if (n == 1):
        C[0] = A[0] * B[0]
    else:
        for i in range(0, n):
            for j in range(0, n):
                C[i, j] = 0
                for k in range(0, n):
                        C[i, j] = C[i, j] + A[i, k] * B[k, j]
    return C


def square_matrix_multiply_strassens(A, B):
    """
    Return the product AB of matrix multiplication.
    Assume len(A) is a power of 2
    """
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    assert (len(A) & (len(A) - 1)) == 0, "A is not a power of 2"

    n = int(A.size ** (0.5))
    C = zeros((n, n))
    if (n == 1):
        C[0] = A[0] * B[0]
    else:
        A11 = zeros((n / 2, n / 2))
        A12 = zeros((n / 2, n / 2))
        A21 = zeros((n / 2, n / 2))
        A22 = zeros((n / 2, n / 2))
        B11 = zeros((n / 2, n / 2))
        B12 = zeros((n / 2, n / 2))
        B21 = zeros((n / 2, n / 2))
        B22 = zeros((n / 2, n / 2))
        S1 = zeros((n / 2, n / 2))
        S2 = zeros((n / 2, n / 2))
        S3 = zeros((n / 2, n / 2))
        S4 = zeros((n / 2, n / 2))
        S5 = zeros((n / 2, n / 2))
        S6 = zeros((n / 2, n / 2))
        S7 = zeros((n / 2, n / 2))
        S8 = zeros((n / 2, n / 2))
        S9 = zeros((n / 2, n / 2))
        S10 = zeros((n / 2, n / 2))
        P1 = zeros((n / 2, n / 2))
        P2 = zeros((n / 2, n / 2))
        P3 = zeros((n / 2, n / 2))
        P4 = zeros((n / 2, n / 2))
        P5 = zeros((n / 2, n / 2))
        P6 = zeros((n / 2, n / 2))
        P7 = zeros((n / 2, n / 2))
        C11 = zeros((n / 2, n / 2))
        C12 = zeros((n / 2, n / 2))
        C21 = zeros((n / 2, n / 2))
        C22 = zeros((n / 2, n / 2))

        for i in range(0, n / 2):
            for j in range(0, n / 2):
                A11[i, j] = A[i, j]
                A12[i, j] = A[i, j + n / 2]
                A21[i, j] = A[i + n / 2, j]
                A22[i, j] = A[i + n / 2, j + n / 2]
                B11[i, j] = B[i, j]
                B12[i, j] = B[i, j + n / 2]
                B21[i, j] = B[i + n / 2, j]
                B22[i, j] = B[i + n / 2, j + n / 2]

        for i in range(0, n / 2):
            for j in range(0, n / 2):
                S1[i, j] = B12[i, j] - B22[i, j]
                S2[i, j] = A11[i, j] + A12[i, j]
                S3[i, j] = A21[i, j] + A22[i, j]
                S4[i, j] = B21[i, j] - B11[i, j]
                S5[i, j] = A11[i, j] + A22[i, j]
                S6[i, j] = B11[i, j] + B22[i, j]
                S7[i, j] = A12[i, j] - A22[i, j]
                S8[i, j] = B21[i, j] + B22[i, j]
                S9[i, j] = A11[i, j] - A21[i, j]
                S10[i, j] = B11[i, j] + B12[i, j]

        P1 = square_matrix_multiply_strassens(A11, S1)
        P2 = square_matrix_multiply_strassens(S2, B22)
        P3 = square_matrix_multiply_strassens(S3, B11)
        P4 = square_matrix_multiply_strassens(A22, S4)
        P5 = square_matrix_multiply_strassens(S5, S6)
        P6 = square_matrix_multiply_strassens(S7, S8)
        P7 = square_matrix_multiply_strassens(S9, S10)

        for i in range(0, n / 2):
            for j in range(0, n / 2):
                C11[i, j] = P5[i, j] + P4[i, j] - P2[i, j] + P6[i, j]
                C12[i, j] = P1[i, j] + P2[i, j]
                C21[i, j] = P3[i, j] + P4[i, j]
                C22[i, j] = P5[i, j] + P1[i, j] - P3[i, j] - P7[i, j]

        for i in range(0, n / 2):
            for j in range(0, n / 2):
                C[i, j] = C11[i, j]
                C[i, j + n / 2] = C12[i, j]
                C[i + n / 2, j] = C21[i, j]
                C[i + n / 2, j + n / 2] = C22[i, j]

    return C


def test():
    print " "
    print "Testing: for each function, it either PASSED or FAILED."
    print "We will use data from the book as well as randomly"
    print "generated data from a common seed. We will not test"
    print "unacceptable input formats (e.g., empty arrays) as those"
    print "situations are covered by assertion fails within functions."
    print " "
    print "First, we will test our maximum subarray functions."
    print " "

    random.seed(2)

    print "For the book data:"
    if (find_maximum_subarray_brute(STOCK_PRICE_CHANGES) == (7, 10)):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    if (find_maximum_subarray_recursive(STOCK_PRICE_CHANGES) == (7, 10)):
        print "    Recursive method: PASSED"
    else:
        print "    Recursive method: FAILED"
    if (find_maximum_subarray_iterative(STOCK_PRICE_CHANGES) == (7, 10)):
        print "    Iterative method: PASSED"
    else:
        print "    Iterative method: FAILED"

    print "For a single element:"
    if (find_maximum_subarray_brute(random.randint(-10, 10, 1)) == (0, 0)):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    if (find_maximum_subarray_recursive(random.randint(-10, 10, 1)) == (0, 0)):
        print "    Recursive method: PASSED"
    else:
        print "    Recursive method: FAILED"
    if (find_maximum_subarray_iterative(random.randint(-10, 10, 1)) == (0, 0)):
        print "    Iterative method: PASSED"
    else:
        print "    Iterative method: FAILED"

    print "For all negative elements:"
    brute = find_maximum_subarray_brute(random.randint(-10, -1, 5))
    rec = find_maximum_subarray_recursive(random.randint(-10, -1, 5))
    it = find_maximum_subarray_iterative(random.randint(-10, -1, 5))
    if (brute[1] - brute[0] == 0):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    if (rec[1] - rec[0] == 0):
        print "    Recursive method: PASSED"
    else:
        print "    Recursive method: FAILED"
    if (it[1] - it[0] == 0):
        print "    Iterative method: PASSED"
    else:
        print "    Iterative method: FAILED"

    print "For all positive elements:"
    if (find_maximum_subarray_brute(random.randint(0, 10, 5)) == (0, 4)):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    if (find_maximum_subarray_recursive(random.randint(0, 10, 5)) == (0, 4)):
        print "    Recursive method: PASSED"
    else:
        print "    Recursive method: FAILED"
    if (find_maximum_subarray_iterative(random.randint(0, 10, 5)) == (0, 4)):
        print "    Iterative method: PASSED"
    else:
        print "    Iterative method: FAILED"

    print "For all the same element:"
    if (find_maximum_subarray_brute((1, 1, 1, 1, 1)) == (0, 4)):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    if (find_maximum_subarray_recursive((1, 1, 1, 1, 1)) == (0, 4)):
        print "    Recursive method: PASSED"
    else:
        print "    Recursive method: FAILED"
    if (find_maximum_subarray_iterative((1, 1, 1, 1, 1)) == (0, 4)):
        print "    Iterative method: PASSED"
    else:
        print "    Iterative method: FAILED"

    print "For all zeros:"
    if (find_maximum_subarray_brute((0, 0, 0, 0, 0)) == (0, 0)):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    if (find_maximum_subarray_recursive((0, 0, 0, 0, 0)) == (0, 0)):
        print "    Recursive method: PASSED"
    else:
        print "    Recursive method: FAILED"
    if (find_maximum_subarray_iterative((0, 0, 0, 0, 0)) == (0, 0)):
        print "    Iterative method: PASSED"
    else:
        print "    Iterative method: FAILED"

    print "For large inputs in small range:"
    print "(checking if rec. and it. methods = brute method)"
    test1 = random.randint(-10, 10, 300)
    if (find_maximum_subarray_recursive(test1)
            == find_maximum_subarray_brute(test1)):
        print "    Recursive method: PASSED"
    else:
        print "    Recursive method: FAILED"
    if (find_maximum_subarray_iterative(test1)
            == find_maximum_subarray_brute(test1)):
        print "    Iterative method: PASSED"
    else:
        print "    Iterative method: FAILED"

    print "For large inputs in large range:"
    print "(checking if rec. and it. methods = brute method)"
    test2 = random.randint(-100, 100, 300)
    if (find_maximum_subarray_recursive(test2)
            == find_maximum_subarray_brute(test2)):
        print "    Recursive method: PASSED"
    else:
        print "    Recursive method: FAILED"
    if (find_maximum_subarray_iterative(test2)
            == find_maximum_subarray_brute(test2)):
        print "    Iterative method: PASSED"
    else:
        print "    Iterative method: FAILED"

    print " "
    print "Next, we will test our square matrix multiply methods."
    print " "

    print "For a single element:"
    testm1a = asarray([3])
    testm1b = asarray([-3])
    expectedm1 = asarray([-9])
    answerm1a = square_matrix_multiply(testm1a, testm1b)
    answerm1b = square_matrix_multiply_strassens(testm1a, testm1b)
    if (answerm1a == expectedm1):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    if (answerm1b == expectedm1):
        print "    Strassen's method: PASSED"
    else:
        print "    Strassen's method: FAILED"

    print "For all negative elements:"
    testm2a = asarray(([-3, -9], [-1, -2]))
    testm2b = asarray(([-5, -6], [-7, -8]))
    expectedm2 = asarray(([78, 90], [19, 22]))
    answerm2a = square_matrix_multiply(testm2a, testm2b)
    answerm2b = square_matrix_multiply_strassens(testm2a, testm2b)
    counter = 0
    for i in range(0, len(testm2a)):
        for j in range(0, len(testm2a[0])):
            if (answerm2a[i, j] == expectedm2[i, j]):
                counter += 1
    if (counter == expectedm2.size):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    counter = 0
    for i in range(0, len(testm2a)):
        for j in range(0, len(testm2a[0])):
            if (answerm2b[i, j] == expectedm2[i, j]):
                counter += 1
    if (counter == expectedm2.size):
        print "    Strassen's method: PASSED"
    else:
        print "    Strassen's method: FAILED"

    print "For all the same element:"
    testm3a = asarray(([3, 3], [3, 3]))
    testm3b = asarray(([3, 3], [3, 3]))
    expectedm3 = asarray(([18, 18], [18, 18]))
    answerm3a = square_matrix_multiply(testm3a, testm3b)
    answerm3b = square_matrix_multiply_strassens(testm3a, testm3b)
    counter = 0
    for i in range(0, len(testm3a)):
        for j in range(0, len(testm3a[0])):
            if (answerm3a[i, j] == expectedm3[i, j]):
                counter += 1
    if (counter == expectedm3.size):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    counter = 0
    for i in range(0, len(testm3a)):
        for j in range(0, len(testm3a[0])):
            if (answerm3b[i, j] == expectedm3[i, j]):
                counter += 1
    if (counter == expectedm3.size):
        print "    Strassen's method: PASSED"
    else:
        print "    Strassen's method: FAILED"

    print "For all zeros:"
    testm4a = asarray(([0, 0], [0, 0]))
    testm4b = asarray(([0, 0], [0, 0]))
    expectedm4 = asarray(([0, 0], [0, 0]))
    answerm4a = square_matrix_multiply(testm4a, testm4b)
    answerm4b = square_matrix_multiply_strassens(testm4a, testm4b)
    counter = 0
    for i in range(0, len(testm4a)):
        for j in range(0, len(testm4a[0])):
            if (answerm4a[i, j] == expectedm4[i, j]):
                counter += 1
    if (counter == expectedm4.size):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    counter = 0
    for i in range(0, len(testm4a)):
        for j in range(0, len(testm4a[0])):
            if (answerm4b[i, j] == expectedm4[i, j]):
                counter += 1
    if (counter == expectedm4.size):
        print "    Strassen's method: PASSED"
    else:
        print "    Strassen's method: FAILED"

    print "For large inputs:"
    testm5a = asarray(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                       [1, 2, 3, 4, 5, 6, 7, 8,
                        9, 10, 11, 12, 13, 14, 15, 16]))
    testm5b = asarray(([16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                       [16, 15, 14, 13, 12, 11, 10, 9,
                        8, 7, 6, 5, 4, 3, 2, 1]))
    expectedm5 = asarray(
        ([2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136],
         [2176, 2040, 1904, 1768, 1632, 1496, 1360, 1224,
          1088, 952, 816, 680, 544, 408, 272, 136]))
    answerm5a = square_matrix_multiply(testm5a, testm5b)
    answerm5b = square_matrix_multiply_strassens(testm5a, testm5b)
    counter = 0
    for i in range(0, len(testm5a)):
        for j in range(0, len(testm5a[0])):
            if (answerm5a[i, j] == expectedm5[i, j]):
                counter += 1
    if (counter == expectedm5.size):
        print "    Brute force method: PASSED"
    else:
        print "    Brute force method: FAILED"
    counter = 0
    for i in range(0, len(testm5a)):
        for j in range(0, len(testm5a[0])):
            if (answerm5b[i, j] == expectedm5[i, j]):
                counter += 1
    if (counter == expectedm5.size):
        print "    Strassen's method: PASSED"
    else:
        print "    Strassen's method: FAILED"

if __name__ == '__main__':
    test()
