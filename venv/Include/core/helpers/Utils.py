import os

def check_photo(tgid):
    files_photo = os.listdir(os.getcwd()+'/core/media/photo')
    if files_photo:
        for i in files_photo:
            if int(i.split("__")[0]) == int(tgid):
                return True
    else:
        return False

def remove_old_photo(tgid):
    files_photo = os.listdir(os.getcwd() + '/core/media/photo')
    if files_photo:
        for i in files_photo:
            if int(i.split("__")[0]) == int(tgid):
                os.remove(os.getcwd() + '/core/media/photo/'+i)


def get_photo_id(tgid):
    files_photo = os.listdir(os.getcwd()+'/core/media/photo')
    if files_photo:
        for i in files_photo:
            if int(i.split("__")[0]) == int(tgid):
                return i.split("__")[1].split(".")[0]
    else:
        return False


