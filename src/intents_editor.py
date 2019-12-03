import numpy as np
import pandas as pd

intentNum = '120'
data = pd.read_csv("data/Q&A_num.csv")
data.columns = ["num", "question", "answer"]
alist = np.array(data[["answer"]])
totalAnswer = alist[int(intentNum) - 1]
answer = str(totalAnswer)[2:len(str(alist[int(intentNum) - 1])) - 2]
print(answer)
