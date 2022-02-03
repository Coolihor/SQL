#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
df.sort_values(by=['grps', 'vals'], ascending = [True,False], inplace = True)
df.set_index('grps', inplace = True)
df_concat = pd.concat([df.loc['a'][:3], df.loc['b'][:3],df.loc['c'][:3]])
df_concat.groupby('grps').agg(sum)

