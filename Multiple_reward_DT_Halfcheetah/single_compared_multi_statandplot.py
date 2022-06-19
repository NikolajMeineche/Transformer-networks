import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
xname = "Iterations"
yname = "Mean return"
Hue = "Experiment"
sns.set_theme()

def data():
    single_hopper1422 = {'Iterations': ['1', '2', '3', '4', '5',] * 3,
                     'Experiment': ['Single objective hopper', ] * 15,
                     'Mean return': [375.726914292585,803.590359499449,1611.15345522065,726.831937886531,1091.73876264437,
                                     252.26356618338048,445.53652058754847,564.3929254417237,1099.4392270120522,919.7345519424238,
                                     1330.97821649208,1577.52975278197,1820.35233071641,1147.23140932762,1342.31047488595,
                                     ]}
    df_singlehopper_1422 = pd.DataFrame(single_hopper1422)
    df_singlehopper_1422 = df_singlehopper_1422[df_singlehopper_1422["Iterations"] == '5']
    single_halfcheetah4770 = {'Iterations': ['1', '2', '3', '4', '5', ] * 4,
                         'Experiment': ['Single objective halfCheetah', ] * 20,
                         'Mean return': [4811.52406198065,4898.37675720588,5017.11114772072,5005.37432810032,4961.1657811359,
                                         4823.754824067831,4911.259125909459,4892.470564958954,4917.208979305799,4960.968124216831,
                                         3534.9763804859203,3965.571404872683,3867.4045783765237,4040.4194227615126,4365.0116612130205,
                                         3502.728570985279,4206.222417906034,4242.381238781026,4130.824484059798,4180.7196523862585
                                         ]}
    df_singlehalfcheetah_4770 = pd.DataFrame(single_halfcheetah4770)
    df_singlehalfcheetah_4770 = df_singlehalfcheetah_4770[df_singlehalfcheetah_4770["Iterations"] == '5']
    multi_hopper = {'Iterations': ['1', '2', '3', '4', '5', ] * 3,
                         'Experiment': ['Multi objective Hopper', ] * 15,
                         'Mean return': [630.659222684852,1258.17578200469,819.948626050128,1492.96113334708,707.414712768447,
                                         641.612508020123, 537.656123950262, 1147.76641132203, 1040.89249874362,1591.15809110763,
                                         1681.76718471765,1750.15543506912,1020.18198915272,1593.57165792947,1862.3865078947]}
    df_multihopper_1422 = pd.DataFrame(multi_hopper)
    df_multihopper_1422  = df_multihopper_1422[df_multihopper_1422["Iterations"] == '5']


    multi_halfcheetah_5156 = {'Iterations': ['1', '2', '3', '4', '5', ] * 3,
                          'Experiment': ['Multi objective HalfCheetah', ] * 15,
                          'Mean return': [1290.3319714542897,1290.3319714542897,2532.5064312346553,3368.3255587980766,4015.458650589135,
                                          199.6461348012718,297.95234197735425,1534.8253646491669,4199.30779119717,4483.029812113761,
                                          297.95234197735425,426.43528231852883,3782.419686711959,4149.500308457168,4676.172944225289]}
    df_multihalfcheetah_5156 = pd.DataFrame(multi_halfcheetah_5156)
    df_multihalfcheetah_5156= df_multihalfcheetah_5156[df_multihalfcheetah_5156["Iterations"] == '5']

    return df_singlehopper_1422 ,df_singlehalfcheetah_4770,df_multihopper_1422,df_multihalfcheetah_5156
def stat():
    df_singlehopper_1422, df_singlehalfcheetah_4770, df_multihopper_1422, df_multihalfcheetah_5156 = data()

    print("Singlehopper vs Multihopper",stats.ttest_ind(df_singlehopper_1422['Mean return'], df_multihopper_1422['Mean return'], equal_var=False))
    print("Singlehalfcheetah vs multihalfcheetah",stats.ttest_ind(df_singlehalfcheetah_4770['Mean return'], df_multihalfcheetah_5156['Mean return'], equal_var=False))

    print("Mean of single hopper," + str(df_singlehopper_1422['Mean return'].mean())+ " variance =" +str(df_singlehopper_1422['Mean return'].std()))
    print("Mean of single halfcheetah," + str(df_singlehalfcheetah_4770['Mean return'].mean())+ " variance =" +str(df_singlehalfcheetah_4770['Mean return'].std()))

    print("Mean of multi hopper, " + str(df_multihopper_1422['Mean return'].mean())+ " variance =" +str(df_multihopper_1422['Mean return'].std()))
    print("Mean of multi halfcheetah, " + str(df_multihalfcheetah_5156['Mean return'].mean())+ " variance =" +str(df_multihalfcheetah_5156['Mean return'].std()))

stat()

def barplot():
    df_singlehopper_1422, df_singlehalfcheetah_4770, df_multihopper_1422, df_multihalfcheetah_5156 = data()
    df_hopper = pd.concat([df_singlehopper_1422,df_multihopper_1422], ignore_index=True)

    df_halfcheetah = pd.concat([df_singlehalfcheetah_4770,df_multihalfcheetah_5156], ignore_index=True)
    ax = sns.barplot(x="Experiment", y="Mean return", data=df_hopper).set(title='Bar plot of Hopper')
    plt.show()
    ax = sns.barplot(x="Experiment", y="Mean return", data=df_halfcheetah).set(title='Bar plot of HalfCheetah')
    plt.show()
barplot()