# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:13:45 2018

@author: Eliud Lelerai
"""

import numpy as np
import pandas as pd
import scipy as ss
from scipy import stats

n = 50 # Number the die is rolled
p = 0.2  # Probability of getting D
(1-p)=q = 0.8  # Probability of failing to get D




X = stats.binom(n, p) # Declare X to be a binomial random variable

#A die marked A to E is rolled 50 times. The probability 
# of getting a “D” exactly 5 times
               
probability=X.pmf(5)          #P(X = 5)

print(probability)

