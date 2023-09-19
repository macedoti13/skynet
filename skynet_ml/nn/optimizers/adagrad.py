from skynet_ml.nn.optimizers.optimizer import Optimizer
from skynet_ml.nn.layers.layer import Layer
import numpy as np

class AdaGrad(Optimizer):
    """
    AdaGrad (Adaptive Gradient Algorithm) optimization algorithm.

    AdaGrad is an adaptive learning rate optimization algorithm designed to improve 
    the performance and training speed of machine learning algorithms. It adapts 
    the learning rates of all model parameters by scaling them inversely proportional 
    to the square root of the sum of all their historical squared values.

    The primary idea behind AdaGrad is that frequently occurring features should 
    have their learning rates decreased, while infrequent features should have their 
    learning rates increased. This can be especially useful for sparse data.

    Inherits from:
    - Optimizer: Base class for optimization algorithms.

    Attributes
    ----------
    learning_rate : float
        The initial learning rate for the optimizer.

    Methods
    -------
    update(layer: Layer) -> None:
        Updates the weights and biases of the provided layer using AdaGrad.

    _update_v(layer: Layer) -> None:
        Internal helper method to update the accumulated squared gradients.
    """
    
    def update(self, layer: Layer) -> None:
        """
        Updates the weights and biases of the provided layer using the AdaGrad algorithm.
        
        The learning rate is adapted based on the accumulation of squared gradients up to the current step.
        This helps in adjusting the learning rates of the weights during the optimization process.
        Frequently occurring features should have their learning rates decreased and infrequent ones should 
        have them increased.

        Parameters
        ----------
        layer : Layer
            The layer whose weights and biases need to be updated.

        Returns
        -------
        None
        """
        epsilon = 1e-15
        self._update_v(layer)
        
        gradient_normalization_weights = np.sqrt(layer.vweights) + epsilon # normalizing the gradient for weights
        normalized_learning_rate = self.learning_rate / gradient_normalization_weights # normalizing the learning rate
        layer.weights -= normalized_learning_rate * layer.dweights # updating the weights
        
        if layer.has_bias:
            gradient_normalization_biases = np.sqrt(layer.vbiases) + epsilon # normalizing the gradient for biases
            normalized_learning_rate = self.learning_rate / gradient_normalization_biases # normalizing the learning rate
            layer.biases -= normalized_learning_rate * layer.dbiases # updating the biases
            
            
    def _update_v(self, layer: Layer) -> None:
        """
        Internal helper method to update the accumulated squared gradients (vweights and vbiases) for a layer.

        For each parameter, this method accumulates the squared gradients, which are used in the update step
        to adjust the learning rate for that particular parameter.

        Parameters
        ----------
        layer : Layer
            The layer whose accumulated squared gradients need to be updated.

        Returns
        -------
        None
        """
        if not hasattr(layer, 'vweights'):
            layer.initialize_v() # initializing the vweights and vbiases attributes if they don't exist
            
        layer.vweights += layer.dweights ** 2 # updating the vweights
        
        if layer.has_bias:
            layer.vbiases += layer.dbiases ** 2 # updating the vbiases