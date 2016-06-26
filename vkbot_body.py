# -*- coding: utf-8 -*-
import vk, time, random
import lec_01


done = True
session = vk.Session(access_token = "3562299b8bf6d97e594c6e932eadda39c8caa182959c116a59dd478c356b43db4e14e991ebd9e4ffdf6e2")
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
        elif str(nui['body']).upper().__contains__('КАК ДЕЛА'):
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
        elif str(nui['body']).upper().__contains__('ДАВАЙ УЧИТЬ PYTHON'):
            try:
                api.messages.send(user_id=nui['uid'], message='Какую главу будем зубрить?')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
        elif str(nui['body']).upper().__contains__('ГЛАВА 1'):
            try:
                api.messages.send(user_id=nui['uid'], message=lec_01.__doc__)
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)                
        else:
            try:
                api.messages.send(user_id=nui['uid'], message='Не понял')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.send(user_id=nui['uid'], message='И что это?')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
        
                
                

    










