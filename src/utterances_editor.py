import csv
import numpy as np
import pandas as pd

data = pd.read_csv("data/QuestionListRedo_1.csv")
data.columns = ["Question", "num"]
nlist = data[["Question"]]
qlist = data[["num"]]
nlist = np.array(nlist)
qlist = np.array(qlist)


def writeIntotxt():
    with open("utterances.txt", "w") as f:
        for i in range(1, 517):
            stri = str(nlist[i])
            stri = stri[1:len(str(nlist[i])) - 1]
            if len(stri) == 1:
                stri = '00' + stri
            if len(stri) == 2:
                stri = '0' + stri
            question = str(qlist[i])
            question = question[2:len(str(qlist[i])) - 2]
            f.write('{\n' +
                    '\"text\": \"' + question + '\",\n' +
                    '\"intent\": \"' + stri + '\",\n' +
                    '\"entities\": []\n' +
                    "},\n")


writeIntotxt()
