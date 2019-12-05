import requests
import numpy as np
import pandas as pd


def getAnswer(intentNum):
    data = pd.read_csv("data/Q&A_num.csv")
    data.columns = ["num", "question", "answer"]
    alist = np.array(data[["answer"]])
    totalAnswer = alist[int(intentNum) - 1]
    answer = str(totalAnswer)[2:len(str(alist[int(intentNum) - 1])) - 2]
    print(str(answer).replace("\\n", "\n").replace("\\r", "\r"))


def getIntent(question):
    baseurl = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/00a4e8c1-f8dc-4407-9e5b-5e09f0ac11fc?verbose=true&timezoneOffset=480&subscription-key=06c82fe138134244903014503f701129&q='
    url = baseurl + question
    response = requests.get(url)
    azure_answer = response.json()
    intent = azure_answer['topScoringIntent']['intent']
    # print(azure_answer['query'])
    # print(azure_answer['topScoringIntent']['intent'])
    print(azure_answer['topScoringIntent']['score'])
    getAnswer(intent)
