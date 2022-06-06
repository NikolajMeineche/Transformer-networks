#import gym
#import collections
import numpy as np
import pandas as pd
import pickle

def splitreward(datapickle):
    #try:
    data = pd.read_pickle(r'datapickle')
    #except:
    #    print('Ikke en pickle')

    returntogo1 = []
    returntogo2 = []

    konstant = -1/10

    for i in range(pd.data.size):
        for t in pd.data['observations'][0].size:
            r2 = konstant * np.square(data['actions'][t])
            r1 = data['rewards'] - r2 # a og b er 1 i halfcheetah

            returntogo1[i].append(r1)
            returntogo2[i].append(r2)

        data[i].append(returntogo1)
        data[i].append(returntogo2)

    return data






