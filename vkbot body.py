# -*- coding: utf-8 -*-
import vk
import time

done = True
session = vk.Session(access_token = "52df445db46eb040d574707879844e7fc3b099694f8034e2b671a26fb975bd49c52605e51e3bfd411aa76")
api = vk.API(session)


while done:
    sm = api.messages.get(count = 10)
    a = []
    maxi = 0
    nui = {}

    for i in sm[1:]:
        try: 
            if i['read_state'] == 0:
                a.append(i)
        except UnicodeEncodeError:
            api.messages.markAsRead(message_ids = i['mid'])
            
            
    for i in a:
        if i['date'] > maxi:
            maxi = k['date']
            nui = k
    










