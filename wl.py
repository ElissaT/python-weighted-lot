import numpy as np

def weight_lot(weights):
    container_list = []

    for (name, weight) in other_weights.items():
       for _ in range(weight):
           container_list.append(name)

    return np.random.choice(container_list)

other_weights = {
    'green': 1,
    'yellow': 2,
    'red': 3
}

print(weight_lot(other_weights))