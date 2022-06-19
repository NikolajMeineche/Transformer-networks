import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()

xname = "R1"
ynameR = "evaluation/target_[ 0.   -0.57]_return_mean"
ynameR1 = "evaluation/target_[ 0.   -0.57]_returnR1_mean"
ynameR2 = "evaluation/target_[ 0.   -0.57]_returnR2_mean"
Hue = "Experiment identifier"

df = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT_Hopper/m_gym/hopper_testR1values_fullset.csv')
Iteration = ['1','2','3','4','5','6','7','8','9','10']
df['Iterations'] = Iteration

sns.lineplot(data=df, x=xname, y=ynameR).set(title='Multiple return, env hopper')
sns.lineplot(data=df, x=xname, y=ynameR1).set_xlabel("R1 conditioned return")
sns.lineplot(data=df, x=xname, y=ynameR2).set_ylabel("Mean return")
plt.legend(labels=["R","R1","R2"], title = "Reward functions")
plt.show()



p = sns.lineplot(data=df, x=xname, y=ynameR2,palette=['g'], color = 'g')
p.set(title='Multiple return, env hopper')
p.set_xlabel("R1 conditioned return")
p.set_ylabel("Mean return")

plt.legend(labels=["R2"], title = "Reward function")

plt.show()

############################PlotforR2################################
xname = "R2"
ynameR = "Return mean"
ynameR1 = "R1 mean"
ynameR2 = "R2 mean"
Hue = "Experiment identifier"

df1 = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT_Hopper/m_gym/new_hopper_testR2values2.csv')
df2 = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT_Hopper/m_gym/new_hopper_testR2values3+.csv')
df3 = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT_Hopper/m_gym/new_hopper_testR2values8+og0.csv')

df = pd.concat([df1,df2,df3], ignore_index= True)
print(df)
Iteration = ['1','2','3','4','5','6','7','8','9','10']
df['Iterations'] = Iteration

sns.lineplot(data=df, x=xname, y=ynameR).set(title='Multiple return, env hopper')
sns.lineplot(data=df, x=xname, y=ynameR1).set_xlabel("R2 conditioned return")
sns.lineplot(data=df, x=xname, y=ynameR2).set_ylabel("Mean return")
plt.legend(labels=["R","R1","R2"], title = "Reward functions")
plt.show()



p = sns.lineplot(data=df, x=xname, y=ynameR2,palette=['g'], color = 'g')
p.set(title='Multiple return, env hopper')
p.set_xlabel("R2 conditioned return")
p.set_ylabel("Mean return")

plt.legend(labels=["R2"], title = "Reward function")

plt.show()