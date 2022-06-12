import seaborn as sns
import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv(r'C:\Users\Bbjar\OneDrive\Skrivebord\tranformers02466\GitHub\Multiple_reward_DT\m_gym\decision_transformer\mRewardReturns.csv')
#evaluation/target_[6000, 6000]_returnR2_std
print("hey")

#yname = "evaluation/target_[6000, 6000]_returnR1_mean"
xname = "evaluation/target_[6000, 6000]_returnR_mean"
yname = "evaluation/target_[6000, 6000]_returnR2_std"
xname = "evaluation/target_[6000, 6000]_returnR1_mean"
xname = "evaluation/target_[6000, 6000]_returnR2_mean"


res = sns.lineplot(x=xname, y=yname, data=csv)
res1 = sns.lineplot(x=xname, y=yname, data=csv)
res2 = sns.lineplot(x=xname, y=yname, data=csv)

plt.show()


