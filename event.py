from globals import Globals
from device_info import DeviceInfo
from mother import Mother
from firebase_admin import db
import threading

class Event(Mother):

    ROOT = 'events'

    def __init__(self, device_info: DeviceInfo, project_name: str, progress: int = 0, to_finish: int = 0, notes: str = '') -> None:
        self.progress = progress
        self.to_finish = to_finish
        self.project_name = project_name
        self.notes = notes
        self.device_info = device_info.toJSON()

    def publish(self):
        # print(self.device_info['device_id'])
        # gs = Globals.getInstance()
        db.reference(Event.ROOT).child(self.project_name).child('progress').set(self.toJSON())


        