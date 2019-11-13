import numpy as np
S1 = np.array([[0.5, 0.5, 0.5, 0.5]])
S2 = np.array([[1/2, -5/6, 1/6, 1/6]])
S3 = np.array([[1/2, 1/6, 1/6, -5/6]])
F1 = np.array([[0, 1, 0]])
F2 = np.array([[1, 0, 1]])
F3 = np.array([[0, 0, 0]])

W = np.outer(F1, S1.T) + np.outer(F2, S2.T) + np.outer(F3, S3.T)
print('Final weights stored are \n' + str(W))
