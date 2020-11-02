from Include.core.helpers import requestsApi
from Include.core.helpers.Utils import *
from .messages import *
import json



def getdata(usertgid):
    token = requestsApi.gettoken(usertgid)
    userData = requestsApi.getuser(token['id'])
    return userData

def getstudy(usertgid):
    data = requestsApi.get_user_study(usertgid)
    return data
def createstudy(usertgid,projectid):
    data = requestsApi.create_user_study(usertgid,projectid)
    return data
def deletestudy(usertgid,projectid):
    data = requestsApi.remove_user_study(usertgid,projectid)
    return data


def getprojects(usertgid):
    data = requestsApi.get_user_projects(usertgid)
    return data
def createproject(usertgid,projectid):
    data = requestsApi.create_user_project(usertgid,projectid)
    return data
def deleteproject(usertgid,projectid):
    data = requestsApi.remove_user_project(usertgid,projectid)
    return data

def getworks(usertgid):
    data = requestsApi.get_user_works(usertgid)
    return data
def creatework(usertgid,projectid):
    data = requestsApi.create_user_work(usertgid,projectid)
    return data
def deletework(usertgid,projectid):
    data = requestsApi.remove_user_work(usertgid,projectid)
    return data

def getcompetences(usertgid):
    data = requestsApi.get_user_competence(usertgid)
    return data
def addcompetences(usertgid,hashtag):
    data = requestsApi.add_competence_foruser(usertgid,hashtag)
    return data
def deletecompetences(usertgid,hashtag):
    data = requestsApi.remove_competence_foruser(usertgid,hashtag)

    return data

def gethobby(usertgid):
    data = requestsApi.get_user_hobby(usertgid)
    return data
def addhobby(usertgid,hashtag):
    data = requestsApi.add_hobby_foruser(usertgid, hashtag)
    return data
def deletehobby(usertgid,hashtag):
    data = requestsApi.remove_hobby_foruser(usertgid, hashtag)
    return data

def get_hobby_or_competence(owner):
    data = requestsApi.get_hobby_or_competence(owner)
    return data