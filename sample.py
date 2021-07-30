#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import csv
import sys
import random

if __name__ == "__main__":
    try:
        p = float(sys.argv[1])
        df = pd.read_csv("../dataset/train.csv",escapechar = "\\",quoting = csv.QUOTE_NONE,
            skiprows=lambda i: i>0 and random.random() > p)
        df.to_pickle("../dataset/sample-train.pkl")
        print("Pickle successfully created in datasets folder")
    except FileNotFoundError:
        print("train.csv must be inside folder named dataset which lies just outside codes folder")
