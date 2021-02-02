##----------------------------------------------------
##      FILE: 	func.py
##    AUTHOR:  Corey Bryant 
##   CREATED:  Mon Feb 01, 2021  01:22PM.
##  MODIFIED:    Tue Feb 02, 2021    03:32PM.
##
##  
## 
## $Id:$
##----------------------------------------------------


import tabpy.tabpy_tools.client as tabpy
import numpy as np

client = tabpy.Client('http://localhost:9004/')

def normalize(x):
    return list( (x-np.mean(x))/np.std(x) )

client.deploy('normalize',normalize,'Return normalized array',override=True)
