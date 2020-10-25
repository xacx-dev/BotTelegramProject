import os

def check_photo(tgid):
    files_photo = os.listdir(os.getcwd()+'/core/media/photo')
    if files_photo:
        for i in files_photo:
            if int(i.split("__")[0]) == int(tgid):
                return True
            else:
                return False
    else:
        return False
