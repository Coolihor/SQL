#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
df.sort_values(by=['grps', 'vals'], inplace = True)
dd = df[((df['grps']=='a')&(df['vals']>4))|((df['grps']=='b')&(df['vals']>3))|((df['grps']=='c')&(df['vals']>21))]
dd.groupby(['grps']).agg(sum)

