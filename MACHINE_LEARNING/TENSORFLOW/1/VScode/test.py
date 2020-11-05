import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

print(tf.__version__)
sess = tf.Session()

hello = tf.constant("Hello from Anandhu")

print(sess.run(hello))