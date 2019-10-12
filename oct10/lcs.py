mat = []

def lcs(word1, word2):
    global mat
    mat = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    for i in range(len(word1)+1):
        for j in range(len(word2)+1):
            if word1[i-1] == word2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                if mat[i-1][j] > mat[i][j-1]:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = mat[i][j-1]
    return mat[len(word1)][len(word2)]

def printLCS(word1, word2):
    global mat
    i = len(word1)
    j = len(word2)
    sub = ''
    while i > 0 and j > 0:
        if word1[i-1] == word2[j-1]:
            sub += word1[i-1]
            i -= 1
            j -= 1
        elif mat[i-1][j] > mat[i][j-1]:
            i -= 1
        else:
            j -= 1
    print("Substring:", sub[::-1])

word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
print("Length of LCS = ", lcs(word1, word2))
printLCS(word1, word2)


"""
OUTPUT

Enter word1: ABCDGH         
Enter word2: AEDFHR
Length of LCS =  3
Substring: ADH
"""