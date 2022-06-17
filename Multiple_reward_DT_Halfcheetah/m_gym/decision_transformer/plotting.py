import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'/home/adrian/PycharmProjects/Transformer-networks/Original_DT_gym/ReplicationValues.csv')
#pd.concat([df[[0]], df[15].str.split(', ', expand=True)], axis=1)


df.columns = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
print(df)
#yname = "evaluation/target_[6000, 6000]_returnR1_mean"
xname = "Iterations"
yname = "evaluation/target_[6000, 6000]_returnR2_std"
Hue = "Identifier"

sns.lineplot(data=fmri, x="timepoint", y="signal", hue=Hue, style="event")

plt.show()


