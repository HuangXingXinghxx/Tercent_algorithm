import numpy as np
import pandas as pd
import csv
from wash_ad_static_feature import ad_static_feature
def ad_operation():
    str = "ad_operation.dat"
    #str1 = "ad_operation.csv"
    data = []
    columns = ["a","b","c","d","e"]
    for line in open(str,'r'):
        line_content = line.split("\n")[0].split("\t")
        data.append(line_content)
    index = [x for x in range(len(data))]
    df = pd.DataFrame(data,index=index,columns=columns)
    df.dropna()
    for column in list(df.columns):
        df = df.loc[df[column]!="",:]
        df = df.loc[df[column]!="-1",:]
    df_ad_static = ad_static_feature()
    #ad_operation出现的广告必须出现在ad_static_feature中
    df = pd.merge(df,df_ad_static,on=["a"])
    df.to_csv("ad_operation.csv")
ad_operation()
