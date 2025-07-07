import numpy as np

def calculate(list):
    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.")
    
    #Convert list into a numpy array of 3,3
    matrix = np.array(list).reshape(3,3)

    #Calculate Statistics
    calculations = {
        "mean": [
            matrix.mean(axis=0).tolist(),    #Columns
            matrix.mean(axis=1).tolist(),    #Rows
            matrix.mean().tolist(),          #Flattened
        ],
        "variance": [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist(),
        ],
        "standard deviation": [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist(),
        ],
        "max": [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist(),
        ],
        "min": [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist(),
        ],
        "sum": [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist(),
        ],
    }

    return calculations
