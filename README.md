# Least dependent component analysis and mutual Information estimation based on KNN
The least dependent component analysis and mutual information repository implements the codes by Kraskov et al originally written in C.
The original C code can be found in https://www.ucl.ac.uk/ion/departments/sobell/Research/RLemon/MILCA/MILCA
The code is imported in python using swig. 

# How to compile
The compilation is straight forward just run in the current directory:

```shell
python setup.py build_ext --inplace
python ./setup.py install
```

The installation generates the mi.so (in linux, and mac) in the current directory. Copy this file to site-packages subfolder in python installation directory.

# Example (Mutual information estimation)

```python
import mi

x = np.randn(1000,10)
y = np.randn(1000,3)
k = 7

z = np.concatenate((x,y),axis=1)
mivalue = mi.mixnyn(z,x.shape[1],k)
```
The above code, calculate the mutual information between x, and y using Kraskov method with k=7.

# Example (ICA estimation, demixing matrix estimation)

```python
import mi
import numpy as np

n_components = 5  # the number of ICA components
x = np.randn(1000,12)
k = 7
method = 0        # either cubic (0), or rectangular (1)
nrot   = 128      # Number of angles to minimize over (suggested: 128)
nharm  = 1        # Number of harmonics to approximate MI(angle) dependence; (suggested: 1)
addnoise = 1e-8   # add small noise to data to convert discrete variables into continuous


covX = np.cov(x.T)  # the data has to be whiten before performing ICA
D_,E_ = np.linalg.eig(covX)
index  = np.argsort(-D_)
D_ = np.matrix(np.diag(1.0/np.sqrt(D_[index])))
E_ = np.matrix(E_[:,index])

Whitening_mat = (D_[0:n_components,:][:,0:n_components])*E_[:,0:n_components].T
y=np.matrix(x)*(np.matrix(Whitening_mat).T)

ica_demixing     = mi.mlica(y,k, method, nrot, nharm, addnoise)  # ICA de-mixing matrix

Rall = np.matrix(ica_demixing)*np.matrix(Whitening_mat)  # The final transform (Matrix whitenning and ica demixing)
```