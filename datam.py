#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

def randomization(n):
 
    A = np.random.random(size=n).reshape(n,1)
    
    return A

def operations(h, w):
  
    A = np.random.random(size=(h,w))
    B = np.random.random(size=(h,w))
    s = A + B 
    
    return A, B, s

def norm(A, B):

    s = A + B
    
    return np.linalg.norm(s)


def neural_network(inputs, weights):
    
    z = np.tanh(weights.T.dot(inputs))
    
    return z

def scalar_function(x, y):
    if x<=y:
       return (np.dot(x,y))
    else:
       return(x/y)
    raise NotImplementedError

    

def vector_function(x, y):

    out = np.vectorize(scalar_function)
    return out
    
    raise NotImplementedError


# In[ ]:




