# import TensorFlow
import tensorflow as tf

# Verify we can print a string
hello = tf.constant("Hello")
tf.print(hello)

# Perform some simple math
a = tf.constant(20)
b = tf.constant(22)
print(a + b)