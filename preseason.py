import pandas as pd
import numpy as np

# read in mbb_2024_preseason_odds.csv
raw_preseason = pd.read_csv('mbb_2024_preseason_odds.csv')
raw_preseason = raw_preseason[["team_id", "team_short_display_name", "implied"]]
raw_preseason.rename(columns={'team_short_display_name': 'team_name'}, inplace=True)
print(raw_preseason.head())
raw_confs = pd.read_csv('mbb_2024_confs.csv')
print(raw_confs.head())