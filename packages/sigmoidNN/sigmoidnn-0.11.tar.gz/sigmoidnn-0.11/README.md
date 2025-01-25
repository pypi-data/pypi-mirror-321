# SigmoidNN

## Overview

This Library implements a simple yet powerful **neural network** using scary mathematical operations, such as the sigmoid activation function, cross-entropy loss, and matrix operations😖. The network has been tested with the MNIST dataset of handwritten digits and achieved an **97.99% accuracy** with the chosen parameters.

You can customize the layers, activation functions, and data to train and test the network for your specific needs.

---

## Documentation

### Installation

```bash
pip install sigmoidNN
```

### Basic Usage

#### To use the SigmoidNN library in your project, import the necessary components:

```python
from sigmoidNN import Network, CrossEntropyCost, QuadraticCost
```

CrossEntropyCost, QuadraticCost are the activation function you can import to use

#### Load dataset to train (or test)

```python
from sigmoid import load_data, load_data_wrapper
```

For training and testing, you need dataset in list(zip(input, output)) from, where each input and output is the list and output is vectorized form of output

`load_data(filepath)` method load the data from the file where as `load_data_wrapper(file_path, input_layer, output_layer, [vectorized=True | False])` method convert the load the data from the file and convert it to list(zip(input, output)) form ( note, your data file should be in the format of input and output separated by comma)

recommended to use `load_data_wrapper()` method as it will convert the data to the required format

#### Load mnist dataset to train (or test)

you can also use mnist dataset
mnist dataset has 50,000 28*28 pixel handwritten numbers
    return value
        training data shape=(50000, 784), array([5, 0, 4, ..., 8, 4, 8], shape=(50000,))), (array([[0., 0., 0., ..., 0., 0., 0.],
        validation data shape=(10000, 784), array([3, 8, 6, ..., 5, 6, 8], shape=(10000,))), (array([[0., 0., 0., ..., 0., 0., 0.],
        and test data shape=(10000, 784). array([7, 2, 1, ..., 4, 5, 6], shape=(10000,))))

```python
from sigmoid import load_mnist_data
training_data, validation_data, test_data = load_mnist_data()
```

this method first load data from gzip file then pass it through load_data_wrapper() method to reshape to list(zip(input, output)) for input and output layer respectively so it can be used as a input for training [or testing]

#### Create a new neural network:

```python
# Initialize network
# Add layers (example for MNIST) and activation function (recommended, use CrossEntrpyCost for fast training on larger errors)
net = Network([784, 115, 10], cost=CrossEntropyCost)
```

you can initialize the weight according to your need, `default_weight_init` or `large_weight_init` method can be used to initialize the weight

```python
net.default_weight_init() # this is the default weight initialization if nothing is specified
```

Train the network:

use `monitor_evaluation_accuracy=True` to monitor the accuracy of the model on the evaluation dataset during training

```python
# Train with your data
net.SGD(training_data=training_data, [ epochs=30, mini_batch_size=10, eta=3.0], test_data=test_data, monitor_evaluation_accuracy=True)
```

#### SGD Parameters

| Attribute                     | Description                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------|
| `training_data`               | The dataset used to train the model.                                                           |
| `epochs`                      | The number of times the training process will iterate over the entire training dataset.         |
| `mini_batch_size`             | The number of training examples used in one iteration of the training process.                 |
| `eta`                         | The learning rate, which determines the step size for updating weights during training.        |
| `lmbda`                       | The regularization parameter, used to prevent overfitting by penalizing large weights.         |
| `test_data`                   | The dataset used to evaluate the model's performance after training.                           |
| `monitor_evaluation_accuracy` | A flag to track and report the accuracy of the model on the evaluation dataset during training. |
| `monitor_evaluation_cost`     | A flag to track and report the cost (or loss) of the model on the evaluation dataset.          |
| `monitor_training_accuracy`   | A flag to track and report the accuracy of the model on the training dataset during training.   |
| `monitor_training_cost`       | A flag to track and report the cost (or loss) of the model on the training dataset.            |

#### Make predictions:

```python
# Make predictions
predictions = net.evaluate(test_data)
```

#### Save instance of model(weights, biases, cost function):

```python
# Save the model
net.save("net.json")
```

#### Load instance of model(weights, biases, cost function):

```python
# Load the model
net = Network.load("net.json")
```

---

## Examples

### Example 1: MNIST Dataset

```python
from sigmoidNN import Network, CrossEntropyCost, QuadraticCost
from sigmoid import load_mnist_data

# Load MNIST dataset
training_data, validation_data, test_data = load_mnist_data()

# Initialize network
net = Network([784, 115, 10], cost=CrossEntropyCost)

# Train with MNIST data
net.SGD(training_data=training_data, epochs=30, mini_batch_size=10, eta=3.0, test_data=test_data, monitor_evaluation_accuracy=True)

net.save("net.json")
```

### Example 2: Custom Dataset

```python
from sigmoidNN import Network, CrossEntropyCost, QuadraticCost
from sigmoid import load_data_wrapper

# Load custom dataset
training_data = load_data_wrapper("data.csv")

# Initialize network
net = Network([2, 3, 1], cost=QuadraticCost)

# Train with custom data
net.SGD(training_data=training_data, epochs=30, mini_batch_size=10, eta=3.0)

net.save("net.json")
```

---

check out [GitHub]("https://github.com/Anas-github-Acc/SigmoidNN-package") for contribution and more 