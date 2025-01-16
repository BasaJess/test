import numpy as np
import torch
import tensorflow as tf
print("--------------------------------------------")
x=np.array([[25,2],[5,26],[3,7]])
print("x: ", x)
print("x.__len__() : ", x.__len__())
print("x.shape : ", x.shape)
print("type(x) : ", type(x))
print("x.size : ", x.size)
print("X[:,1]:", x[:,1])
print("x[1,:]:", x[1,:])
print("x[0:2]:", x[0:2, 0:2])
print(type(x[0]))
x_t = x.T
print(x_t)
print(x_t.shape)
type(x)
y=np.array([[3,4,5]])
print("y= ",    y)
print("y.shape: ",y.shape)
y_t=y.T
print("y.T  ",y_t)
print("y_t.shape: ",y_t.shape)
print("L2 Norm of x: np.linalg.norm(y) : ",np.linalg.norm(x))
#py_sum = x + y
#py_sum
#type(py_sum)
x_float = 25.0
float_sum = x_float + y
float_sum
type(float_sum)
print("--------------------------------------------")
x_pt = torch.tensor([[25,2],[5,26],[3,7]])
print(x_pt)
print(x_pt.shape)
print(x_pt[1,:])
print("--------------------------------------------")
x_tf = tf.Variable([[25, 2],[5,26],[3,7]])
print("x_tf: ",x_tf)
print("x_tf.shape: ",x_tf.shape)
print("tf.rank(x_tf): ",tf.rank(x_tf))
print("x_tf[1,:]: ",x_tf[1,:])
y_tf = tf.Variable(3, dtype=tf.int32)
print(x_tf + y_tf)
tf_sum = tf.add(x_tf, y_tf)
print(tf_sum)
print(tf_sum.numpy())
print(type(tf_sum.numpy()))
tf_float = tf.Variable(25.0, dtype=tf.float32)
print(tf_float)