seq1 = "GAT"
seq2 = "GCT"

m =len(seq1)
n =len(seq2)

Score_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]

gap_penalty = -2
match_score = 1
mismatch_penalty = -1

for i in range(1,m+1):
    Score_matrix[i][0]=Score_matrix[i-1][0] + gap_penalty
    
for j in range(1,n+1):
    Score_matrix[0][j]=Score_matrix[0][j-1] + gap_penalty
    
for i in range(1,m+1):
    for j in range(1,n+1):
        if(seq1[i-1]==seq2[j-1]):
            diagonal_score = Score_matrix[i-1][j-1]+match_score
        else:
            diagonal_score = Score_matrix[i-1][j-1]+mismatch_penalty
        
        up_score = Score_matrix[i-1][j] + gap_penalty
        left_score = Score_matrix[i][j-1] + gap_penalty
        
        Score_matrix[i][j] = max(diagonal_score,up_score,left_score)

aligned_seq1 = ""
aligned_seq2 = ""

i = m
j = n

while()

for i in Score_matrix:
    print(i)
    
    
#     Scoring matrix:
#      _   G   C   T   
# _    0  -2  -4  -6
# G   -2   1  -1  -3
# A   -4  -1   0  -2
# T   -6  -3  -2   1