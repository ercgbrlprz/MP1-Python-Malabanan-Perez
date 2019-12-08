# malabanan, angelo - perez, eric
# 2-ece-a
# ece2112 machine problem 1 (python solution)

import matplotlib.pyplot as plt

def f(n):
    
   if n <= 9:
     return n * n-7
    
   return f(n-10)

X = []
Y = []
    
for a in range (0,100):
   X.append(a)
   Y.append(f(a))
    
plt.stem(X,Y)
    
plt.title('Graph of f(n)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')