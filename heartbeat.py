from globals import Globals
from device_info import DeviceInfo
from mother import Mother
from firebase_admin import db
import threading

class HeartBeat(Mother):

    ROOT = 'heart_beats'

    def __init__(self, device_info: DeviceInfo = None) -> None:
        self.device_info = device_info.toJSON()

    def publish(self):
        gs = Globals()
        gs.init()
        db.reference(HeartBeat.ROOT).child(
            self.device_info['device_id']).set(self.toJSON())
