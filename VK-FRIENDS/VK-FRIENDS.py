import vk,time

#мой ID = 160926229
#ada ID = 371412182

session = vk.Session(access_token='3e39f64310d6265db34707e865e2f1de96e90830611ad9a4c0169b239c72af62ed01250a0012a1b9d3c28')
api = vk.API(session)

for i in api.users.getFollowers(user_id = 371412182,count = 20, v = 5.52)['items']:
    print (i)
    api.friends.add(user_id = i , v = 5.52 )
