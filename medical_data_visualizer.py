import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight']/((df['height']/100)**2)) > 25).astype(int)

# 3
df['gluc'] = (df['gluc'] != 1).astype(int)
df['cholesterol'] = (df['cholesterol'] != 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,
                id_vars=['cardio'],
                value_vars=sorted(['cholesterol','gluc','smoke','alco','active','overweight']),
                var_name = 'variable',
                value_name = 'Status')


    # 6
    df_cat = df_cat.value_counts().reset_index(name="total")
    

    # 7
    figr = sns.catplot(df_cat,
            x='variable',
            y='total',
            col='cardio',
            hue='Status',
            kind='bar',
            order=sorted(['cholesterol','gluc','smoke','alco','active','overweight']))


    # 8
    

    # 9
    figr.savefig('catplot.png')
    fig = figr.fig
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                (df['height'].between(df['height'].quantile(0.025),
                            df['height'].quantile(0.975),
                            inclusive='both')) &
        
                (df['weight'].between(df['weight'].quantile(0.025),
                            df['weight'].quantile(0.975),
                            inclusive='both'))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots()

    # 15
    ax = sns.heatmap(corr,
            mask=mask,
            linewidths=.7,
            annot=True,
            annot_kws={'size': 10},
            fmt='.1f')


    # 16
    fig.savefig('heatmap.png')
    return fig