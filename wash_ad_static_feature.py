import numpy as np
import pandas as pd
import csv
def ad_static_feature():
    str = "ad_static_feature.out"
    #str1 = "ad_static_feature.csv"
    data = []
    columns = ["a","b","c","d","e","f","g"]
    for line in open(str,'r'):
        line_content = line.split("\n")[0].split("\t")
        if(len(line_content)<7):#异常数据
            continue
        else:
            data.append(line_content)
    index = [x for x in range(len(data))]
    df = pd.DataFrame(data,index=index,columns=columns)
    df.dropna()
    for column in list(df.columns):
        df = df.loc[df[column]!="",:]#异常数据
        df = df.loc[df[column]!="-1",:]#异常数据
        df = df.loc[df[column] != "0", :]#异常数据
    list_delete = []
    for index in list(df.index):
        if "," in df.loc[index,"f"]:
            list_delete.append(index);
    df = df.drop(list_delete,axis=0)
    df.to_csv("ad_static_feature.csv")
    return df
ad_static_feature()
