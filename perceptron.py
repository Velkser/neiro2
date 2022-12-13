#TODO More neiro
import numpy as np

# Функция для расчета изменения фесов
def sigmoid(x):
    return 1/(1+np.exp(-x))

#Тренировочные данные
training_inputs = np.array([[0,0,1], #0
                            [1,1,1], #1
                            [1,0,0], #1
                            [0,1,0],
                            [1,0,1],
                            [0,1,1],
                            [1,0,0],
                            [0,0,0]])#0

training_outputs = np.array([[0,1,1,0,1,0,1,0]]).T

np.random.seed(1)

sinaptik_weights = 2*np.random.random((3,1)) - 1



#Метод обратного распространения
for i in range(200000):
    input_layer =training_inputs
    outputs = sigmoid( np.dot(input_layer, sinaptik_weights))
    
    err = training_outputs - outputs
    adjustments = np.dot(input_layer.T, err * (outputs * (1-outputs)))
    
    sinaptik_weights = sinaptik_weights + adjustments
    
print("Весы после обучения: \n", sinaptik_weights, "\n")
print("Результат после обучения: \n", outputs, "\n")

#Tests
test_inputs = [np.array([0,0,1]),
               np.array([0,1,0]),
               np.array([1,0,0]),
               np.array([0,1,1]),
               np.array([1,0,1]),
               np.array([1,1,0]),
               np.array([1,1,1])]
print("Новая ситуация: ")
for i in test_inputs:
    outputs = sigmoid( np.dot(i, sinaptik_weights))
    print(outputs)
