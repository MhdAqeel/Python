seq1 = "GAT"
seq2 = "GCT"

m =len(seq1)
n =len(sqe2)

Score_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]

gap_penalty = -2

for i in range(1,m+1):
    Score_matrix[i][0]=Score_matrix[i-1][0] + gap_penalty
    
for j in range(1,n+1):
    Score_matrix[0][j]=Score_matrix[0][j-1] + gap_penalty