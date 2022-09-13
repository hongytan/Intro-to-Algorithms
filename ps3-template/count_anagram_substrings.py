# Compute hash of string
def find_hash(s):
        # Compute frequency table
        frequency_table = [0 for _ in range(26)]
        for j in s:
                frequency_table[ord(j)-97] += 1

        # Compute hash for frequency table
        h = 0
        for j in range(26):
                h += frequency_table[j]*26**j

        return h

# Compute hash table with frequency table as key and count as value
def compute_hash_table(A,k):
        n = len(A) - k + 1
        D = {}

        for i in range(n):
                substring = A[i:i+k]
                h = find_hash(substring)
                
                if h in D:
                        D[h] += 1
                else:
                        D[h] = 1
        return D

# Find anagram substring count of substring B in string A
def find_anagram_substring_count(A,B):
        k = len(B)
        h = find_hash(B)
        H = compute_hash_table(A,k)
        if h in H:
                return H[h]
        else:
                return 0

def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    k = len(S[0])
    H = compute_hash_table(T,k)
    for s_i in S:
        a_i = find_anagram_substring_count(T, s_i)
        A.append(a_i)

    return tuple(A)