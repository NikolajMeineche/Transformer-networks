import gym
import collections
import numpy as np
import d4rl


#Function to convert a return in a specific environment into a normalized return to compare with Chen et al.
def ConvertReturn(reward, env, dataset):
    name = f'{env}-{dataset}-v2'
    Env = gym.make(name)
    returns = Env.get_normalized_score(reward)
    return returns

print(ConvertReturn(2100, 'hopper', 'medium'))



