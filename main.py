import sys


def solution(A):
    """Your solution goes here."""
    target = sum(A) // 2
    # print(target)
    partSolutions = [[0] * (target + 1)] * (len(A) + 1)
    # print(partSolutions)
    for numIdx in range(1, len(A) + 1):
        for remainingTarget in range(1, target + 1):
            if A[numIdx - 1] <= remainingTarget:
                partSolutions[numIdx][remainingTarget] = max(partSolutions[numIdx - 1][remainingTarget],
                                                             A[numIdx - 1] + partSolutions[numIdx - 1][remainingTarget - A[numIdx - 1]])
    # print(partSolutions)
    return sum(A) - 2 * partSolutions[-1][-1]


# def select(array, i, target):
#     print(i)
#     print(array)
#     if i >= len(array):
#         return []
#
#     l1 = select(array, i + 1, target - array[i])
#     l1.append(array[i])
#
#     l2 = select(array, i + 1, target)
#
#     t1 = sum(l1)
#     t2 = sum(l2)
#
#     if abs(t1 - target) < abs(t2 - target):
#         return l1
#     else:
#         return l2


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    # input = sys.stdin.readline().split()
    # A = [int(x) for x in input[0].split(",")]
    A = [5, 4, 3, 6, 1,33,7,2,1,44,9,4,12,65,34,98,56,43,12,16,83,966,24,4,89,34,90,54,13,56,74,95]
    # A = [5, 4, 3, 6, 1]
    # sys.stdout.write(str(solution(A)))
    print(solution(A))


if __name__ == "__main__":
    main()
