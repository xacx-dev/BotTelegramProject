import json
import requests
from config import *

def check_vk_url(url):
    id = str(url).split("/")[len(str(url).split("/"))-1]
    data = requests.get('https://api.vk.com/method/users.get?user_ids='+id+'&access_token='+vk_token+'&v='+vk_version).json()
    try:
        data['response'][0]['id']
        return True
    except KeyError:
        return False


def check_pass(user_pass,tgid):
    data = requests.post(req_url + "/user/check_password?password=" + str(user_pass) + "&telid=" + str(tgid)).json()
    return data

def getuser(userid):
    data = requests.get(req_url + "/user/"+ str(userid)).json()
    return data

def getgroups():
    data = requests.get(req_url + "/group/").json()

    return data

def gettoken(tgid):
    data = requests.get(req_url + "/user/tg_secret/"+str(secure_code)+"/"+ str(tgid)).json()
    return data

def update(tgid,param,value):
    token_d = gettoken(tgid)
    id = token_d['id']
    token = token_d['token']
    data_u = getuser(id)
    params = {"telegram_id": tgid,
              "first_name": data_u['first_name'],
              "last_name": data_u["last_name"],
              "city": data_u['city'],
              "startdate": data_u['startdate'],
              "email": data_u['email'],
              "fb": data_u['fb'],
              "vk": data_u['vk'],
              "telnum": data_u['telnum'],
              "birthday": data_u['birthday'],
              "group": data_u['group'],
              "token": "string",
              "roots": 2
            }
    userData = json.loads(json.dumps(params))
    userData[param] = value
    userData['token'] = token
    requests.post(req_url + "/user/"+str(id)+"/"+str(token),data=json.dumps(userData))
