import statistics
import numpy as np


def ele_mul(multiplier, vector):
    return [a * multiplier for a in vector]


def ele_add(vec_a, vec_b):
    return [a+b for a, b in zip(vec_a, vec_b)]


def vector_sum(vec_a):
    return sum(vec_a)


def vector_average(vec_a):
    return statistics.mean(vec_a)

weights = np.array([0.1, 0.2, 0])

def neural_network(input, weights):
    pred = input.dot(weights)
    return pred


