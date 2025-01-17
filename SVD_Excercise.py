
print ("--------------------------------------------------------------")
print ("SVD and eigendecomposition are closely related to each other:")
print("")
print ("     1.- Left-singular vectors of  A  = eigenvectors of  AA_t .")
print ("     2.- Right-singular vectors of  A  = eigenvectors of  A_tA .")
print ("     3.- Non-zero singular values of  A  = square roots of eigenvalues of  AA_t  = square roots of eigenvalues of  A_tA") 
print("")
print("Exercise: Using the matrix P from the preceding PyTorch exercises, demonstrate that these three SVD-eigendecomposition equations are true.")
print("")
print ("     1.- Left-singular vectors of  A  = eigenvectors of  AAt .")
import torch
A = torch.tensor([[25, 2, -5], [3, -2, 1], [5, 7, 4.]])
print("     Matrix P renamed as A: ")
print(A)
print("     A tranposed:")
A_t = torch.t(A)
print(A_t)
print("     AAt:")
print(torch.linalg.matmul(A,A_t))
print("     Eigenvectors of AA_t:")
lambdas_cplx, AA_t_eig = torch.linalg.eig(torch.linalg.matmul(A,A_t))
print(AA_t_eig)
print("     Left Singular Vectors of A:")
U, S, V = torch.linalg.svd(A)
print(U)
print("")
print ("     2.- Right-singular vectors of  A  = eigenvectors of  A_tA .")
print("     Eigenvectors of A_tA:")
lambdas_cply, A_tA_eig = torch.linalg.eig(torch.linalg.matmul(A_t,A))
print(A_tA_eig)
print("     Right Singular Vectors of A:")
print(torch.t(V))
print("")
print ("     3.- Non-zero singular values of  A  = square roots of eigenvalues of  AA_t  = square roots of eigenvalues of  A_tA") 
print ("     Non-zero singular values of  A:")
print(S)
print ("     square roots of eigenvalues of  AA_t")
print(lambdas_cplx ** .5)
print ("     square roots of eigenvalues of  A_tA")
print(lambdas_cply ** .5)