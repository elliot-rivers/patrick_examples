import scipy.io
import numpy

scipy.io.savemat('testo.mat', {'aa': numpy.array([[2.0, 2.0], [3.0, 3.0]]), 'field1': 3.0, 'field2': 2.0})
