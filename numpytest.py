'''
Created on 2016/12/23

@author: nogami_kenji
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.arange(0, 8, 0.1)
    y = np.sin(x)
    
    plt.plot(x, y)
    plt.show()
