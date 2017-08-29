# token - https://oauth.vk.com/authorize?client_id=6163289&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos ,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token
# docs - https://vk.com/dev/manuals
# vk - https://pikabu.ru/story/api_vkontakte_dlya_python_3961240
# https://oauth.vk.com/blank.html#access_token=18997adcd84d5669c964c15a2002b065105ab78afb3ad8b4bbc101ab9bef7110e6cf410abcbe6687fb10f&expires_in=0&user_id=197610904
import json
import requests
import vk
token = "18997adcd84d5669c964c15a2002b065105ab78afb3ad8b4bbc101ab9bef7110e6cf410abcbe6687fb10f"
method = "groups.getMembers"
method_2='friends.get'
v = 5.68
session = vk.Session(access_token=token)
api = vk.API(session)
# задаем адрес, токен, метод, версию и параметры
url = "https://api.vk.com/method/{method}?{params}&access_token={token}&v={version}"
# делаем первый запрос, чтобы узнать количество
params = "group_id=goto_msk&offset={0}"
response = requests.get(url.format(method=method, version=v, params=params.format(0), token=token))
result = response.json()
# узнаем количество
i=1
for i in range (1):#(response{count}):
    user_id=result[{items[i]}]
    print(response[items[i]])
    resp = requests.get(url.format(method=method_2, version=v, params=params2.format(0), token=token))
    friends = resp.json()
    print(friends)
'''for friend in friends:
        fc=0
        if api.isMember(group_id='goto_msk',user_id=friend) is True:
            fc=fc+1
            print(user(),fc)
    user=user[fc]
# сортируем
mx=0
for user in users:
    if user[fc]>mx:
        mx=user[fc]
print(mx)'''

