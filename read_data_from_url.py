#try to use iris dataset for create model of NN

import tensorflow as tf
import numpy as np
import urllib.request

#read data from url to fetch
link = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data'

fp = urllib.request.urlopen(link)
mybytes = fp.read()
mystr = mybytes.decode("utf8")

fp.close()
print(mystr)
