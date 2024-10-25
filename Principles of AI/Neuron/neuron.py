ss+import random;

class Neuron:
    def __init__(self):
        self.weight1 = random.random();
        self.weight2 = random.random();
        self.t = random.random();
        self.count = 1
        
    def predict(self, x1, x2):
        y_pred = 0
        if (x1 * self.weight1 + x2  * self.weight2) > self.t:
            y_pred = 1
        return y_pred
    
    def learn(self, x1, x2, y_act):
        error = self.predict(x1, x2) - y_act;
        self.weight1 -= error * x1 / 100
        self.weight2 -= error * x2 / 100
        self.t += error / 100
        self.count += 1
        print("\nWeights Changed | Epoch: ", self.count)
        print("Weight 1: ", self.weight1)
        print("Weight 2: ", self.weight2)
        print("Threshold: ", self.t)

data = [
    [1, 1, 1],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]

neuron = Neuron()

def startTrain():
    for row in data
        neuron.learn(row[0], row[1], row[2])
        
def startPredict():
    if (neuron.predict(1, 1) == 1 and neuron.predict(1, 0) == 0 and neuron.predict(0, 1) == 0 and neuron.predict(0, 0) == 0):
        return True
    return False

while True:
    startTrain()
    if startPredict():
        break
    
for row in data:
    print("\nPrediction: ", neuron.predict(row[0], row[1]), " | Actual: ", row[2])
