import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()

xname = "R1"
ynameR = "evaluation/target_[   0. -386.]_return_mean"
ynameR1 = "evaluation/target_[   0. -386.]_returnR1_mean"
ynameR2 = "evaluation/target_[   0. -386.]_returnR2_mean"
Hue = "Experiment identifier"

df = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT/m_gym/FA_R1values.csv')
Iteration = ['1','2','3','4','5','6','7','8','9','10']
df['Iterations'] = Iteration
"""
sns.lineplot(data=df, x=xname, y=ynameR).set(title='Multiple return, env halfcheetah')
sns.lineplot(data=df, x=xname, y=ynameR1).set_xlabel("R1 conditioned return")
sns.lineplot(data=df, x=xname, y=ynameR2).set_ylabel("Mean return")
plt.legend(labels=["R","R1","R2"], title = "Reward functions")
plt.show()



p = sns.lineplot(data=df, x=xname, y=ynameR2,palette=['g'], color = 'g')
p.set(title='Multiple return, env halfcheetah')
p.set_xlabel("R1 conditioned return")
p.set_ylabel("Mean return")

plt.legend(labels=["R2"], title = "Reward function")

plt.show()
"""
############################PlotforR2################################
df = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT/m_gym/FA_R2values.csv')
xname = "R2"
ynameR = "evaluation/target_[5156.    0.]_return_mean"
ynameR1 = "evaluation/target_[5156.    0.]_returnR1_mean"
ynameR2 = "evaluation/target_[5156.    0.]_returnR2_mean"

Iteration = ['1','2','3','4','5','6','7','8','9','10']
df['Iterations'] = Iteration

sns.lineplot(data=df, x=xname, y=ynameR).set(title='Multiple return, env halfcheetah')
sns.lineplot(data=df, x=xname, y=ynameR1).set_xlabel("R2 conditioned return")
sns.lineplot(data=df, x=xname, y=ynameR2).set_ylabel("Mean return")
plt.legend(labels=["R","R1","R2"], title = "Reward functions")
plt.show()



p = sns.lineplot(data=df, x=xname, y=ynameR2,palette=['g'], color = 'g')
p.set(title='Multiple return, env halfcheetah')
p.set_xlabel("R2 conditioned return")
p.set_ylabel("Mean return")

plt.legend(labels=["R2"], title = "Reward function")

plt.show()