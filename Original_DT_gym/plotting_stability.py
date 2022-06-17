import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme()
pc_name = 'adrian'

#######################K-values#####################
df = pd.read_csv(r'/home/'+str(pc_name)+'/PycharmProjects/Transformer-networks/Original_DT_gym/ReplicationValues.csv')

df = df[ (df['Variable iterated over'] == "K = 1") | (df['Variable iterated over'] == "K = 3")| (df['Variable iterated over'] == "K = 8")| (df['Variable iterated over'] == "K = 20")]

xname = "Iteration"
yname = "evaluation/target_3600_return_mean"
Hue = "Variable iterated over"

sns.lineplot(data=df, x=xname, y=yname, hue=Hue).set(title='Context length budget transformer')# style="event")
plt.show()

#######################embed_dim -values#####################

df = pd.read_csv(r'/home/'+str(pc_name)+'/PycharmProjects/Transformer-networks/Original_DT_gym/ReplicationValues.csv')

df = df[ (df['Variable iterated over'] == "embed_dim  = 32") | (df['Variable iterated over'] == "embed_dim  = 128")]

xname = "Iteration"
yname = "evaluation/target_3600_return_mean"
Hue = "Variable iterated over"

sns.lineplot(data=df, x=xname, y=yname, hue=Hue).set(title='Embedded dimensions budget transformer')# style="event")
plt.show()

#######################n_layer -values#####################

df = pd.read_csv(r'/home/'+str(pc_name)+'/PycharmProjects/Transformer-networks/Original_DT_gym/ReplicationValues.csv')

df = df[ (df['Variable iterated over'] == "n_layer = 1") | (df['Variable iterated over'] == "n_layer = 3")]

xname = "Iteration"
yname = "evaluation/target_3600_return_mean"
Hue = "Variable iterated over"

sns.lineplot(data=df, x=xname, y=yname, hue=Hue).set(title='N-layer budget transformer')# style="event")
plt.show()