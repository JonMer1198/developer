# from __future__ import division
# from math import *
# import numpy as np
# v0= 5
# g= 9.81
# yc= 0.2
# t1= (v0 - sqrt(v0**2 - 2*g*yc))/g
# t2= (v0 + sqrt(v0**2 - 2*g*yc))/g
# print 'At t=%g s and %g s, the height is %g m.' % (t1, t2, yc)

# import matplotlib.pyplot as plt
# import numpy as np


# Fs = 8000
# f = 5
# sample = 8000
# x = np.arange(sample)
# y = np.sin(2 * np.pi * f * x / Fs)
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('probability')
# plt.show()


# from math import *
# import numpy as np
# import matplotlib.pyplot as plt

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C, S = np.cos(X), np.sin(X) * np.sin(X)

# plt.plot(X, C)
# plt.plot(X, S)

# plt.show()


from math import *
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
S = np.sin(X) * np.sin(X)

plt.plot(X, S)

plt.show()
