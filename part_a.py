import numpy as np

p = np.array([[20, 20, 1], [20, 140, 1], [60, 60, 1]])
b = np.array([[230, 130, 1], [350, 190, 1], [290, 110, 1]])
x = np.transpose(np.linalg.solve(p, b))
print (x)


