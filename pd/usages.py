# -*- coding: utf-8 -*-
import pandas as pd


# 按...分组，按...排序
df = pd.DataFrame()
def valsort(row):
    row['absvalue'] = row['value'].abs()
    return row

gdf = df.groupby(['item', 'itemID']).apply(valsort).sort(['item', 'absvalue'],
                                                    ascending=[1,0]).reset_index()