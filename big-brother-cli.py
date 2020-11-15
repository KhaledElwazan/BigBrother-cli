import threading
from threading import Thread
from globals import Globals
from device_info import DeviceInfo
import json
from heartbeat import HeartBeat
import time
from event import Event

if __name__ == '__main__':

    Globals()

    device = DeviceInfo(
        device_id='10', device_name='workstation 10', notes='I don not have any notes!')
    print(device.toJSON())

    while(True):

        hb = HeartBeat('10',device)
        thread = hb.run_in_background()
        thread.join()
        print(hb.toJSON())
        time.sleep(10)
