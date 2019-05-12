import numpy as np
import pandas as pd
import csv
from wash_ad_static_feature import ad_static_feature
def wash_totalExposureLog():
    str = "totalExposureLog.out"
    data = []
    columns = ["a","b","c","d","e","f","g","h","i","j"]
    for line in open(str,'r'):
        line_content = line.split("\n")[0].split("\t")
        data.append(line_content)
    index = [x for x in range(len(data))]
    df = pd.DataFrame(data,index=index,columns=columns)
    df.to_csv("ad_operation.csv")
wash_totalExposureLog()
