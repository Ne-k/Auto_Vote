import requests
import json

url = "https://campustech.org/api/2.0/contacts/send/email/user"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Origin": "https://campustech.org",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://campustech.org/tech-the-halls",
    "Cookie": 'permanent_cookie={"id":"FBC5462D-83CF-4535-BA4A-A15969F2EB35"}; user_search_params={}; '
              'session_cookie={"id":"101E927E-D6D0-49A6-B9F0-196CC6844446"}; '
              'campustech_org.sid=s%3AXYdhKmeVndj9KNkSielawVWSJlrCyj7E.Jqth9EVhT8KnmMsatX21KbNy5ydjr41Q2zXSc2tjA5s',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}
payload = {
    "subject": "Verification Code Email",
    "type": "verificationCodeEmailConfigs",
    "emailTo": ["username.lilrice@gmail.com"],
    "fields": {"[submitter_name]": "Weee"},
    "entry_id": "6048a009-143c-42cc-98be-b312c45d5e73"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.status_code)
print(response.text)
