import threading
from threading import Thread
from globals import Globals
from device_info import DeviceInfo
import json

from event import Event

if __name__ == '__main__':

    Globals()
    dinfo = DeviceInfo('123')
    dinfo.device_id = '123'
    dinfo.device_name = 'mmoniem'
    dinfo.notes = 'notes'

    event = Event(device_info=dinfo,project_name='eurus: peres decomposition')
    event.progress = 10
    event.to_finish = 100
    # print(JSONEncoder.encode(event))

    # print(event.toJSON())
    # print(json.dumps(event.toJSON()))
    # for i in range(5):
    # event.run_in_background() 
    # event.progress = 10
    # event.run_in_background()
    threads = []
    event.progress = 50
    threads.append(event.run_in_background())
    print('00')
    event.progress = 100
    event.run_in_background() 
    event.progress = 50
    threads.append(event.run_in_background())
    print('11')
    event.progress = 100
    event.run_in_background() 
    event.progress = 50
    threads.append(event.run_in_background())
    print('22')
    event.progress = 100
    event.run_in_background() 
    threads.append(event.run_in_background())
    event.progress = 50
    threads.append(event.run_in_background())
    print('33')
    event.progress = 100
    event.run_in_background() 
    event.progress = 50
    threads.append(event.run_in_background())
    print('44')
    event.progress = 100
    event.run_in_background() 
    event.progress = 50
    threads.append(event.run_in_background())
    print('5')
    # event.progress = 100
    # event.run_in_background() 
    # threads.append(event.run_in_background())


    for i in threads:
        i.join()
        print('-')


    # cred = credentials.Certificate(
    #     "big-brother-df0a9-firebase-adminsdk-fv0o6-90519d1867.json")
    # # firebase_admin.initialize_app(cred)
    # firebase_admin.initialize_app(cred, {
    #     'databaseURL': 'https://big-brother-df0a9.firebaseio.com'})

    # # As an admin, the app has access to read and write all data, regradless of Security Rules
    # project_name = 'eurus-peres decompositions'
    # projects_root = 'projects'
    # ref = db.reference('{}/{}'.format(projects_root, project_name))
    # ref.child('khaled').set('mohamed')
    # print(ref.get())
