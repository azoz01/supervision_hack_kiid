import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from constants import KEY_PHRASES_DICT

def lcs(X, Y, factor=20):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    
    max_error = m // factor
 
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
    M = [[None]*(n + 1) for i in range(m + 1)]
    
    missing_key = [[m]*(n + 1) for i in range(m + 1)]
    missing_text = [[n]*(n + 1) for i in range(m + 1)]
 
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
                M[i][j] = ''
                missing_key[i][j] = m
                missing_text[i][j] = n
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                M[i][j] = M[i-1][j-1] + X[i-1]
                missing_key[i][j] = missing_key[i-1][j-1] - 1
                missing_text[i][j] = missing_text[i-1][j-1] - 1
                
            else:
                # L[i][j] = max(L[i-1][j], L[i][j-1])
                if L[i-1][j] > L[i][j-1]:
                    L[i][j] = L[i-1][j]
                    M[i][j] = M[i-1][j] + '_'
                    missing_key[i][j] = missing_key[i-1][j] 
                    missing_text[i][j] = missing_text[i-1][j] - 1                
                else:
                    L[i][j] = L[i][j-1]
                    M[i][j] = M[i][j-1] + '^'
                    missing_key[i][j] = missing_key[i][j-1] - 1
                    missing_text[i][j] = missing_text[i][j-1] 
                    
            if M[i][j] == X:
                return True
                    
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    root = M[m][n][:m+max_error].rstrip('^').rstrip('_')
    total_err = root.count('^') + root.count('_')
    
    return total_err <= max_error * 2


def check_doc(doc: pd.Series) -> pd.DataFrame:
    phrases = []
    does_exist = []
    for phrase, col in KEY_PHRASES_DICT.items():
        text = ' '.join(doc[col].lower().split())
        phrase_flat = ' '.join(phrase.lower().split())
        res = lcs(phrase_flat, text)
        
        phrases.append(phrase)
        does_exist.append(res)
        
    df = pd.DataFrame(data={'WYRAZENIE' : phrases, 'FLAGA_WYSTAPIENIA': does_exist})
    return df