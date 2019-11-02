import numpy as np


class Network:

    def __init__(self,layerSizes):
        self.layerSizes = layerSizes

    def FF(self):


    def _BP(self):

    def _init_model(self):
        w0 = self._generate_weights(self.layerSizes[0], self.layerSizes[1])
        w1 = self._generate_weights(self.layerSizes[1], self.layerSizes[2])
        w2 = self._generate_weights(self.layerSizes[2], self.layerSizes[3])
        w3 = self._generate_weights(self.layerSizes[3], self.layerSizes[4])

    def _generate_bias(self, input_dim):

    def _generate_weights(self, input_dim, layer_dim):
        weights = np.random.rand(input_dim, layer_dim)
        return weights

    def _sigmoid(self, x):

    def _deriv_sigmoid(self, x):

    def _error(self,x):

    def _deriv_error(self,x):


class Actuator:

    def __init__(self, network):
        self.network = network

    def train(self,x):

    def test(self,x):
