#import gym
#import collections
import numpy as np
import pandas as pd
import pickle

def splitreward(env, datatype):
    name = f'{env}-{datatype}-v2.pkl'
    data = pd.read_pickle(f'{name}')
    konstant = -1/10
    for traj in range(len(data)):
        r_forward = []
        r_control = []

        for timestep in range(len(data[traj]['rewards'])):
            r2 = konstant * np.square(np.linalg.norm(data[traj]['actions'][timestep]))
            r1 = data[traj]['rewards'][timestep] - r2 # a og b er 1 i halfcheetah
            r_forward.append(r1)
            r_control.append(r2)

        data[traj]['r1'] = np.array([r_forward]).squeeze()
        data[traj]['r2'] = np.array([r_control]).squeeze()

    n = 'm_reward'
    with open(f'{n}-{name}', 'wb') as f:
        pickle.dump(data, f)

#splitreward('halfcheetah','medium')
