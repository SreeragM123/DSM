import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

U, S, VT = np.linalg.svd(A)

reconstructed_A = np.dot(U, np.dot(np.diag(S), VT))

print("Original Matrix:")
print(A)

print("\nReconstructed Matrix:")
print(reconstructed_A)
