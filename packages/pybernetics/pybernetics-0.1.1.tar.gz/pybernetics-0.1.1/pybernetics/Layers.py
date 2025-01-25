"""
Layers
======
This module provides functionality for handling layers and activation functions 
within a neural network. It includes implementations of fully connected layers 
(Dense layers) and a variety of activation functions.

Classes:
--------
1. Dense:
    Represents a fully connected layer in a neural network. 
    Allows forward and backward propagation with support for different weight initialization methods.

2. Sigmoid:
    Implements the Sigmoid activation function with support for gradient computation.

3. ReLU:
    Implements the Rectified Linear Unit (ReLU) activation function.

4. Tanh:
    Implements the hyperbolic tangent (Tanh) activation function.

5. Binary:
    Implements the Binary activation function.

6. LeakyReLU:
    Implements the Leaky Rectified Linear Unit (LeakyReLU) activation function with a configurable slope for negative inputs.

7. Swish:
    Implements the Swish activation function, which is defined as `x * sigmoid(beta * x)`.

8. ELU:
    Implements the Exponential Linear Unit (ELU) activation function.

9. Softmax:
    Implements the Softmax function for converting logits to probabilities.

10. SELU:
    Implements the Scaled Exponential Linear Unit (SELU) activation function.

11. GELU:
    Implements the Gaussian Error Linear Unit (GELU) activation function.

12. Softplus:
    Implements the Softplus activation function, which smooths the ReLU function.

13. Arctan:
    Implements the Arctan activation function and its derivative.

14. Signum:
    Implements the Signum activation function, which outputs -1, 0, or 1 based on input sign.

15. Hardmax:
    Implements the Hardmax activation function, which outputs a one-hot vector for the index of the maximum value.

16. LogSigmoid:
    Implements the LogSigmoid activation function, which is the logarithm of the sigmoid function.

17. ReLU6:
    Implements the ReLU6 activation function, which caps the output at 6.

18. TReLU:
    Implements the Thresholded ReLU (TReLU) activation function, which outputs non-zero values only above a threshold.

19. Clip:
    Implements a clipping activation function that constrains inputs to a specified range.

20. Normalize:
    Implements normalization of input values to a specified output range.

21. Custom:
    Allows defining custom activation functions with user-specified forward and backward operations.

22. ZeroCenteredSigmoid:
    Custom activation function made by the author, meant to act as an improvement on conventional Sigmoid, scaled to the range -1 to 1.

23. Dropout:
    Implements the Dropout layer, randomly removing certain data to avoid over fitting the neural network, with controllable paramaters.

22. Conv1D:
    Implements a kernal sliding in a 1D input across the whole input.

Utilities:
----------
- The module uses helper methods from `_Utils` to compute element-wise activation and derivatives.
- Supports various initialization methods for weights, including random, Xavier, He, LeCun, and zero initialization.

Usage:
------
- Define a Dense layer to initialize learnable weights and biases.
- Chain multiple activation functions for non-linear transformations.
- Use the `forward` and `backward` methods for training and inference.

Example:
--------
```python
from pybernetics.Layers import Dense, ReLU
from pybernetics.Models import Sequential
import numpy as np

dense = Dense(2, 1)
relu = ReLU()

X = np.array([1, 2])

dense.forward(X)
relu.forward(dense.outputs)

print(f"Final Outputs: {relu.outputs}")
```
"""

import numpy as np
from . import _random_seed
from . import _Utils
from typing import Callable, Literal, Union

RealNumber = Union[int, float]

# Set the seed for reproducibility. NumPy uses a pseudo-random number generator 
# to produce numbers based on an algorithm (like the Box-Muller transform) for Gaussian distribution.
# Mersenne Twister based on seed below
np.random.seed(_random_seed)

class Dense:
    """
    A dense (fully connected) layer in a neural network.

    This layer connects every input to every output with learnable weights and biases. 
    It performs a linear transformation on the input data.

    Attributes:
        weights (numpy.ndarray): The weights of the layer, initialized randomly using np.random.
        biases (numpy.ndarray): The biases of the layer, initialized to zero.

    Methods:
        forward(inputs):
            Computes the output of the layer given the input data.

        backward(dvalues):
            Computes the gradient of the loss with respect to the inputs, weights, and biases.
    """

    def __init__(self, n_inputs: int, n_neurons: int, weights_init: Literal["random", "xavier", "he", "lecun", "zero"] = "random") -> None:
        """
        Initializes an instance of LayerDense

        Parameters:
            n_inputs (int): The number of input features.
            n_neurons (int): The number of neurons (outputs) in the layer.
        """
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons
        self.weights_init = weights_init

        # Initialize weights based on the specified method
        if weights_init == "random":
            self.weights = np.random.randn(n_inputs, n_neurons) * 0.1

        elif weights_init == "xavier":
            # Xavier initialization (Glorot)
            self.weights = np.random.randn(n_inputs, n_neurons) * np.sqrt(2 / (n_inputs + n_neurons))

        elif weights_init == "he":
            # He initialization (for ReLU)
            self.weights = np.random.randn(n_inputs, n_neurons) * np.sqrt(2 / n_inputs)

        elif weights_init == "lecun":
            # LeCun initialization (for SELU)
            self.weights = np.random.randn(n_inputs, n_neurons) * np.sqrt(1 / n_inputs)

        elif weights_init == "zero":
            # All weights initialized to zero
            self.weights = np.zeros((n_inputs, n_neurons))

        else:
            raise ValueError(f"Invalid initialization method: {weights_init}")

        self.biases = np.zeros((1, n_neurons))

    def get_config(self):
        """
        Returns the configuartion of the Dense layer
        """
        return {
            "n_inputs": self.n_inputs,
            "n_neurons": self.n_neurons,
            "weights_init": self.weights_init,
            "weights": self.weights,
            "biases": self.biases
        }

    @classmethod
    def from_config(cls, config) -> 'Dense':
        from_config_dense = cls(
                                n_inputs=config["n_inputs"],
                                n_neurons=config["n_neurons"],
                                weights_init=config["weights_init"],
                               )

        from_config_dense.weights = config["weights"]
        from_config_dense.biases = config["biases"]

        return from_config_dense

    def forward(self, inputs: np.ndarray) -> None:
        """
        Performs the forward pass of the layer.

        Parameters:
            inputs (numpy.ndarray): The input data to the layer.

        Returns:
            None: The output is stored in the `self.output` attribute.
        """

        self.inputs = inputs
        self.outputs = np.dot(inputs, self.weights) + self.biases

    def backward(self, dvalues: np.ndarray) -> None:
        """
        Performs the backward pass of the layer.

        Parameters:
            dvalues (numpy.ndarray): The gradient of the loss with respect to the output.

        Returns:
            None: The gradients of the loss with respect to the inputs, weights, and biases 
            are stored in the attributes `self.dinputs`, `self.dweights`, and `self.dbiases`.
        """

        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        self.dinputs = np.dot(dvalues, self.weights.T)

class Sigmoid:
    """
    Sigmoid
    =======
    Sigmoid activation function.

    Implements the sigmoid activation function with input and output
    clipping to prevent overflow. The sigmoid function is defined as:
    1 / (1 + exp(-x)).

    Parameters
    ----------
    in_clip_min : float, optional
        Minimum value to clip the input (default is -500).
    in_clip_max : float, optional
        Maximum value to clip the input (default is 500).
    out_clip_min : float, optional
        Minimum value to clip the output (default is 1e-7).
    out_clip_max : float, optional
        Maximum value to clip the output (default is 1 - 1e-7).

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If any of the input parameters are invalid.
    """
    def __init__(self,
                 in_clip_min: RealNumber = -500,
                 in_clip_max: RealNumber = 500,
                 out_clip_min: RealNumber = 1e-7,
                 out_clip_max: RealNumber = 1 - 1e-7
        )-> None:

        # Validate the clipping ranges to ensure they are correct
        if in_clip_min >= in_clip_max:
            raise ValueError("in_clip_min should be less than in_clip_max.")

        if out_clip_min >= out_clip_max:
            raise ValueError("out_clip_min should be less than out_clip_max.")

        self.in_clip_min = in_clip_min
        self.in_clip_max = in_clip_max
        self.out_clip_min = out_clip_min
        self.out_clip_max = out_clip_max

    def forward(self, inputs: np.ndarray) -> None:
        """
        Sigmoid layer forward pass
        --------------------------
        Parameters:
            - 'inputs' (np.ndarray): The array to apply the sigmoid function to (element-wise)
        """
        self.inputs = inputs

        # Clip inputs to prevent overflow
        self.outputs = np.clip(self.inputs, self.in_clip_min, self.in_clip_max)

        # Sigmoid activation function: 1 / (1 + exp(-x))
        self.outputs = 1 / (1 + np.exp(-self.outputs))

        # Clip output to avoid extreme values
        self.outputs = np.clip(self.outputs, self.out_clip_min, self.out_clip_max)

        return self.outputs

    def backward(self, dvalues: np.ndarray) -> None:
        """
        Backward pass for Sigmoid activation function.
        
        Computes the gradient of the loss with respect to the input during backpropagation.
        The gradient is calculated as the derivative of the Sigmoid function 
        multiplied by the gradient of the next layer (`dvalues`).
        
        Parameters
        ----------
        dvalues : np.ndarray
            The gradient of the loss with respect to the output of this layer.
        
        Returns
        -------
        np.ndarray
            The gradient of the loss with respect to the input of this layer.
        """
        self.dinputs = dvalues * (self.outputs * (1 - self.outputs))
        return self.dinputs

    def get_config(self):
        """
        Get the configuration of the Sigmoid layer.

        This method returns the current configuration of the Sigmoid layer, 
        which includes the clipping values for both input and output.

        Returns
        -------
        dict
            A dictionary containing the clipping values for input and output.
        """
        return {
            "in_clip_min": self.in_clip_min,
            "in_clip_max": self.in_clip_max,
            "out_clip_min": self.out_clip_min,
            "out_clip_max": self.out_clip_max
        }

    @classmethod
    def from_config(cls, config: dict) -> 'Sigmoid':
        """
        Create a Sigmoid layer from a configuration dictionary.

        This class method takes a configuration dictionary, which should contain
        the clipping values for input and output, and initializes a `Sigmoid` layer 
        with those values.

        Parameters
        ----------
        config : dict
            A dictionary containing the configuration values for the Sigmoid layer.
            Expected keys: "in_clip_min", "in_clip_max", "out_clip_min", "out_clip_max".

        Returns
        -------
        Sigmoid
            A Sigmoid layer instance initialized with the provided configuration.
        """
        return cls(**config)

class ZeroCenteredSigmoid:
    """
    Designed to be a better implementation of Sigmoid, following Tanh's range of -1 to 1, where x = 0, y = 0, making it zero centered

    `Sigmoid`:
        - Defined as Sigmoid(x) = 1 / (1 + e ** -x).
        - lim (x -> ∞) Sigmoid(x) = 1.
        - lim (x -> -∞) Sigmoid(x) = 0.
        - Can get computationally expensive.
        - Can result in overflows with exponential.
        - Not zero centered.
        - Vanishing gradient problem.
        - Clipping implemented to prevent numerical overflow / instability (inf, -inf, nan).

    `ZeroCenteredSigmoid`:
        - Defined as ZeroCenteredSigmoid(x) = 2 * (1 / (1 + e ** -x)) - 1.
        - Clipping implemented to prevent numerical overflow / instability (inf, -inf, nan).
    """

    def __init__(self,
                 in_clip_min: RealNumber = -500,
                 in_clip_max: RealNumber = 500,
                 out_clip_min: RealNumber = -(1e-7),
                 out_clip_max: RealNumber = 1e-7
        )-> None:

        # Validate the clipping ranges to ensure they are correct
        if in_clip_min >= in_clip_max:
            raise ValueError("in_clip_min should be less than in_clip_max.")

        if out_clip_min >= out_clip_max:
            raise ValueError("out_clip_min should be less than out_clip_max.")

        self.in_clip_min = in_clip_min
        self.in_clip_max = in_clip_max
        self.out_clip_min = out_clip_min
        self.out_clip_max = out_clip_max

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = np.clip(inputs, self.in_clip_min, self.in_clip_max)
        self.outputs = 2 * (1 / (1 + np.exp(-self.inputs))) - 1
        self.outputs = np.clip(self.outputs, self.out_clip_min, self.out_clip_max)

        return self.outputs

    def backward(self, dvalues: np.ndarray) -> None:
        sigmoid_value = 2 / (1 + np.exp(-self.inputs)) - 1
        self.dinputs = dvalues * (2 * sigmoid_value * (1 - sigmoid_value))

        return self.dinputs

    def get_config(self):
        """
        Returns the configuration of the ZeroCenteredSigmoid layer
        """
        return {
            "in_clip_min": self.in_clip_min,
            "in_clip_max": self.in_clip_max,
            "out_clip_min": self.out_clip_min,
            "out_clip_max": self.out_clip_max
        }

    @classmethod
    def from_config(cls, config: dict) -> 'ZeroCenteredSigmoid':
        return cls(**config)

class ReLU:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs
        self.outputs = np.where(inputs > 0.0, inputs, 0.0)

    def backward(self, dvalues: np.ndarray) -> None:
        self.dinputs = dvalues * np.where(self.inputs > 0, 1.0, 0.0)

    def get_config(self):
        """
        Returns the configuartion of the ReLU layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'ReLU':
        return cls()

class Tanh:
    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs
        self.outputs = np.tanh(inputs)

    def backward(self, dvalues: np.ndarray) -> None:
        self.dinputs = dvalues * (1 - self.outputs ** 2)

    def get_config(self):
        """
        Returns the configuartion of the Tanh layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'Tanh':
        return cls()

class Binary:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs
        self.outputs = np.where(inputs >= 0, 1.0, 0.0)

    def backward(self, dvalues: np.ndarray) -> None:
        self.dinputs = np.zeros_like(self.inputs)

    def get_config(self):
        """
        Returns the configuartion of the Binary layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'Binary':
        return cls()

class LeakyReLU:
    def __init__(self, alpha: RealNumber) -> None:
        self.alpha = alpha

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs
        self.outputs = np.where(inputs < 0, self.alpha * inputs, inputs)

    def backward(self, dvalues: np.ndarray) -> None:
        self.outputs = dvalues * np.where(self.inputs > 0.0, 1.0, self.alpha)

    def get_config(self):
        """
        Returns the configuartion of the LeakyReLU layer
        """
        return {
            "alpha": self.alpha
        }

    @classmethod
    def from_config(cls, config: dict) -> 'LeakyReLU':
        return cls(**config)

class Swish:
    def __init__(self, beta: RealNumber = 1) -> None:
        self.beta = beta

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs
        self.outputs = _Utils.Maths.ActivationFunctions.swish(inputs, self.beta)

    def backward(self, dvalues: np.ndarray) -> None:
        self.dinputs = dvalues * _Utils.Helpers.apply_elementwise(_Utils.Maths.ActivationFunctions.Derivatives.swish, self.inputs) # NEEDS WORK

    def get_config(self):
        """
        Returns the configuartion of the Swish layer
        """
        return {
            "beta": self.beta
        }

    @classmethod
    def from_config(cls, config) -> 'Swish':
        return cls(**config)

class ELU:
    def __init__(self, alpha: RealNumber = 1) -> None:
        self.alpha = alpha

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs
        self.outputs = _Utils.Maths.ActivationFunctions.elu(inputs, self.alpha)

    def backward(self, dvalues: np.ndarray) -> None:
        self.dinputs = dvalues * _Utils.Maths.ActivationFunctions.Derivatives.elu(self.inputs, self.alpha)

    def get_config(self):
        """
        Returns the configuartion of the ELU layer
        """
        return {
            "alpha": self.alpha
        }

    @classmethod
    def from_config(cls, config) -> 'ELU':
        return cls(**config)

class Softmax:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs

        exp_values = np.exp(inputs - np.max(inputs, axis=-1, keepdims=True))  # Prevent overflow
        self.outputs = exp_values / np.sum(exp_values, axis=-1, keepdims=True)

    def backward(self, dvalues: np.ndarray) -> None:
        self.dinputs = np.zeros_like(dvalues)

        for i in range(len(dvalues)):
            jacobian_matrix = np.diagflat(self.outputs[i]) - np.outer(self.outputs[i], self.outputs[i])
            self.dinputs[i] = np.dot(jacobian_matrix, dvalues[i])

    def get_config(self):
        """
        Returns the configuartion of the Softmax layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'Softmax':
        return cls()

class SELU:
    def __init__(self, alpha: RealNumber = 1.67326, scale: RealNumber = 1.0507) -> None:
        self.alpha = alpha  # Coefficient for the negative part of the function
        self.scale = scale  # Scaling factor for the output

    def forward(self, inputs: np.ndarray) -> None:
        """Applies the SELU activation function element-wise on the input array."""
        self.inputs = inputs
        self.outputs = self.scale * np.where(self.inputs > 0, self.inputs, self.alpha * (np.exp(self.inputs) - 1))

    def backward(self, dvalues: np.ndarray) -> None:
        """Calculates the gradient (derivative) of the SELU activation function."""
        self.dinputs = dvalues * self.scale * np.where(self.inputs > 0, 1, self.alpha * np.exp(self.inputs))

    def get_config(self):
        """
        Returns the configuartion of the SELU layer
        """
        return {
            "alpha": self.alpha,
            "scale": self.scale
        }

    @classmethod
    def from_config(cls, config) -> 'SELU':
        return cls(**config)

class GELU:
    def __init__(self) -> None:
        pass

    @staticmethod
    def gelu(input: np.ndarray) -> np.ndarray:
        # GELU function
        return 0.5 * input * (1 + np.tanh(np.sqrt(2 / np.pi) * (input + 0.044715 * np.power(input, 3))))

    @staticmethod
    def gelu_derivative(input: np.ndarray) -> np.ndarray:
        # Derivative of GELU
        factor = np.sqrt(2 / np.pi)
        z = factor * (input + 0.044715 * np.power(input, 3))
        sech2 = 1 - np.tanh(z)**2  # sech^2(z)
        return 0.5 * (1 + np.tanh(z)) + input * sech2 * factor * (1 + 0.13345 * np.power(input, 2))

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs
        self.outputs = self.gelu(self.inputs)

    def backward(self, dvalues: np.ndarray) -> None:
        self.dinputs = dvalues * self.gelu_derivative(self.inputs)

    def get_config(self):
        """
        Returns the configuartion of the GELU layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'GELU':
        return cls()

class Softplus:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """Compute the Softplus activation."""
        self.inputs = inputs
        self.outputs = np.log(1 + np.exp(inputs))

    def backward(self, dvalues: np.ndarray) -> np.ndarray:
        """Compute the derivative of Softplus with respect to the inputs."""
        self.dinputs = dvalues * (1 / (1 + np.exp(-self.inputs)))

    def get_config(self):
        """
        Returns the configuartion of the Softplus layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'Softplus':
        return cls()

class Arctan:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> None:
        """Compute the Arctan (inverse tangent) activation."""
        self.inputs = inputs
        self.outputs = np.arctan(inputs)

    def backward(self, dvalues: np.ndarray) -> None:
        """Compute the derivative of Arctan with respect to the inputs."""
        self.dinputs = dvalues / (1 + self.inputs ** 2)  # Derivative of Arctan

    def get_config(self):
        """
        Returns the configuartion of the Arctan layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'Arctan':
        return cls()

class Signum:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> None:
        """Compute the Signum (sign) activation."""
        self.inputs = inputs
        self.outputs = np.sign(inputs)

    def backward(self, dvalues: np.ndarray) -> None:
        """Compute the derivative of Signum with respect to the inputs."""
        # The derivative of the signum function is 0 everywhere except at 0,
        # where it's undefined, so we simply return 0 as a placeholder.
        self.dinputs = np.zeros_like(self.inputs)

    def get_config(self):
        """
        Returns the configuartion of the Signum layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'Signum':
        return cls()

class Hardmax:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> None:
        """Compute the Hardmax activation."""
        self.inputs = inputs
        # Find the index of the maximum value in the array
        self.outputs = np.zeros_like(self.inputs)
        self.outputs[np.argmax(self.inputs)] = 1

    def backward(self, dvalues: np.ndarray) -> None:
        """Compute the derivative of Hardmax."""
        # Initialize the gradient with zeros
        self.dinputs = np.zeros_like(self.inputs)

        # Set the gradient to 1 for the index of the maximum value
        self.dinputs[np.argmax(self.inputs)] = 1  # Derivative is 1 at the max value index

    def get_config(self):
        """
        Returns the configuartion of the Hardmax layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'Hardmax':
        return cls()

class LogSigmoid:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> None:
        """Compute the LogSigmoid activation."""
        self.inputs = inputs
        self.outputs = -np.log(1 + np.exp(-self.inputs))  # LogSigmoid formula

    def backward(self, dvalues: np.ndarray) -> None:
        """Compute the derivative of LogSigmoid."""
        sigmoid = 1 / (1 + np.exp(-self.inputs))  # Sigmoid function
        self.dinputs = dvalues * sigmoid * (1 - sigmoid)  # Sigmoid derivative

    def get_config(self):
        """
        Returns the configuartion of the LogSigmoid layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'LogSigmoid':
        return cls()

class ReLU6:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> None:
        """Forward pass for ReLU6."""
        self.inputs = inputs
        self.outputs = np.clip(self.inputs, 0, 6)  # Clipping values between 0 and 6

    def backward(self, dvalues: np.ndarray) -> None:
        """Backward pass for ReLU6."""
        self.dinputs = dvalues * (self.inputs > 0) * (self.inputs < 6)  # Derivative for ReLU6

    def get_config(self):
        """
        Returns the configuartion of the ReLU6 layer
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'ReLU6':
        return cls()

class TReLU:
    def __init__(self, theta: RealNumber = 1.0) -> None:
        self.theta = theta

    def forward(self, inputs: np.ndarray) -> None:
        self.inputs = inputs
        self.outputs = np.where(self.inputs > self.theta, self.inputs, 0)

    def backward(self, dvalues: np.ndarray) -> None:
        self.dinputs = dvalues * (self.inputs > self.theta)

    def get_config(self) -> dict:
        """
        Returns the configuartion of the GELU layer
        """
        return {
            "theta": self.theta
        }

    @classmethod
    def from_config(cls, config: dict) -> 'GELU':
        return cls(**config)

class Clip:
    def __init__(self, min_: RealNumber, max_: RealNumber) -> None:
        """
        Initialize the Clip activation function.
        :param min_: Minimum value for clipping.
        :param max_: Maximum value for clipping.
        """
        self.clip_min = min_
        self.clip_max = max_

    def forward(self, inputs: np.ndarray) -> None:
        """
        Forward pass for the Clip function.
        :param inputs: Input array to clip.
        """
        self.inputs = inputs
        self.outputs = np.clip(self.inputs, self.clip_min, self.clip_max)

    def backward(self, dvalues: np.ndarray) -> None:
        """
        Backward pass for the Clip function.
        :param dvalues: Gradients flowing from the next layer.
        """
        # Gradients are passed only where the inputs are not clipped
        self.dinputs = dvalues * ((self.inputs > self.clip_min) & (self.inputs < self.clip_max))

    def get_config(self):
        """
        Returns the configuartion of the Clip layer
        """
        return {
            "min_": self.clip_min,
            "max_": self.clip_max
        }

    @classmethod
    def from_config(cls, config: dict) -> 'Clip':
        return cls(**config)

class Normalize:
    def __init__(self, in_min: RealNumber, in_max: RealNumber, out_min: RealNumber, out_max: RealNumber) -> None:
        """
        Initialize the Normalization activation function.
        :param in_min: Minimum (inclusive) value of the input.
        :param in_max: Maximum (inclusive) value of the input.
        :param out_min: Minimum (inclusive) value of the output.
        :param out_max: Maximum (inclusive) value of the output.
        """
        self.in_min = in_min
        self.in_max = in_max
        self.out_min = out_min
        self.out_max = out_max

    def forward(self, inputs: np.ndarray) -> None:
        """
        Forward pass for normalization.
        :param inputs: Input array to normalize.
        """
        self.inputs = inputs
        # Perform normalization: scale inputs to the output range
        self.outputs = self.out_min + (inputs - self.in_min) * (self.out_max - self.out_min) / (self.in_max - self.in_min)

    def backward(self, dvalues: np.ndarray) -> None:
        """
        Backward pass for normalization.
        :param dvalues: Gradients flowing from the next layer.
        """
        # Gradients pass unchanged through normalization, scaled by the input-output ratio
        self.dinputs = dvalues * (self.out_max - self.out_min) / (self.in_max - self.in_min)

    def get_config(self):
        """
        Returns the configuartion of the Normalization layer
        """
        return {
            "in_min": self.in_min,
            "in_max": self.in_max,
            "out_min": self.out_min,
            "out_max": self.out_max
        }

    @classmethod
    def from_config(cls, config: dict) -> 'Normalize':
        return cls(**config)

class Custom:
    def __init__(self, activation_function: Callable[[np.ndarray], np.ndarray], derivative_function: Callable[[np.ndarray], np.ndarray]) -> None:
        """
        Initialize the custom activation function.

        Both the forward and backward pass functions will be passed a np.ndarray when they are called.

        :param activation_function: A callable function for the forward pass (e.g., f(x)).
        :param derivative_function: A callable function for the backward pass (e.g., f'(x)).
        """
        self.activation_function = activation_function
        self.derivative_function = derivative_function

    def forward(self, inputs: np.ndarray) -> None:
        """
        Forward pass for the custom activation function.

        :param inputs: Input array.
        """
        self.inputs = inputs
        self.outputs = self.activation_function(self.inputs)

    def backward(self, dvalues: np.ndarray) -> None:
        """
        Backward pass for the custom activation function.

        :param dvalues: Gradients flowing from the next layer.
        """
        self.dinputs = dvalues * self.derivative_function(self.inputs)

    def get_config(self) -> dict:
        return {}
    
    @classmethod
    def from_config(cls, config: dict) -> 'Custom':
        return cls(**config)

class Flatten:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """
        Flatten the input to a 1D vector.
        """
        self.input_shape = inputs.shape  # Store the original shape for later use
        self.outputs = inputs.flatten()
        return self.outputs

    def backward(self, dvalues: np.ndarray) -> np.ndarray:
        """
        Reshape the gradients back to the original input shape.
        """
        self.dinputs = dvalues.reshape(self.input_shape)
        return self.dinputs

    def get_config(self) -> dict:
        """
        Return an empty config as Flatten doesn't require any parameters.
        """
        return {}

    @classmethod
    def from_config(cls, config=None) -> 'Flatten':
        """
        Create an instance of Flatten (no parameters needed).
        """
        return cls()

class Dropout:
    def __init__(self, rate: RealNumber) -> None:
        """
        Initialize a 'Dropout' layer instance.

        Params:
            - 'rate' (RealNumber / Union[int, float]: Dropout rate, e.g., 0.5 means 50% dropout.

        Returns:
            - None (None): Python initialization 'magic methods' do not return values.
        """
        self.rate = rate

    def forward(self, inputs: np.ndarray):
        """
        Forward pass, appply a numpy mask to the input array (np.ndarray).

        Params:
            - 'inputs' (np.ndarray): Neural network inputs, (2D standard).
        
        Returns:
            - 'outputs' (np.ndarrau): The layer's outputs.
        
        Notes:
            - Reccommended pybernetics and standard convention architecure uses [layer].outputs,
              rather than relying on return values
        """
        # Generate random dropout mask: 1 means keep the neuron, 0 means drop it
        self.mask = np.random.binomial(1, 1 - self.rate, size=inputs.shape)
        self.outputs = inputs * self.mask
        return self.outputs

    def backward(self, d_values: np.ndarray):
        """
        Backward pass, simply propogate the gradient through the layer's mask.

        Params:
            - 'd_values' (np.ndarray): Derivative values from the previous (next) layer
        Returns:
            - 'dinputs' (np.ndarray: The dinputs of the layer.

        Notes:
            - Reccommended pybernetics and standard convention architecure uses [layer].dinputs,
              rather than relying on return values.
        """
        self.dinputs = d_values * self.mask
        return self.dinputs

    def get_config(self) -> dict:
        """
        Deconstruct the 'Dropout' object to a kwarg (key word arguments) list, in dictionary format.

        Returns:
            - 'config' (dict): Config data for reconstruction.
        """
        return {
            "rate": self.rate
        }

    @classmethod
    def from_config(cls, config) -> 'Dropout':
        """
        Reconstruct the seralizated object using kwargs (key word arguments).

        'config':
            - The config dictionary to pass as kwargs to Dropout.__init__.
            - Reccomended to be obtained from Dropout.get_config.

        Returns:
            - 'Dropout' (object): The reconstructed class from the kwarg dict.
        """
        return cls(**config)

# Low support below:
class Conv1D:
    """
    A 1D Convolutional layer for a neural network.

    This layer applies a 1D convolution operation on the input data. It slides a kernel across the input to produce output feature maps.

    Attributes:
        weights (numpy.ndarray): The convolutional filters (kernels) of the layer, initialized randomly.
        biases (numpy.ndarray): The biases of the layer, initialized to zero.
        stride (int): The step size by which the kernel moves across the input.
        padding (int): The number of zero-padding applied to the input for the convolution.
    
    Methods:
        forward(inputs):
            Computes the output of the layer given the input data.
        
        backward(dvalues):
            Computes the gradient of the loss with respect to the inputs, weights, and biases.
    """

    def __init__(self, n_inputs: int, n_filters: int, kernel_size: int, stride: int = 1, padding: int = 0, weights_init: Literal["random", "xavier", "he", "lecun", "zero"] = "random") -> None:
        """
        Initializes an instance of Conv1D
        
        Parameters:
            n_inputs (int): The number of input features (channels).
            n_filters (int): The number of filters (kernels) in the layer.
            kernel_size (int): The size of the kernel (filter).
            stride (int): The step size for the convolution.
            padding (int): The number of zero-padding applied to the input.
            weights_init (str): The method for initializing the weights ("random", "xavier", "he", "lecun", "zero").
        """

        self.stride = stride
        self.padding = padding

        # Initialize weights based on the specified method
        if weights_init == "random":
            self.weights = 0.1 * np.random.randn(n_filters, n_inputs, kernel_size)
        
        elif weights_init == "xavier":
            self.weights = np.random.randn(n_filters, n_inputs, kernel_size) * np.sqrt(2 / (n_inputs + kernel_size))
        
        elif weights_init == "he":
            self.weights = np.random.randn(n_filters, n_inputs, kernel_size) * np.sqrt(2 / n_inputs)
        
        elif weights_init == "lecun":
            self.weights = np.random.randn(n_filters, n_inputs, kernel_size) * np.sqrt(1 / n_inputs)
        
        elif weights_init == "zero":
            self.weights = np.zeros((n_filters, n_inputs, kernel_size))
        
        else:
            raise ValueError(f"Invalid initialization method: {weights_init}")

        self.biases = np.zeros((n_filters, 1))

    def forward(self, inputs: np.ndarray) -> None:
        """
        Performs the forward pass of the convolutional layer.
        
        Parameters:
            inputs (numpy.ndarray): The input data to the layer.
        
        Returns:
            None: The output is stored in the `self.outputs` attribute.
        """
        self.inputs = inputs
        batch_size, n_channels, input_length = inputs.shape
        n_filters, n_channels, kernel_size = self.weights.shape

        # Apply padding if necessary
        if self.padding > 0:
            self.inputs = np.pad(self.inputs, ((0, 0), (0, 0), (self.padding, self.padding)), mode='constant', constant_values=0)
        
        output_length = (input_length - kernel_size) // self.stride + 1
        self.outputs = np.zeros((batch_size, n_filters, output_length))

        for i in range(batch_size):
            for f in range(n_filters):
                for j in range(output_length):
                    start = j * self.stride
                    end = start + kernel_size
                    self.outputs[i, f, j] = np.sum(self.inputs[i, :, start:end] * self.weights[f]) + self.biases[f]
    
    def backward(self, dvalues: np.ndarray) -> None:
        """
        Performs the backward pass of the convolutional layer.
        
        Parameters:
            dvalues (numpy.ndarray): The gradient of the loss with respect to the output.
        
        Returns:
            None: The gradients of the loss with respect to the inputs, weights, and biases 
            are stored in the attributes `self.dinputs`, `self.dweights`, and `self.dbiases`.
        """
        batch_size, n_filters, output_length = dvalues.shape
        _, n_channels, input_length = self.inputs.shape
        _, _, kernel_size = self.weights.shape

        self.dweights = np.zeros_like(self.weights)
        self.dbiases = np.zeros_like(self.biases)
        self.dinputs = np.zeros_like(self.inputs)

        for i in range(batch_size):
            for f in range(n_filters):
                self.dbiases[f] += np.sum(dvalues[i, f])
                for j in range(output_length):
                    start = j * self.stride
                    end = start + kernel_size
                    self.dweights[f] += self.inputs[i, :, start:end] * dvalues[i, f, j]
                    self.dinputs[i, :, start:end] += self.weights[f] * dvalues[i, f, j]
    
        # Remove padding from the input gradients if padding was applied
        if self.padding > 0:
            self.dinputs = self.dinputs[:, :, self.padding:-self.padding] if self.padding > 0 else self.dinputs