import pandas as pd
import os
import glob

os.sys.path.append(os.path.dirname(os.path.abspath('..')))

filenames = glob.glob('../long_term_WQ_data_Canada/*.csv')

dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename, encoding = "ISO-8859-1"))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)

big_frame[big_frame['SITE_NO'] == 'ON02GG0004'].index.tolist()
# returns empty list -> no data on Great Lakes
