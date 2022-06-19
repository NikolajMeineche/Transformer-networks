import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()
###R1###
xname = "R1"
ynameR = "evaluation/target_[ 0.   -0.57]_length_mean"

Hue = "Experiment identifier"

df = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT_Hopper/m_gym/hopper_testR1values_fullset.csv')
Iteration = ['1','2','3','4','5','6','7','8','9','10']
df['Iterations'] = Iteration

sns.lineplot(data=df, x=xname, y=ynameR).set(title='Multiple return, env hopper')
sns.lineplot(data=df, x=xname, y=ynameR).set_xlabel("R1 conditioned return")
sns.lineplot(data=df, x=xname, y=ynameR).set_ylabel("Mean length")
#plt.legend(labels=["R","R1","R2"], title = "Reward functions")
plt.show()





###R2###
xname = "R2"
ynameR = "Length mean"

Hue = "Experiment identifier"

df1 = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT_Hopper/m_gym/new_hopper_testR2values2.csv')
df2 = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT_Hopper/m_gym/new_hopper_testR2values3+.csv')
df3 = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Multiple_reward_DT_Hopper/m_gym/new_hopper_testR2values8+og0.csv')

df = pd.concat([df1,df2,df3], ignore_index= True)

Iteration = ['1','2','3','4','5','6','7','8','9','10']
df['Iterations'] = Iteration

sns.lineplot(data=df, x=xname, y=ynameR).set(title='Multiple return, env hopper')
sns.lineplot(data=df, x=xname, y=ynameR).set_xlabel("R2 conditioned return")
sns.lineplot(data=df, x=xname, y=ynameR).set_ylabel("Mean length")
#plt.legend(labels=["","","Mean length"])
plt.show()


