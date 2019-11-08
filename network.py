import numpy as np

class Network:

    def __init__(self,layerSizes):
        self.layerSizes = layerSizes

    def FF(self, input):
        self.input = input

        self.o0 = input.dot(self.w0)
        self.a0 = self._sigmoid(self.o0)

        self.o1 = self.a0.dot(self.w1)
        self.a1 = self._sigmoid(self.o1)

        self.o2 = self.a1.dot(self.w2)
        self.a2 = self._sigmoid(self.o2)

        self.o3 = self.a2.dot(self.w3)
        self.a3 = self._sigmoid(self.o3)

    def BP(self, expected):

    def calcLoss(self, expected):
        self.loss = self._error(expected)
        return self.loss

    def _init_model(self):
        self.w0 = self._generate_weights(self.layerSizes[0], self.layerSizes[1])
        self.w1 = self._generate_weights(self.layerSizes[1], self.layerSizes[2])
        self.w2 = self._generate_weights(self.layerSizes[2], self.layerSizes[3])
        self.w3 = self._generate_weights(self.layerSizes[3], self.layerSizes[4])

    def _generate_bias(self, input_dim):

    def _generate_weights(self, input_dim, layer_dim):
        weights = np.random.rand(input_dim + 1, layer_dim)
        return weights

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _deriv_sigmoid(self, x):
        return x * (1 - x)

    def _error(self,x):
        return (1 / (2 * x.shape[0])) * np.sum(np.square(self.a3 - x))

    def _deriv_error(self, x):
        return (1 / x.shape[0]) * np.sum(self.a3 - x) * x

class Actuator:

    def __init__(self, network):
        self.network = network

    def train(self, x, y, batchSize=1, epochs=1, randomize=False, valPercentage=0.0):
        if valPercentage > 0:
            valSize = int(x.shape[0] * valPercentage)
            valX = x[:valSize]
            valY = y[:valSize]
            trainX = x[valSize:]
            trainY = y[valSize:]
        else:
            trainX = x
            trainY = y

        trainXBatches = []
        trainYBatches = []
        valXBatches = []
        valYBatches = []

        i = 0

        while i + batchSize < trainX.shape[0]:

            trainXBatches.append(trainX[i:i + batchSize + 1])
            trainYBatches.append(trainY[i:i + batchSize + 1])

            i += batchSize

        i = 0

        while valPercentage > 0 and i + batchSize < valX.shape[0]:

            valXBatches.append(valX[i:i + batchSize + 1])
            valYBatches.append(valY[i:i + batchSize + 1])

            i += batchSize

        for e in range(epochs):
            if randomize:
                _randomSync(trainX, trainY)

            network.FF(trainX)
            print(network.calcLoss(trainY))
            network.BP()


    def _randomSync(self, a, b):
        rng_state = np.random.get_state()
        np.random.shuffle(a)
        np.random.set_state(rng_state)
        np.random.shuffle(b)

    def test(self,x):
