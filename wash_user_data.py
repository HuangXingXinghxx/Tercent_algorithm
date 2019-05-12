import numpy as np
import pandas as pd
import csv
def user_data():
    str = "user_data.out"
    #str1 = "ad_operation.csv"
    data = []
    columns = ["a","b","c","d","e","f","g","h","i","j","k"]
    for line in open(str,'r'):
        line_content = line.split("\n")[0].split("\t")
        data.append(line_content)
    index = [x for x in range(len(data))]
    df = pd.DataFrame(data, index=index, columns=columns)
    df.to_csv("user_data.csv")
user_data()
