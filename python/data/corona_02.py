import requests, json 
import pandas as pd 
from datetime import datetime , timedelta
import os.path

# BASE_DIR = os.path.dirname((os.path.relpath("./")))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, './pythonDBProcess/secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg
    
url = 'https://apis.data.go.kr/1352000/ODMS_COVID_02/callCovid02Api'

today = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
print(today)

params = '?serviceKey=' + get_secret("data_apiKey")
params += "&pageNo=1"
params += "&numOfRows=500"
params += "&apiType=JSON"
params += "&status_dt="+str(today)

url += params
print(url)

response = requests.get(url)
print(response)
print('-'*50)

contents = response.text
print(type(contents))
print(contents)
print('-'*50)

dictionary = json.loads(contents)
print(type(dictionary))
print(dictionary)
print('-'*50)

items = dictionary['items']
print(type(items))
print(items)
print('-'*50)

items_dict = {key:value for key, value in enumerate(items)}
print(type(items_dict))
print(items_dict)
print('-'*50)

items = items_dict[0]
print(type(items))
print(items)
print('-'*50)

df = pd.DataFrame(items, index=[0]).rename(index={0:'result'}).T
print(type(df))
print(df)
print('-'*50)