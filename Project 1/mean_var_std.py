import numpy as np

def calculate(input):
    
    # first try reshaping input to a 3x3 matrix, throwing an exception if the reshape fails.
    # this ensures only a 9-element list will get through
    # because the only number with a prime factorization of (3, 3) is 9.
    
    try: 
        np.reshape(input, (3, 3))
    except ValueError:
        raise ValueError('List must contain nine numbers.')
        
    input_3by3 = np.reshape(input, (3, 3))
        
    # initialize a dict of empty lists to populate.
        
    stats = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    
    # iterate through the matrix data 3 times: twice with the axis set to the iteration count,
    # the third time with the axis set to None (resulting in a whole matrix calculation).
    # chain the cast back to a Python List right then and there.
    
    for i in range(3):
        selected_axis = i if i < 2 else None
        stats['mean'].append(input_3by3.mean(axis=selected_axis).tolist())
        stats['variance'].append(input_3by3.var(axis=selected_axis).tolist())
        stats['standard deviation'].append(input_3by3.std(axis=selected_axis).tolist())
        stats['max'].append(input_3by3.max(axis=selected_axis).tolist())
        stats['min'].append(input_3by3.min(axis=selected_axis).tolist())
        stats['sum'].append(input_3by3.sum(axis=selected_axis).tolist())
        
    # here's your piping hot stat dictionary, ready to consume before John Oliver comes on!

    return stats