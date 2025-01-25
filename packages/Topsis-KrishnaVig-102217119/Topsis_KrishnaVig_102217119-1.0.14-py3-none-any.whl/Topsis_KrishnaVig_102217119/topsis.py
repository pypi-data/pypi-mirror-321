import numpy as np
import pandas as pd
import sys

def topsis(input_file,weights,impacts,output_file):
    
    if input_file.lower().endswith('.xlsx'):
        data = pd.read_excel(input_file)
    elif input_file.lower().endswith('.csv'):
        data = pd.read_csv(input_file)
    else:
        print("unsupported file format")
        sys.exit(1)

    decision = data.iloc[:,1:]
    decision = np.array(decision).astype(float)
    weights = np.array(weights).astype(float)
    impacts = [char for char in impacts]
    
    nrow = decision.shape[0]
    ncol = decision.shape[1]
    
  
    assert len(decision.shape) == 2, "Decision matrix must be two dimensional"
    assert len(weights.shape) == 1, "Weights array must be one dimensional"
    assert len(weights) == ncol, "Wrong length of Weights array, should be {}".format(ncol)
    assert len(impacts) == ncol,"Wrong length of Impacts array, should be {}".format(ncol)
    

    weights = weights/sum(weights)
    

    N = np.zeros((nrow,ncol))
    
    nf = [None]*ncol
    for j in range(ncol):
        nf[j] = np.sqrt(sum((decision[:,j])**2))
    
   
    for i in range(nrow):
        for j in range(ncol):
            N[i][j] = decision[i][j]/nf[j]
    
   
    W = np.diag(weights)
    V = np.matmul(N,W)
    
    
    u = [max(V[:,j]) if impacts[j] == '+' else min(V[:,j]) for j in range(ncol)]
    l = [max(V[:,j]) if impacts[j] == '-' else min(V[:,j]) for j in range(ncol) ]
    
     
    du = [None]*nrow
    dl = [None]*nrow
    
    
    for i in range(nrow):
        du[i] = np.sqrt(sum([(v1-u1)**2 for v1,u1 in zip(V[i],u) ]))
    for i in range(nrow):
        dl[i] = np.sqrt(sum([(v1-u1)**2 for v1,u1 in zip(V[i],l) ]))
    
    du = np.array(du).astype(float)
    dl = np.array(dl).astype(float)
    
    
    score = dl/(dl+du)
    
    score = pd.Series(score)
    ranks = score.rank(ascending = False,method = 'min').astype(int)
    data['Topsis Score'] = score
    data['Rank'] = ranks
    
    data.to_csv(output_file,index = False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("incorrect number of parameters")
        sys.exit(1)
    
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    
    topsis(input_file,weights,impacts,output_file)