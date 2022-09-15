import os
import json

pc_name = os.name
username = os.getlogin()
folder_list = os.listdir()
env = os.environ
distination = os.getcwd()
#os = os.uname()

#print(f"{pc_name = }, {distination = }, {folder_list = }, {env = }, {username = }, {os= } ")

massive = {
                'pc_name': pc_name,
                'dist_name': distination,
                'folder_list': folder_list,
                'env': list(env),
                'username': username,
    }
print(massive)

with open('os_report.json', 'w') as fh:
	json.dump(massive, fh)