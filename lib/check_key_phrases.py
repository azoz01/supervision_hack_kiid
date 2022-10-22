import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from constants import KEY_PHRASES_DICT

def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
    
    M = [[None]*(n + 1) for i in range(m + 1)]
    
    missing_in_text = [[None]*(n + 1) for i in range(m + 1)]
    missing_in_key = [[None]*(n + 1) for i in range(m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
                M[i][j] = ''
                missing_in_text[i][j] = 0
                missing_in_key[i][j] = 0                
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                M[i][j] = M[i-1][j-1] + Y[j-1]
                missing_in_text[i][j] = missing_in_text[i-1][j-1]
                missing_in_key[i][j] = missing_in_key[i-1][j-1]                
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                M[i][j] =  M[i-1][j] + '_' if L[i-1][j] > L[i][j-1] else M[i][j-1] + '^'
                if L[i-1][j] > L[i][j-1]:
                    missing_in_text[i][j] = missing_in_text[i-1][j] + 1
                    missing_in_key[i][j] = missing_in_key[i-1][j]    
                else:
                    missing_in_text[i][j] = missing_in_text[i][j-1]
                    missing_in_key[i][j] = missing_in_key[i][j-1] + 1 
                
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    print(M[m][n])
    print(f'missing in key: {missing_in_key[m][n]}')
    print(f'missing in text: {missing_in_text[m][n]}')
    return M[m][n]