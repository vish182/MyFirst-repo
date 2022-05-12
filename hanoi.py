import time
# array to store already calculated values to avoid repeated calculation
dp = [0] * 101
def hanoiWithMoves(m, source, aux, dest):
    if m == 1:
        print("Moving disk ", m, " from ", source, " to rod ", dest)
        return 1
    else:
        temp1 = hanoiWithMoves(m-1, source, dest, aux)
        print("Moving disk ", m, " from ", source, " to rod ", dest)
        temp2 = hanoiWithMoves(m-1, aux, source, dest)
        dp[m] = temp1 + temp2 + 1
        return dp[m]

def hanoiWithoutMoves(m):
    if m == 1:
        return 1
    if dp[m] > 0:
        return dp[m]
    else:
        temp1 = 2 * hanoiWithoutMoves(m-1)
        dp[m] = temp1 + 1
        return dp[m]



while True:
    n = int(input("Enter the number of disks: "))

    print("    1. Solve with moves shown")
    print("    2. Solve without showing moves")

    op = int(input("\n Select Option: "))

    if op == 1:
        start = time.time()
        print("Answer: ", hanoiWithMoves(n, 1, 2, 3))
    elif op == 2:
        start = time.time()
        print("Answer: ", hanoiWithoutMoves(n))
    else:
        break
    end = time.time()
    print("Time Taken: ", (end - start), " seconds")