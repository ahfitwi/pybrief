#------------------------------------------------------------------------------
#  Module, Compiled by: Alem H Fitwi, 
#------------------------------------------------------------------------------
# Computer code has a tendency to grow. We can say that code that doesn’t grow 
#  is probably completely unusable or abandoned.
# Growing code is in fact a growing problem. A larger code always means 
#   tougher maintenance. 
# How do you divide a piece of software into separate but cooperating parts? 
# This is the question. Modules are the answer.
# Namespace: A space inwhich some unique names exist
# Aliasing
#    import pandas as pd
#    import numpy as np
#    multiprocessing as mp 
# dir(module)
# help(module), help(class), help(fuc)
# Module: a collection of functions
# Types of Modules:
    # User-defined
    # Built-in 
    # Third-party

print("------------------------------------------------------")
from random import random, seed
seed(3)
for i in range(10):
    print(random())
print("------------------------------------------------------")
seed(3)
for i in range(10):
    print(random())
print("------------------------------------------------------")
from random import *
#randrange(end)
#randrange(beg,end)
#randrange(beg, end, step)
#randint(left, right)
#choice(sequence)
#sample(sequence, elements_to_chose=1)
#------------------------------------------------------------------------------
# Package: collection of modules
#------------------------------------------------------------------------------
# package plays a similar role to a folder/directory in the world of files.
# package <-- modules <-- functions
# Summary
#       - Packages can contain modules
#       - Modules cannot contain other modules
#       - The __init__.py files are required to make Python treat directories 
#          containing the file as packages. This prevents directories with 
#          a common name, such as string , unintentionally hiding valid modules 
#          that occur later on the module search path.
from sys import path
path.append('/home/alem/Desktop/packages/')
path.append('./packages/extrapack.zip')
# package ---< extra ---> good --> (best(_pycache__, sigma.py, tau.py), _pycache__, alpha.py, beta.py)
#                    ---> __pycache__
#         -          --> ugly (omega.py, psi.py)
#                    ---> __init__.py
#                    ---> iota.py
#------------------------------------------------------------------------------
#                                    ~End~
#------------------------------------------------------------------------------
