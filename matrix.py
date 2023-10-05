import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

result_add = matrix1 + matrix2

result_sub = matrix1 - matrix2

result_mul = matrix1 * matrix2

result_dot = np.dot(matrix1, matrix2)

matrix1_transpose = np.transpose(matrix1)

result_sqrt = np.sqrt(matrix1)

sum_elements = np.sum(matrix1)

result_exp = np.exp(matrix1)

result_log = np.log(matrix1)

result_abs = np.abs(matrix1)

result_sin = np.sin(matrix1)

result_cos = np.cos(matrix1)

mean_value = np.mean(matrix1)

max_value = np.max(matrix1)