import tensorflow as tf
import numpy as np

hello = tf.constant('Hello, Tensorflow! Lets Create World using Neural Network!!')
sess = tf.Session()
print(sess.run(hello))
