# -*- coding: utf-8 -*-
import vk, time, random

done = True
session = vk.Session(access_token = "b7690ac26382a9b074c4eb953e39a9ef0fb42c0e441df4813046ce1fbbae4d209b55f0af0f895844e8a6d")
api = vk.API(session)
sleep = 1.5

while done:
    sm = api.messages.get(count = 10)
    time.sleep(sleep)
    a = []
    maxi = 0
    nui = {}


    for i in sm[1:]:
        try: 
            if i['read_state'] == 0:
                a.append(i)
        except UnicodeEncodeError:
            api.messages.markAsRead(message_ids = i['mid'])
            time.sleep(sleep)
    for i in a:
        if i['date'] > maxi:
            maxi = i['date']
            nui = i

    print(nui)
    if nui != {}:
        if str(nui['body']).upper().__contains__('ПРИВЕТ'):
            try:
                api.messages.send(user_id = nui['uid'],message = 'Привет')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.send(user_id=nui['uid'], message='Hello')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
        if str(nui['body']).upper().__contains__('КАК ДЕЛА'):
            try:
                api.messages.send(user_id=nui['uid'], message= random.choice(['Норм', 'Прекрасно','Отлично','Все пучком','Лучше всех',
                                                                              'По тихой грусти', 'Всё ОК', 'Все хорошо', 'Ничего',
                                                                              'Как в "Брат 2"', 'Отлично, не дождёшься', 'Вчера сломал 2 ребра']))
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.send(user_id=nui['uid'], message='Ice')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
        else:
            try:
                api.messages.send(user_id=nui['uid'], message='Не понял')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.send(user_id=nui['uid'], message='И что это')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)


    










