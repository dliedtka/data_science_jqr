import time 
import random


def start_time() -> float:
    '''
    Use with elapsed_time() to compute time elapsed.
    @return Seconds since the epoch.
    '''
    return time.time()


def elapsed_time(start_time: float) -> float:
    '''
    Compute time elapsed since you called start_time().
    @param start_time Return value from start_time().
    @return Number of seconds since start_time().
    '''
    return time.time() - start_time


def random_data(num_features: int, num_samples: int, seeded: bool=False
    ) -> list[list[int]]:

    '''
    Generate a "random" num_samples x num_features matrix of data. Each feature 
    will be randomly generated between a min and max value (each randomly 
    selected between -100 and 100 inclusive).
    @param num_features The number of features in the matrix to return.
    @param num_samples The number of samples in the matrix to return.
    @return num_samples x num_features matrix of "random" data
    '''

    if seeded:
        random.seed(42196)
    
    data = []
    for _ in range(num_features):
        high = random.randint(-100, 100)
        low = random.randint(-100, 100)
        if low > high:
            tmp = low 
            low = high 
            high = tmp 
        data.append([random.randint(low,high) for __ in range(num_samples)])
    
    return [[data[j][i] for j in range(num_features)] 
        for i in range(num_samples)]
