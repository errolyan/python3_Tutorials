# -*- coding:utf-8 -*-
# /usr/bin/python
'''
@Author:  Yan Errol  @Email:2681506@gmail.com   
@Date:  2019-06-03  16:17
@File：Bayesian neural newwork
@Describe:贝叶斯神经网络
@Evn:
'''

import edward as ed
from edward.models import Normal

n_samples = x.shape[0]  # number of samples, equal N
n_input = 1  # number of input neurons

for my_num_hidden, my_subplot_num in zip([1, 2, 4, 16], range(1, 5, 1)):

    n_hidden = my_num_hidden  # number of hidden neurons
    print('Fitting curve with {} hidden neurons Bayesian Neural Network'.format(my_num_hidden))

    W_0 = Normal(loc=tf.zeros([n_input, n_hidden]), scale=tf.ones([n_input, n_hidden]))
    W_1 = Normal(loc=tf.zeros([n_hidden, n_input]), scale=tf.ones([n_hidden, n_input]))
    b_0 = Normal(loc=tf.zeros(n_hidden), scale=tf.ones(n_hidden))
    b_1 = Normal(loc=tf.zeros(n_input), scale=tf.ones(n_input))

    x_train = x
    y_train = Normal(loc=tf.matmul(tf.sigmoid(tf.matmul(x_train, W_0) + b_0), W_1) + b_1, scale=0.01)

    qW_0 = Normal(loc=tf.get_variable("qW_0/loc" + str(my_subplot_num - 1), [n_input, n_hidden]),
                  scale=tf.nn.softplus(tf.get_variable("qW_0/scale" + str(my_subplot_num - 1), [n_input, n_hidden])))
    qW_1 = Normal(loc=tf.get_variable("qW_1/loc" + str(my_subplot_num - 1), [n_hidden, n_input]),
                  scale=tf.nn.softplus(tf.get_variable("qW_1/scale" + str(my_subplot_num - 1), [n_hidden, n_input])))
    qb_0 = Normal(loc=tf.get_variable("qb_0/loc" + str(my_subplot_num - 1), [n_hidden]),
                  scale=tf.nn.softplus(tf.get_variable("qb_0/scale" + str(my_subplot_num - 1), [n_hidden])))
    qb_1 = Normal(loc=tf.get_variable("qb_1/loc" + str(my_subplot_num - 1), [n_input]),
                  scale=tf.nn.softplus(tf.get_variable("qb_1/scale" + str(my_subplot_num - 1), [n_input])))

    inference = ed.KLqp({W_0: qW_0, b_0: qb_0, W_1: qW_1, b_1: qb_1}, data={y_train: y})
    inference.run(n_iter=10000, n_samples=20)


    def neural_network(x, W_0, W_1, b_0, b_1):
        h = tf.matmul(tf.sigmoid(tf.matmul(x, W_0) + b_0), W_1) + b_1
        return tf.reshape(h, [-1])


    mus = []
    for s in range(20):
        mus.append(neural_network(x_train, qW_0.sample(), qW_1.sample(), qb_0.sample(), qb_1.sample()))
    mus = tf.stack(mus)

    plt.subplot(int("22" + str(my_subplot_num)))
    plt.scatter(x, y)
    plt.xlabel("x", fontsize=20)
    plt.ylabel("y", fontsize=20, rotation=0)
    for i in range(20):
        plt.plot(x, mus.eval()[i], c='r')
    plt.title('{} hidden neurons'.format(my_num_hidden))
    print('************************************************************')
plt.show()