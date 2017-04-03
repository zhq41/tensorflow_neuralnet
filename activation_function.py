#how to use activation function of tensorflow

import tensorflow as tf
import numpy as np

x1 = 1.0
sess = tf.Session()

#sigmoid function
result = tf.nn.sigmoid(x1)
print("Sigmoid result of ",x1," is ",sess.run(result))

#tanh function
result = tf.nn.tanh(x1)
print("tanh result of ",x1," is ",sess.run(result))

#elu function
result = tf.nn.elu(x1)
print("elu result of ",x1," is ",sess.run(result))

#softplus function
result = tf.nn.softplus(x1)
print("Softplus result of ",x1," is ",sess.run(result))

#softsign function
result = tf.nn.softsign(x1)
print("Softsign result of ",x1," is ",sess.run(result))
