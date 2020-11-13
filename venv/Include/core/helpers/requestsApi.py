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

def gettoken(tgid):
    data = requests.get(req_url + "/user/tg_secret/"+str(secure_code)+"/"+ str(tgid)).json()
    return data

def check_pass(user_pass,tgid):
    data = requests.post(req_url + "/user/check_password?password=" + str(user_pass) + "&telid=" + str(tgid)).json()
    return data

def getuser(userid):
    data = requests.get(req_url + "/user/"+ str(userid)).json()
    return data
def getusers_in_group(group_id):
    data = requests.get(req_url + "/user/group/" + str(group_id)).json()
    return data
#----------------finder-----------------#
def find_user_lastname(last_name):
    data = requests.get(req_url + "/user/search/ln/"+ str(last_name)).json()
    if data == []:
        return False
    else:
        return data
def find_user_tg(telegram_id):
    data = requests.get(req_url + "/user/search/tg/"+ str(telegram_id)).json()
    if data == []:
        return False
    else:
        return data
def find_user_vk(vk_id):
    data = requests.get(req_url + "/user/search/vk/"+ str(telegram_id)).json()
    if data == []:
        return False
    else:
        return data

def find_user_fb(vk_id):
    data = requests.get(req_url + "/user/search/fb/"+ str(telegram_id)).json()
    if data == []:
        return False
    else:
        return data

#----------------------------------------#



#----------------------------------------#
#study
def get_user_study(tgid):
    data = requests.get(req_url + "/study/user/"+ str(tgid)).json()
    return data
def create_user_study(tgid,post_data):
    token = gettoken(tgid)['token']
    data = requests.post(req_url + "/study/"+ str(tgid)+"/"+str(token),data=json.dumps(post_data)).json()
    return data
def remove_user_study(tgid,work_id):
    token = gettoken(tgid)['token']
    data = requests.delete(req_url + "/study/"+ str(tgid)+"/"+str(token)+"/"+str(work_id)).json()
    return data
#----------------------------------------#

#----------------------------------------#
#work
def get_user_works(tgid):
    data = requests.get(req_url + "/work/user/"+ str(tgid)).json()
    return data
def create_user_work(tgid,post_data):
    token = gettoken(tgid)['token']
    data = requests.post(req_url + "/work/"+ str(tgid)+"/"+str(token),data=json.dumps(post_data)).json()
    return data
def remove_user_work(tgid,work_id):
    token = gettoken(tgid)['token']
    data = requests.delete(req_url + "/work/"+ str(tgid)+"/"+str(token)+"/"+str(work_id)).json()
    return data
#----------------------------------------#

#----------------------------------------#
#projects
def get_user_projects(tgid):
    data = requests.get(req_url + "/project/user/"+ str(tgid)).json()
    return data
def create_user_project(tgid,post_data):
    token = gettoken(tgid)['token']
    data = requests.post(req_url + "/project/"+ str(tgid)+"/"+str(token),data=json.dumps(post_data)).json()
    return data
def remove_user_project(tgid,project_id):
    token = gettoken(tgid)['token']
    data = requests.delete(req_url + "/project/"+ str(tgid)+"/"+str(token)+"/"+str(project_id)).json()
    return data
#----------------------------------------#


#--------------hobby--------------------#
def get_user_hobby(userid):
    data = requests.get(req_url + "/hobby/"+ str(userid)).json()
    return data
def get_users_byhobby(hashtag):
    data = requests.get(req_url + "/hobby/users/"+ str(hashtag)).json()
    return data
def add_hobby_foruser(tgid,hashtag):
    token = gettoken(tgid)['token']
    data = requests.get(req_url + "/hobby/"+ str(tgid)+"/"+str(token)+"/"+str(hashtag)).json()
    return data
def remove_hobby_foruser(tgid,hashtag):
    token = gettoken(tgid)['token']
    data = requests.delete(req_url + "/hobby/"+ str(tgid)+"/"+str(token)+"/"+str(hashtag)).json()
    return data
#----------------------------------------#
def get_hobby_or_competence(param):
    data = requests.get(req_url + "/tip/" + str(param)).json()
    return data
#---------------Competence-------------------#
def get_user_competence(userid):
    data = requests.get(req_url + "/competence/"+ str(userid)).json()
    return data
def get_users_bycompetence(hashtag):
    data = requests.get(req_url + "/competence/users/"+ str(hashtag)).json()
    return data
def add_competence_foruser(tgid,hashtag):
    token = gettoken(tgid)['token']
    data = requests.get(req_url + "/competence/"+ str(tgid)+"/"+str(token)+"/"+str(hashtag)).json()
    return data
def remove_competence_foruser(tgid,hashtag):
    token = gettoken(tgid)['token']
    data = requests.delete(req_url + "/competence/"+ str(tgid)+"/"+str(token)+"/"+str(hashtag)).json()
    return data
#----------------------------------------#

def getUserData(tgid):
    token = gettoken(tgid)
    userData = getuser(token['id'])
    return userData


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
