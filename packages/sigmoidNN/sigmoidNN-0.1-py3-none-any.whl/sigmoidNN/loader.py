import pickle
import gzip
import os

import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))

"""Network need data shape of list(zip(input, output)) for input and output layer respectively"""

# load 50,000 dataset from mnist
def load_data(file_path):
    """
    mnist dataset has 50,000 28*28 pixel handwritten dataset
    return value =:
        training data shape=(50000, 784), array([5, 0, 4, ..., 8, 4, 8], shape=(50000,))), (array([[0., 0., 0., ..., 0., 0., 0.],
        validation data shape=(10000, 784), array([3, 8, 6, ..., 5, 6, 8], shape=(10000,))), (array([[0., 0., 0., ..., 0., 0., 0.],
        and test data shape=(10000, 784). array([7, 2, 1, ..., 4, 5, 6], shape=(10000,))))
    so we need to pass this through load_data_wrapper to get the desired shape
    """

    file_path = os.path.join(script_dir, file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError("Dataset file not found.")
    f = gzip.open(file_path, "rb")

    u = pickle._Unpickler(f)
    u.encoding = "latin1"
    training_data, validation_data, test_data = u.load()
    f.close()

    return (training_data, validation_data, test_data)


def load_data_wrapper(file_path, input_layer, output_layer, vectorized=True):
    tr_d, va_d, te_d = load_data(file_path)
    training_inputs = [np.reshape(x, (input_layer, 1)) for x in tr_d[0]]
    if vectorized:
        training_results = [vectorized_result(y, output_layer) for y in tr_d[1]]
    else:
        training_results = tr_d[1]
    training_data = list(zip(training_inputs, training_results))

    validation_inputs = [np.reshape(x, (input_layer, 1)) for x in va_d[0]]
    validation_data = list(zip(validation_inputs, va_d[1]))

    test_inputs = [np.reshape(x, (input_layer, 1)) for x in te_d[0]]
    test_data = list(zip(test_inputs, te_d[1]))

    return (training_data, validation_data, test_data)

def load_mnist_data(vectorized=True):
    return load_data_wrapper("data/mnist.pkl.gz", 784, 10, vectorized)


def vectorized_result(j, output_layer):
    """
    This is used to convert a digit
    (0...9) into a corresponding desired output
    """
    e = np.zeros((output_layer, 1))
    e[j] = 1.0
    return e
