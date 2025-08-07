import numpy as mp
import numpy as np

#eskiusul
a = [1, 2, 3, 4]
b = [3, 5, 7, 8]

ab = []
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 8, 3, 4])   #array icerisinde list
b = np.array([3, 5, 2, 8])
a * b

#import numpy as np
a = np.random.randint(10, size=5)
var = a.ndim
var1 = a.shape
var3 = a.size
var4 = a.dtype

(np.random.randint(1, 10, size=9)).reshape(3, 3)

# İNDEX SEÇİMİ
import numpy as np
a = np.random.randint(10, size=10)
var = a[0]
var1= a[0] = 99
var2 = a[0:5]  #sol taraf dahil sağ taraf haric olacak şelikde

print(var)
print(var1)
print(var2)


import numpy as np
y = np.random.randint(10, size=(4, 5)) #3 satır 5 sütün

var = y[0, 0]
var1 = y[2, 0]
var2 = y[1, 3]

print(var)
print(var1)
print(var2)

### fancy index

import numpy as np
v = np.arange(0, 30, 3) #0 dan 30 a kadar 3 er artarak arry oluştur demektir.
var = v[1]
print(var)

#numpy ile denklem çözümü
# 8*x0 + 4x1 = 15
# x0 + 3*x1 = 12
import numpy as np
a = np.array(([8, 1], [4,3]))
b = np.array([15, 12])

var = np.linalg.solve(a, b)
print(var)

#bittii





