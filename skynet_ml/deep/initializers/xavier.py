import numpy as np

class Xavier:
    """
    Xavier initializer. Best suited for sigmoid and tanh activation functions.
    
    This initializer uses normal distribution with mean 0 and variance 1/n. 
    """    
    
    def initialize_weights(self, input_dim: int, output_dim: int) -> np.array:
        """
        Initializes the weights from the normal distribution.

        Args:
            input_dim (int): Dimension of the input data or number of input neurons.
            output_dim (int): Number of output neurons.

        Returns:
            np.array:  A 2D array of shape (output_dim, input_dim) initialized with Xavier algorithm.
        """        
        return np.random.normal(0, np.sqrt(1/input_dim), size=(output_dim, input_dim))
    
    
    def initialize_bias(self, input_dim: int, output_dim: int, has_bias: bool = True) -> np.array:
        """
        Initializes the bias from the normal distribution.

        Args:
            input_dim (int): Dimension of the input data or number of input neurons.
            output_dim (int): Number of output neurons.
            has_bias (bool, optional): Determines whether to include a bias term. Defaults to True.
            
        Returns:
            np.array:  A 2D array of shape (output_dim, 1) initialized with Xavier algorithm
        """        
        if has_bias:
            return np.random.normal(0, np.sqrt(1/input_dim), size=(output_dim, 1))
        
        return np.zeros((output_dim, 1))
