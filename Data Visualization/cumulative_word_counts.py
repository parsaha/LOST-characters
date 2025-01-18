import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

s1_cumul = pd.DataFrame()
season = 1
for ep_num in range(1,25):
    episode_table = pd.read_csv("../Word Count Tables/Season "+str(season)+'/S'+str(season)+'E'+str(ep_num)+'.csv')
    s1_cumul = pd.concat([s1_cumul, episode_table], axis=0)
s1_cumul = s1_cumul.groupby(['Character']).sum().reset_index()

s2_cumul = pd.DataFrame()
season = 2
for ep_num in range(1,24):
    episode_table = pd.read_csv("../Word Count Tables/Season "+str(season)+'/S'+str(season)+'E'+str(ep_num)+'.csv')
    s2_cumul = pd.concat([s2_cumul, episode_table], axis=0)
s2_cumul = s2_cumul.groupby(['Character']).sum().reset_index()

s3_cumul = pd.DataFrame()
season = 3
for ep_num in range(1,23):
    episode_table = pd.read_csv("../Word Count Tables/Season "+str(season)+'/S'+str(season)+'E'+str(ep_num)+'.csv')
    s3_cumul = pd.concat([s3_cumul, episode_table], axis=0)
s3_cumul = s3_cumul.groupby(['Character']).sum().reset_index()

s4_cumul = pd.DataFrame()
season = 4
for ep_num in range(1,14):
    episode_table = pd.read_csv("../Word Count Tables/Season "+str(season)+'/S'+str(season)+'E'+str(ep_num)+'.csv')
    s4_cumul = pd.concat([s4_cumul, episode_table], axis=0)
s4_cumul = s4_cumul.groupby(['Character']).sum().reset_index()

s5_cumul = pd.DataFrame()
season = 5
for ep_num in range(1,17):
    episode_table = pd.read_csv("../Word Count Tables/Season "+str(season)+'/S'+str(season)+'E'+str(ep_num)+'.csv')
    s5_cumul = pd.concat([s5_cumul, episode_table], axis=0)
s5_cumul = s5_cumul.groupby(['Character']).sum().reset_index()

s6_cumul = pd.read_csv("../Word Count Tables/Season 6/S6E1.csv")
season = 6
for ep_num in range(3,18):
    episode_table = pd.read_csv("../Word Count Tables/Season "+str(season)+'/S'+str(season)+'E'+str(ep_num)+'.csv')
    s6_cumul = pd.concat([s6_cumul, episode_table], axis=0)
s6_cumul = s6_cumul.groupby(['Character']).sum().reset_index()

show_cumul = pd.concat([s1_cumul, s2_cumul, s3_cumul, s4_cumul, s5_cumul, s6_cumul], axis=0).groupby(['Character']).sum().reset_index()

top_ten = show_cumul.reset_index().sort_values(['Word Count'], ascending=False)[:10]

s1_cumul.loc[s1_cumul.shape[0]+1] = ['BEN', 0]
s2_cumul.replace('GALE','BEN', inplace=True)
s1_cumul.loc[s1_cumul.shape[0]+1] = ['DESMOND', 0]
s3_cumul.loc[s1_cumul.shape[0]+1] = ['MICHAEL', 0]
s5_cumul.loc[s1_cumul.shape[0]+1] = ['MICHAEL', 0]