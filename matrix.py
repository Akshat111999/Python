import numpy as np
import matplotlib.pyplot as plt

m=[[0.0,1.2,3.3,2.5,1.4,2.34,3.2,1.2,2.33],
   [1.23,0.0,1.22,2.23,3.1,1.34,2.45,3.51,1.22],
   [2.34,1.45,0.0,4.2,3.67,1.24,2.66,1.46,1.46],
   [3.21,4.21,1.23,0.0,2.41,1.34,1.2,3.22,2.92],
   [1.21,1.21,2.23,1.26,0.0,2.34,3.2,1.22,3.45],
   [2.11,2.77,1.67,3.4,1.21,0.0,2.22,3.23,1.87],
   [1.56,4.21,1.23,3.56,1.44,2.33,0.0,1.56,3.44],
   [2.29,1.21,3.23,2.34,1.11,1.34,1.2,0.0,1.44],
   [1.76,2.21,2.96,1.44,2.41,3.34,2.2,3.85,0.0],]
matrix=np.matrix(m)

print(matrix)

