'''
Created on 2016/12/23

@author: nogami_kenji
'''

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = a
    c = a[:]

    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    
    a[0] = 100
    
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
