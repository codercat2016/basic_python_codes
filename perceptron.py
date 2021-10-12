import numpy as np
import matplotlib.pyplot as plt

features = np.array([[0,0]
                    ,[0,1]
                    ,[1,0]
                    ,[1,1]
])

labels = np.array([0,0,0,1])
w = [0.9, 0.9]
threshold = 0.5
learning_rate = 0.1
epoch = 20


for j in range(0, epoch):
    global_delta = 0 
    for i in range (0, features.shape[0]):
        actual = labels[i]
        instance = features[i]

        x0 = instance[0]
        x1 = instance[1]

        sum_unit = x0* w[0] + x1*w[1]

        if sum_unit > threshold :
            fire =1
        else:
            fire = 0

        delta = actual -fire
       
        global_delta = global_delta + abs(delta)
        # print("prediction:", fire, "wheras actual was", actual, "error:",delta,")")

        w[0] = w[0] + delta * learning_rate
        w[1] = w[1] + delta * learning_rate
    print(global_delta)    
    
    if(global_delta == 0):
        break
    
    






