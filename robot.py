########### Python 3.6 #############
import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '06c82fe138134244903014503f701129',
}

params = {
    # Query parameter
    'q': '计算GPA',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

try:
    r = requests.get('https://chinaeast2.api.cognitive.azure.cn/luis/v2.0/apps/f90f0f86-ab01-49e8-88df-523e4ceb9e63',
                     headers=headers, params=params)
    print(r.json())

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
