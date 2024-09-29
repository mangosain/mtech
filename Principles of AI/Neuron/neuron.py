import random

class Neuron:
    def __init__(self):
        self.weight1 = random.random()
        self.weight2 = random.random()
        self.bias = random.random()
        self.count = 0
        
    def predict(self, x1, x2):
        y_pred = 0
        if (self.weight1 * x1 + self.weight2 * x2) > self.bias:
            y_pred = 1
        return y_pred
    
    def learn(self, x1, x2, y_act):
        error = self.predict(x1, x2) - y_act
        self.weight1 -= error * x1 * 0.01
        self.weight2 -= error * x2 * 0.01
        self.bias += error * 0.01
        self.count += 1
        print("\nWeights Changed | Epoch: ", self.count)
        print("Weight 1: ", self.weight1)
        print("Weight 2: ", self.weight2)
        print("Bias: ", self.bias)

# Create a Neuron object
neuron = Neuron()

# input array
inputArray = [
    [1, 1, 1],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]

def trainFuntion():
    for i in range(len(inputArray)):
        neuron.learn(inputArray[i][0], inputArray[i][1], inputArray[i][2])
        
def testFunction():
    for i in range(len(inputArray)):
        if neuron.predict(inputArray[i][0], inputArray[i][1]) != inputArray[i][2]:
            return False
    return True

while True:
    # Training
    trainFuntion()
    
    # Testing
    if testFunction():
        break
    
for i in range(len(inputArray)):
    print("\nPrediction: ", neuron.predict(inputArray[i][0], inputArray[i][1]), " | Actual: ", inputArray[i][2])