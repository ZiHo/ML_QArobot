import csv
import numpy as np
import pandas as pd

data = pd.read_csv("data/QuestionListRedo.csv")
data.columns = ["Question", "num"]
qlist = data[["Question"]]
qlist = np.array(qlist)

with open("utterances.txt", "w") as f:
    for i in range(1, 121):
        stri = str(i)
        if len(stri) == 1:
            stri = '00' + stri
        if len(stri) == 2:
            stri = '0' + stri
        question = str(qlist[i-1])
        question = question[2:len(str(qlist[i-1]))-2]
        f.write('{\n' +
                '\"text\": \"' + question + '\",\n' +
                '\"intent\": \"' + stri + '\",\n' +
                '\"entities\": []\n' +
                "},\n")
