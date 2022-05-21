#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = int(input('Digite um número e encontre todos os números primos menores que ele: '))
for p in range(2, n+1):
    if p >= 2:
        for div in range(2, p):
            if(p % div==0):
                break
        else:
            print(p)
                


# In[ ]:





# In[ ]:





# In[ ]:




