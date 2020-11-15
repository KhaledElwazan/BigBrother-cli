import firebase_admin
from globals import Globals
from device_info import DeviceInfo
from mother import Mother
from firebase_admin import db
import threading
import time

class HeartBeat(Mother):

    ROOT = 'heartbeats'

    def __init__(self, id:str,device_info: DeviceInfo ) -> None:
        self.device_info = device_info.toJSON()
        self.timestamp=timestamp()
        self.id = id

    def publish(self):
        # gs = Globals()
        # gs.init()
        db.reference(HeartBeat.ROOT).child(
            self.device_info['device_id']).set(self.toJSON())
            
def timestamp():
    return int(round(time.time()*1000))