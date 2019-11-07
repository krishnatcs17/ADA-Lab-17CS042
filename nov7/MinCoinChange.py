def printCoins(A, d, S):
    a = A
    print("\nChanges:")
    while a > 0:
        print(d[S[a]])
        a -= d[S[a]]

def findMinCoinChange(A, d):
    coins = [9999 for _ in range(A+1)]
    S = [-1 for _ in range(A+1)]
    coins[0] = 0
    S[0] = 0
    for i in range(1, A+1):
        for j in range(len(d)):
            if d[j] <= i:
                if coins[i - d[j]] + 1 < coins[i]:
                    coins[i] = 1 + coins[i - d[j]]
                    S[i] = j
    print("Min coins needed: ", coins[-1])
    printCoins(A, d, S)                   


if __name__ == "__main__":

    A = int(input("Change amount: "))
    d = list(map(int, input("Denomination array: ").split()))
    findMinCoinChange(A, d)
