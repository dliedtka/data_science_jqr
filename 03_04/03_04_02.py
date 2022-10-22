#!/usr/bin/env python3 
# 3.4.2 Normalize data


# no imports allowed, just use built utilities to get random data
from utils import random_data, start_time, elapsed_time


def normalize_random_data(num_features, num_samples, verbose=False, 
    timed=False):
    '''
    '''

    # create a random dataset of integers
    if timed:
        st = start_time()
    data = random_data(num_features, num_samples, seeded=True)
    if timed:
        print (f"{elapsed_time(st):.2f} seconds to create data.")
    if verbose:
        print ("")
        for sample in data:
            print (sample)
    
    if timed:
        st = start_time()

    # compute mean for each feature
    means = []
    for feat in range(num_features):
        means.append(sum([data[i][feat] for i in range(num_samples)]) / 
            num_samples)
    
    # compute standard deviation for each feature
    s_devs = [] 
    for feat in range(num_features):
        s_devs.append((sum([(data[i][feat] - means[feat]) ** 2 for i in
            range(num_samples)]) / num_samples) ** 0.5)

    # normalize data
    for i in range(num_samples):
        for feat in range(num_features):
            data[i][feat] = (data[i][feat] - means[feat]) / s_devs[feat]
    if verbose:
        print ("")
        for sample in data:
            print (sample)
    
    if timed:
        print (f"{elapsed_time(st):.2f} seconds to normalize.")


if __name__ == "__main__":
    normalize_random_data(3, 4, verbose=True, timed=True)
    print ("")
    normalize_random_data(25, 100000, timed=True)
