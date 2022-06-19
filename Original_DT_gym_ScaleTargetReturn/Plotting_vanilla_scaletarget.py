import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()
pc_name = 'adrian'
xname = "Target_return"
yname = "evaluation/target_3600_return_mean"
Hue = "Experiment identifier"


#######################env = hopper, target = 0 #####################
df1 = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Vanilla_DT_gym_ScaleTargetReturn/ScaledTargetshopper0-1600.csv')
df3 = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Vanilla_DT_gym_ScaleTargetReturn/ScaledTargetshopper2000-3600.csv')
df2 = pd.concat([df1,df3], ignore_index= True)
targetreturn = [0., 400., 800., 1200., 1600., 2000., 2400., 2800., 3200., 3600.]
print(df2)
df2 = df2[ (df2['Experiment identifier'] == "environment = hopper, target = 0") | (df2['Experiment identifier'] == "environment = hopper, target = 400")|(df2['Experiment identifier'] == "environment = hopper, target = 800")|(df2['Experiment identifier'] == "environment = hopper, target = 1200")|(df2['Experiment identifier'] == "environment = hopper, target = 1600")|(df2['Experiment identifier'] == "environment = hopper, target = 2000")|(df2['Experiment identifier'] == "environment = hopper, target = 2400")|(df2['Experiment identifier'] == "environment = hopper, target = 2800")|(df2['Experiment identifier'] == "environment = hopper, target = 3200")|(df2['Experiment identifier'] == "environment = hopper, target = 3600")]
df2 = df2.drop_duplicates(subset=['Experiment identifier'],keep='last')
print('heyo')
print(df2)
df2 = df2.assign(Target_return=targetreturn)


g = sns.lineplot(data=df2, x=xname, y=yname)
sns.lineplot(x = targetreturn, y = targetreturn,linestyle='--',color='g')
plt.axvline(2400, color = 'r',linestyle='--' )
g.set(title='env = hopper')
g.set_xlabel("Target return")
g.set_ylabel("Mean return")
g.legend(labels=["Decision Transformer","Oracle","Best Trajectory"])

plt.show()

#######################env = halfcheeta, target  #####################
yname = 'evaluation/target_12000_return_mean'
df2 = pd.read_csv(r'/home/'+ str(pc_name)+'/PycharmProjects/Transformer-networks/Vanilla_DT_gym_ScaleTargetReturn/MultipleTargetsHalfcheetah_1it_forall.csv')
targetreturn = [0., 1333, 2666, 4000., 5333, 6666, 8000., 9333, 10666, 12000.]

df2 = df2[ (df2['Experiment identifier'] == "environment = halfcheetah, target = 0") | (df2['Experiment identifier'] == "environment = halfcheetah, target = 1333")|(df2['Experiment identifier'] == "environment = halfcheetah, target = 2666")|(df2['Experiment identifier'] == "environment = halfcheetah, target = 4000")|(df2['Experiment identifier'] == "environment = halfcheetah, target = 5333")|(df2['Experiment identifier'] == "environment = halfcheetah, target = 6666")|(df2['Experiment identifier'] == "environment = halfcheetah, target = 12000")|(df2['Experiment identifier'] == "environment = halfcheetah, target = 8000")|(df2['Experiment identifier'] == "environment = halfcheetah, target = 9333")|(df2['Experiment identifier'] == "environment = halfcheetah, target = 10666")]
df2 = df2.drop_duplicates(subset=['Experiment identifier'])

g = sns.lineplot(data=df2, x=xname, y=yname)
sns.lineplot(x = targetreturn, y = targetreturn,linestyle='--',color='g')
plt.axvline(2666, color = 'r',linestyle='--')

g.set(title='env = halfcheetah')
g.set_xlabel("Target return")
g.set_ylabel("Mean return")
g.legend(labels=["Decision Transformer","Oracle","Best Trajectory"])
plt.show()
