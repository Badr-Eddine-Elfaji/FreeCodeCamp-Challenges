import numpy as np

def calculate(list) :
    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.")
    
    #Convert list into a numpy array of 3,3
    matrix = np.array(list).reshape(3, 3)

    #Calculate Statistics
    calculations = {
        "Mean": [
            matrix.mean(axis=0).tolist(),    #Columns
            matrix.mean(axis=1).tolist(),    #Rows
            matrix.mean().tolist(),          #Flattened
        ],
        "Variance": [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist(),
        ],
        "Standard Deviation": [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist(),
        ],
        "Max": [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist(),
        ],
        "Min": [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist(),
        ],
        "Sum": [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist(),
        ],
    }
    return calculations
print(calculate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
